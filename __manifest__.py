{
    "name": "BOOKING",
    "summary": """
        management of reservation""",
    "author": "k.joel, Odoo Community Association (OCA)",
    "website": "https://karizma-conseil.com/",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # for the full list
    "category": "Uncategorized",
    "version": "16.0.1.0.0",
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
        "views/product_category_views.xml",
        "views/templates_owl.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "/booking_management/static/src/css/style.scss",
        ],
        "web.assets_backend": [
            # "/booking_management/static/src/components/list_item/owl_view.js",
            "/booking_management/static/src/js/popup_form.js",
            "/booking_management/static/src/js/code_field.js",
            "/booking_management/static/src/components/list_item/list_item.scss",
            "/booking_management/static/src/components/list_item/list_item.js",
            "/booking_management/static/src/components/list_item/list_item.xml",
            # "/booking_management/static/src/list_view/owl_tree_arch_parser.js",
            "/booking_management/static/src/js/list_view/list_model.js",
            "/booking_management/static/src/js/list_view/list_controller.js",
            "/booking_management/static/src/js/list_view/list_controller.xml",
            # "/booking_management/static/src/js/list_view/list_view.scss",
            "/booking_management/static/src/js/list_view/list_renderer.js",
            "/booking_management/static/src/js/list_view/list_renderer.xml",
            "/booking_management/static/src/js/list_view/list_view.js",
        ],
        "booking_management.assets_playground": [
            # bootstrap
            ("include", "web._assets_helpers"),
            "web/static/src/scss/pre_variables.scss",
            "web/static/lib/bootstrap/scss/_variables.scss",
            ("include", "web._assets_bootstrap"),
            "web/static/src/libs/fontawesome/css/font-awesome.css",  # required for fa icons
            "web/static/src/legacy/js/promise_extension.js",  # required by boot.js
            "web/static/src/boot.js",  # odoo module system
            "web/static/src/env.js",  # required for services
            "web/static/src/session.js",  # expose session_info containing server information
            "web/static/lib/owl/owl.js",  # owl library
            "web/static/lib/owl/odoo_module.js",  # to be able to import "@odoo/owl"
            "web/static/src/core/utils/functions.js",
            "web/static/src/core/browser/browser.js",
            "web/static/src/core/registry.js",
            "web/static/src/core/assets.js",
            "booking_management/static/src/**/*",
        ],
    },
}
