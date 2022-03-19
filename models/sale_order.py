from odoo import fields, models, api


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	reservation_ids = fields.One2many('reservation.reservation', 'devis_id', string='Reservation')
	total_reservation = fields.Integer('Total reservation', compute='_compute_total_reservation')

	def _compute_total_reservation(self):
		for r in self:
			r.total_reservation = len(r.reservation_ids)

	def open_view_reservations(self):
		action = self.env['ir.actions.act_window']._for_xml_id('reservation.reservation_all_action_window')
		if self.total_reservation > 1:
			action['domain'] = [('id', 'in', self.reservation_ids.ids)]
		elif self.reservation_ids:
			tree_view = [(self.env.ref('reservation.reservation_tree').id, 'tree')]
			action['view_mode'] = tree_view
			action['res_id'] = self.reservation_ids.id
		return action



