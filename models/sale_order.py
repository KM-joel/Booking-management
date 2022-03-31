from odoo import fields, models, api


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	reservation_ids = fields.One2many('reservation.reservation', 'devis_id', string='Reservation')
	total_reservation = fields.Integer('Total reservation', compute='_compute_total_reservation')
	active_devis = fields.Boolean(default=False)

	def _compute_total_reservation(self):
		for r in self:
			r.total_reservation = len(r.reservation_ids)

	def open_view_reservations(self):
		action = self.env['ir.actions.act_window']._for_xml_id('reservation.reservation_all_action_window')
		if self.total_reservation > 1:
			action['view_mode'] = 'tree,form'
			action['res_id'] = self.reservation_ids.id
			action['views'] = []
		else:
			action['domain'] = [('id', 'in', self.reservation_ids.ids)]
		return action


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



