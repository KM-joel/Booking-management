from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    so_confirmed_user_id = fields.Many2one("res.users", string="So confirmed user")
