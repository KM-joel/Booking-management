from odoo import models, fields, api


class ReservationArticle(models.Model):

    _inherit = 'product.product'

    reservation_id = fields.Many2one('reservation.reservation', 'Resevation')


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
