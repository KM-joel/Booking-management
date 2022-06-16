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



