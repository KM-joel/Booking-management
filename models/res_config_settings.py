from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    booking_product_id = fields.Many2one(related='company_id.product_id', string='Product conf', store=1, readonly=0)
