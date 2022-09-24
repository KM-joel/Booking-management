from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    reservation_ids = fields.One2many(
        "booking.management.reservation", "client_id", string="Reservation"
    )
