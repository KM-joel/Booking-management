from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
   _inherit = 'res.config.settings'


   product_id = fields.Many2one('product.product', string='Product conf', store=1, readonly=0)
