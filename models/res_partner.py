from odoo import _, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def open_view_send_message(self):
        return {
            "type": "ir.actions.act_window",
            "name": _("Whatsapp Message"),
            "res_model": "whatsapp.send.message",
            "target": "new",
            "view_mode": "form",
            "context": {"default_user_id": self.id},
        }
