from odoo import fields, models, api

class ResUsers(models.Model):
	_inherit = 'res.users'

	reservation_ids = fields.One2many('reservation.reservation', 'client_id', string='Reservation')