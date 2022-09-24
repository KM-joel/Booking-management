{
    "name": "BOOKING",
    "summary": """
        management of reservation""",
    "description": """
        management of reservation""",
    "author": "k.joel, Odoo Community Association (OCA)",
    "website": "https://karizma-conseil.com/",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    # "version": "1.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale", "hr", "hr_recruitment", "web", "contacts"],
    "application": True,
    # always loaded
    "data": [
        "security/reservation_groups.xml",
        "security/reservation_security.xml",
        "security/ir.model.access.csv",
        "views/reservation_reservation_views.xml",
        "views/reservation_article_views.xml",
        "views/sale_order_views.xml",
        "data/reservation_reference_sequence.xml",
        "data/reservation_many_quotation.xml",
        "views/account_move_views.xml",
        "views/templates.xml",
        "views/res_company_views.xml",
        "wizard/whatsapp_send_message_views.xml",
        "views/res_partner_views.xml",
        "views/res_config_settings.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "/booking_management/static/src/css/style.scss",
        ],
        "web.assets_backend": [
            "/booking_management/static/src/js/popup_form.js",
        ],
    },
}
