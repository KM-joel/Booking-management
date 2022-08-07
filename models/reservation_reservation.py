from odoo import fields, models, api,_
from odoo.exceptions import ValidationError
import datetime


class Reservation(models.Model):

	_name = 'booking.management.reservation'
	_description = 'management of reservation'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_order = 'reference desc'

	reference = fields.Char('Reference', readonly=True, required=True, default='/')
	client_id = fields.Many2one('res.users', 'Client', required=True, tracking=1)
	article_ids = fields.One2many('product.product', 'reservation_id',required=True, tracking=True)
	article_id = fields.Many2one('product.product', 'Article', required=True, tracking=2)
	reservation_date = fields.Date('Reservation date', required=True, tracking=3)
	reservation_duration_hours = fields.Integer('Duration in hours')
	reservation_duration_day = fields.Integer('Duration in day')
	reservation_duration_month = fields.Integer('Durartion in month')
	end_date_reservation = fields.Date('End date of reservation', readonly=True, tracking=True, compute='_compute_end_date_reservation')
	state = fields.Selection([
					('new', 'New'),
					('confirmed', 'Confirmed'),
					('validated', 'Validated'),
					('canceled', 'Canceled')], default='new', tracking=3)
	devis_id = fields.Many2one('sale.order', 'Quote')
	partner_id = fields.Many2one('res.partner', related='devis_id.partner_id', string='Partner')
	total_duration_hours = fields.Float(string='Total duration hours', compute='_compute_total_duration_hours', store=1)

	progress = fields.Integer(string='Progress', compute='_compute_progress')
	reference_record = fields.Reference(selection=[('sale.order', 'Sales'), ('account.move', 'Invoices')], string='Records')

	@api.model
	def create(self, vals):
		if vals.get('reference', '/') == '/':
			vals['reference'] = self.env['ir.sequence'].next_by_code('ref.sequence.code') or '/'
		result = super(Reservation, self).create(vals)
		return result

	def name_get(self):
		return [(record.id, '[%s]/%s/%s' % (record.reference, record.client_id.name, record.article_id.name)) for record in self]
		# result = []
		# for reserv in self:
		# 	name = '[%s]/%s/%s'  % (reserv.reference, reserv.client_id.name, reserv.article_id.name)
		# 	result.append((reserv.id, name))
		# return result

	@api.depends('reservation_date', 'reservation_duration_hours', 'reservation_duration_day','reservation_duration_month')
	def _compute_end_date_reservation(self):
		for t in self:
			duration = datetime.timedelta(days=t.reservation_duration_day + (t.reservation_duration_month*30),
			                              hours=t.reservation_duration_hours)
			if not (t.reservation_date and duration):
				t.end_date_reservation = t.reservation_date
				continue
			start_date = fields.Datetime.from_string(t.reservation_date)
			t.end_date_reservation = start_date + duration

	def next_step(self):
		self.ensure_one()
		if self.state == 'new':
			return self.write({'state': 'confirmed'})
		elif self.state == 'confirmed':
			# return {
			# 	'type': 'ir.actions.client',
			# 	'tag': 'display_notification',
			# 	'params': {
			# 		'type': 'success',
			# 		'message': _("Vous avez valide votre reservation avec success, Mr. : %s") % self.client_id.name,
			# 		'sticky': False,
			# 	}
			# }
			self.write({'state': 'validated'})
			type_notif = 'success' if self.env['booking.management.reservation'].search_count([('client_id', '=', self.client_id.id), ('state', '=', 'validated')]) > 1 else 'warning'
			if type_notif == 'success':
				type_mess = _("Vous avez valide votre reservation avec success cher client %s")
			else:
				type_mess = _("Vous avez valide votre reservation avec success Mr. %s")
			return {
				'type': 'ir.actions.client',
				'tag': 'display_notification',
				'params': {
					'type': type_notif,
					'title': _("Reservation"),
					'message': type_mess % self.client_id.name,
					'sticky': False,
					'next': {
						'type': 'ir.actions.act_window_close'
					},
				}
			}

		else:
			raise ValidationError('You have already confirmed your reservation')

	def canceled_reservation(self):
		self.ensure_one()
		if self.state == 'validated':
			return self.write({'state': 'canceled'})
		elif self.state == 'canceled':
			return self.write({'state': 'new'})
		else:
			raise ValidationError('Please create your reservation again')

	# @api.depends('reservation_duration_day', 'reservation_duration_hours')
	def create_quote(self):
		self.ensure_one()
		duration = (self.reservation_duration_month*30 + self.reservation_duration_day)*24 + self.reservation_duration_hours
		price = 0
		order = self.env['sale.order'].search([], limit=1)
		if duration < 10:
			price = 150.00
		else:
			price = 140.00
		sale_order_cost = order.create({
			'date_order': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
			'name': self.reference,
			'active_devis': True,
			'order_line': [
				(0, 0, {'price_unit': price, 'product_uom_qty': duration, 'product_id': self.article_id.id})
			],
			'partner_id': self.client_id.partner_id.id,
			'pricelist_id': order.pricelist_id.id
		})
		self.devis_id = sale_order_cost

	@api.depends('reservation_duration_hours', 'reservation_duration_month', 'reservation_duration_day')
	def create_many_quotation(self):
		users = set(self.client_id)
		price = 0
		for user in users:
			reserve = [record for record in self if record.client_id == user]
			sale_order_cost = self.env['sale.order'].create({
				'partner_id': user.partner_id.id,
				'active_devis': True,
			})
			for res in reserve:
				if res.state == 'validated':
					duration =  res.reservation_duration_hours + (res.reservation_duration_month*30 + res.reservation_duration_day)*24
					if duration < 10:
						price = 150.00
					else:
						price = 140.00
					sale_order_cost.order_line = [(0, 0, {
						'name': res.reference,
						'price_unit': price,
						'product_uom_qty': duration,
						'product_id': res.article_id.id,
					})]
					res.devis_id = sale_order_cost
				else:
					raise ValidationError('You cannot create a quote for an invalid reservation')

	@api.depends('reservation_duration_month', 'reservation_duration_day', 'reservation_duration_hours')
	def _compute_total_duration_hours(self):
		for rec in self:
			rec.total_duration_hours = rec.reservation_duration_hours + (rec.reservation_duration_month*30 + rec.reservation_duration_day)*24

	def extern_link_whatsapp(self):
		self.ensure_one()
		msg = 'Hey %s, your reservation number is %s.' %(self.client_id.name, self.reference)
		whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' %(self.client_id.phone, msg)
		return {
			'type': 'ir.actions.act_url',
			'target': 'new', # or 'self'
			'url': whatsapp_api_url,
		}

	def extern_link_youtube(self):
		for rec in self:
			pass

	@api.depends('state')
	def _compute_progress(self):
		for rec in self:
			if rec.state == 'new':
				progress = 25
			elif rec.state == 'confirmed':
				progress = 75
			elif rec.state == 'validated':
				progress = 100
			else:
				 progress = 0
			rec.progress = progress

	# client_id = fields.Many2one('res.users', 'Client', required=True, tracking=1, search='_search_client_id')
	# def _search_client_id(self, operator, value):
	# 	return [('reservation_date', '=', fields.Date.today())]











	# Verifier le total et tester
	# @api.constrains('reservation_duration_hours','reservation_duration_day')
	# def _check_date(self):
	# 	if self.reservation_duration_day <= 30 and self.reservation_duration_day <= 24:
	# 		raise ValidationError(f'Vous avez saisi une valeur superieure a 32 jours #{self.reservation_duration_day}')
		# elif self.reservation_duration_hours <= 24:
		# 	raise ValidationError(f'Vous avez saisi une valeur superieure a 24 Heure #{self.reservation_duration_hours}')
	# self.env['ir.config_parameter'].get_param('booking_management.field_parameter')
	# self.env.context.get('active_id')



