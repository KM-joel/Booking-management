# -*- coding: utf-8 -*-

import requests
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class WhatsappSendMessage(models.TransientModel):
    _name = 'whatsapp.send.message'
    _description = 'whatsapp.send.message'

    user_id = fields.Many2one('res.partner', string='Recepient')
    mobile = fields.Char(related='user_id.mobile', required=1)
    message = fields.Text(string='Message', required=1)

    def send_message(self):
        if self.message and self.mobile:
            token = self.env.user.company_id.token_whatsapp
            if not token:
                raise ValidationError(_('Put the token in the company'))
            else:
                params = {
                    'phone': self.mobile,
                    'body': self.message
                }
                response = requests.post(token, params=params)
                print('----------->', response)
