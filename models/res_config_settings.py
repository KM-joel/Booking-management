from odoo import fields, models, api


class ResCompany(models.Model):
   _inherit = 'res.company'

   product_id = fields.Many2one('product.product', string='Product')


class ResConfigSettings(models.TransientModel):
   _inherit = 'res.config.settings'


   booking_product_id = fields.Many2one(related='company_id.product_id', string='Product conf', store=1,readonly=0)


