from odoo import models, fields, api


class ReservationArticle(models.Model):
    _name = 'reservation.article'
    _description = 'management of article'
    _rec_name = 'name_article'

    name_article = fields.Char(string='Name of article', required=True)
    description_article = fields.Text(string='Description of article')
    reservation_id = fields.Many2many('Resevation')


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
