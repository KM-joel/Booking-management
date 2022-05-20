from odoo import http, _
from odoo.http import request as r

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
import werkzeug

class PortalReservation(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(PortalReservation, self)._prepare_portal_layout_values()
        client_id = r.env['res.users'].sudo().search([('id', '=', r.env.user.id)], limit=1)
        reservations_count = r.env['booking.management.reservation'].search_count([])
        values['reservations_count'] = reservations_count
        return values

    def _application_get_page_view_values(self, application, access_token, **kwargs):
        values = {
            'page_name': 'application',
            'application': application,
        }
        return self._get_page_view_values(application, access_token, values, 'my_applications_history', False, **kwargs)


    @http.route(['/my/reservation/', '/my/reservation/page/<int:page>'], type='http', auth='user', website=True)
    def portal_my_reservations(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = self._prepare_portal_layout_values()

        reservations = r.env['booking.management.reservation']
        domain = []

        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Description'), 'order': 'name desc'},
            'state': {'label': _('Status'), 'order': 'state'},
        }
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        client_id = r.env['res.users'].sudo().search([('id', '=', r.env.user.id)], limit=1)

        domain += []
        reservations_count = reservations.search_count(domain)

        pager = portal_pager(
            url = '/my/reservation/',
            url_args = {'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total = reservations_count,
            page = page,
            step = self._items_per_page
        )

        reservations = reservations.search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        r.session['my_applications_history'] = reservations.ids[:100]

        values.update({
            'date': date_begin,
            'reservations': reservations,
            'page_name': 'application',
            'pager': pager,
            'default_url': '/my/reservation/',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })

        return r.render('booking_management.portal_my_reservations', values)

