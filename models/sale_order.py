from odoo import fields, models, api


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	reservation_ids = fields.One2many('booking.management.reservation', 'devis_id', string='Reservation')
	total_reservation = fields.Integer('Total reservation', compute='_compute_total_reservation')
	active_devis = fields.Boolean(default=False)

	@api.depends('reservation_ids')
	def _compute_total_reservation(self):
		for r in self:
			r.total_reservation = len(r.reservation_ids)

	def open_view_reservations(self):
		self.ensure_one()
		return {
			'name': 'Reserve',
			'type': 'ir.actions.act_window',
			'view_mode': 'tree,form',
			'res_model': 'booking.management.reservation',
			'domain': [('id', 'in', self.reservation_ids.ids)]
		}
		# action = self.env['ir.actions.act_window']._for_xml_id('booking_management.reservation_all_action_window')
		# if self.total_reservation > 1:
		# 	action['domain'] = [('id', 'in', self.reservation_ids.ids)]
		# elif self.reservation_ids:
		# 	# action['view_mode'] = [(self.env.ref('booking_management.reservation_tree').id)]
		# 	action['res_id'] = [res.id for res in self.reservation_ids]
		# return action

	confirmed_user_id = fields.Many2one(related='reservation_ids.client_id', string='Confirmed user')

	def action_confirm(self):
		super(SaleOrder, self).action_confirm()
		print('+++++++++++++++++++++++++++++++')
		self.user_id = self.confirmed_user_id

	def _prepare_invoice(self):
		invoices_vals = super(SaleOrder, self)._prepare_invoice()
		invoices_vals['so_confirmed_user_id'] = self.confirmed_user_id.id
		print('------------------------------->', invoices_vals)
		return invoices_vals

	count_client_group = fields.Integer(string='Count in group client', compute='_compute_count_client_group')

	@api.constrains('reservation_ids')
	def _compute_count_client_group(self):
		group_by_client = self.env['booking.management.reservation'].read_group(domain=[], fields=['client_id'], groupby=['client_id'])
		for r in group_by_client:
			print('++++++++++++++++++>', r)
			client_id = r.get('client_id')[0]
			print('++++++++++++++++++>', client_id)
			client_rec = self.browse(client_id)
			print('++++++++++++++++++>', client_rec)
			print('---------', r['client_id_count'])
			client_rec.count_client_group = r['client_id_count']
			self -= client_rec
		self.count_client_group = 0



	# def open_expenses_action(self):
	# 	action = self.env['ir.actions.act_window']._for_xml_id('hr_expense.action_hr_expense_sheet_all_all')
	# 	action['context'] = {
	# 		'search_default_approved': 1,
	# 		'search_default_to_post': 1,
	# 		'search_default_journal_id': self.id,
	# 		'default_journal_id': self.id,
	# 	}
	# 	action['view_mode'] = 'tree,form'
	# 	action['views'] = [(k, v) for k, v in action['views'] if v in ['tree', 'form']]
	# 	return action
	# def action_anim_method(self):
	# 	print('Action in animation when confirmed reservation & effect arc_en_ciel')
	# 	return {
	# 		'effect': {
	# 			'fadeout': 'slow',
	# 			'message': 'Your reservation is validated',
	# 			'type': 'rainbow_man'
	# 		}
	# 	}
	# account = self.env['account.move'].browse([51, 72]).mapped('name')
	# for ac in account:
	# 	print('------->', ac)
	# self.env['account.move'].browse(3).write({'name': 'update_name', 'email': 'joel@gmail.com'})
	# 	self.env['account.move'].browse(99).get_metadata()
	# 	self.env['account.move'].browse(99).get_metadata()[0].get('xmlid')
	# 	self.env['account.move'].fields_get(['name', 'field_label'], ['type', 'string'])




