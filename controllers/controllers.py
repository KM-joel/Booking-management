import json
from odoo import http
from odoo.http import request

class Controllers(http.Controller):

	@http.route('/api/reservation/', type="json", auth="public", method=['GET'], csrf=False)
	def get_reservation(self):
		values = {}
		data = request.env['reservation.reservation'].search([])

		if data:
			values['success'] = True
			values['return'] = data
		else:
			values['success'] = False
			values['error_code'] = 1
			values['error_data'] = 'No data found!'

		return json.dumps(values)