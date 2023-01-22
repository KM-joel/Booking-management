from odoo import _, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request as r

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class PortalReservation(CustomerPortal):
    def __init__(self):
        pass

    def _prepare_portal_layout_values(self):
        values = super(PortalReservation, self)._prepare_portal_layout_values()
        # client_id = (
        #     r.env.user.id
        # )  # r.env['res.users'].sudo().search([('id', '=', r.env.user.id)], limit=1)
        reservations_count = r.env["booking.management.reservation"].search_count([])
        values["reservations_count"] = reservations_count
        return values

    def _application_get_page_view_values(self, reservation, access_token, **kwargs):
        values = {
            "page_name": "reservation",
            "reservation": reservation,
        }
        return self._get_page_view_values(
            reservation,
            access_token,
            values,
            "my_reservations_history",
            False,
            **kwargs
        )

    @http.route(
        ["/my/reservation", "/my/reservation/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_reservations(
        self, page=1, date_begin=None, date_end=None, sortby=None
    ):

        values = self._prepare_portal_layout_values()

        reservations = r.env["booking.management.reservation"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("Description"), "order": "reference desc"},
            "state": {"label": _("Status"), "order": "state"},
        }
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]

        # client_id = (
        #     r.env.user.id
        # )  # r.env['res.users'].sudo().search([('id', '=', r.env.user.id)], limit=1)

        domain += []
        reservations_count = reservations.search_count(domain)

        pager = portal_pager(
            url="/my/reservation",
            url_args={"date_begin": date_begin, "date_end": date_end, "sortby": sortby},
            total=reservations_count,
            page=page,
            step=self._items_per_page,
        )

        reservations = reservations.search(
            domain, order=order, limit=self._items_per_page, offset=pager["offset"]
        )
        r.session["my_reservations_history"] = reservations.ids[:100]

        values.update(
            {
                "date": date_begin,
                "reservations": reservations,
                "page_name": "application",
                "pager": pager,
                "default_url": "/my/reservation",
                "searchbar_sortings": searchbar_sortings,
                "sortby": sortby,
            }
        )

        return r.render("booking_management.portal_my_reservations", values)

    @http.route("/reservation/request/", type="http", auth="user", website=True)
    def view_reservation_form_create(self, error=None):
        articles = r.env["product.product"].search([])
        # clients = r.env.uid  # r.env['res.users'].search([('id', '=', r.env.uid)])
        reservations = r.env["booking.management.reservation"].search([])

        values = {
            "articles": articles,
            "reservations": reservations,
            "error": error,
        }
        return r.render("booking_management.reservation_submit", values)

    @http.route("/reservation/create", type="http", auth="user", website=True)
    def create_reservation_records(self, **post):
        try:
            values = {
                "client_id": r.env.uid,
                "article_id": r.env["product.product"]
                .sudo()
                .search([("id", "=", post.get("type_article"))], limit=1)
                .id,
                "reservation_date": post.get("reservation_date"),
                "end_date_reservation": post.get("end_date_reservation"),
                "reservation_duration_hours": post.get("reservation_duration_hours"),
                "reservation_duration_day": post.get("reservation_duration_day"),
                "reservation_duration_month": post.get("reservation_duration_month"),
            }
            r.env["booking.management.reservation"].sudo().create(values)
            return self.portal_my_reservations()
        except Exception as excep:
            return self.view_reservation_form_create(error=excep)

    @http.route(
        [
            "/my/reservation/<int:reservation_id>",
            "/my/reservation/<int:reservation_id>/<access_token>",
        ],
        type="http",
        auth="public",
        website=True,
    )
    def open_view_detail_reservation(
        self, reservation_id=None, access_token=None, **kw
    ):
        try:
            reservation_sudo = self._document_check_access(
                "booking.management.reservation", reservation_id, access_token
            )
        except (AccessError, MissingError):
            return r.redirect("/my")

        values = self._application_get_page_view_values(
            reservation_sudo, access_token, **kw
        )

        products = r.env["product.product"].search([])

        values.update(
            {
                "reservation": reservation_sudo,
                "articles": products,
            }
        )
        return r.render("booking_management.portal_reservation_page", values)

    @http.route("/reservation/update", type="http", auth="user", website=True)
    def update_reservation(self, **post):
        pass


class OwlPlaygroung(http.Controller):
    def __init__(self):
        pass

    @http.route(["/owl/playgroung"], type="http", auth="public")
    def show_playgroung(self):
        return r.render("booking_management.playground")
