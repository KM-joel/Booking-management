import requests

from odoo import _, fields, models
from odoo.exceptions import ValidationError


class WhatsappSendMessage(models.TransientModel):
    _name = "whatsapp.send.message"
    _description = "whatsapp.send.message"

    user_id = fields.Many2one("res.partner", string="Recepient")
    mobile = fields.Char(related="user_id.mobile", required=1)
    content_send = fields.Text(string="Message", required=1)

    def send_message(self):
        if self.content_send and self.mobile:
            token = self.env.user.company_id.token_whatsapp
            if not token:
                raise ValidationError(_("Put the token in the company"))
            else:
                params = {"phone": self.mobile, "body": self.content_send}
                requests.post(token, params=params)
