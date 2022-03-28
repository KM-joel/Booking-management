# -*- coding: utf-8 -*-
{
    'name': "gestion des reservations",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product'],
    'application': True,

    # always loaded
    'data': [
        'security/reservation_groups.xml',
        'security/reservation_security.xml',
        'security/ir.model.access.csv',
        'views/reservation_reservation_views.xml',
        'views/menus/reservation_menus.xml',
        'views/reservation_article_views.xml',
        'views/menus/article_menus.xml',
        'views/sale_order_views.xml',
        'views/menus/sale_order_menus.xml',
        'data/reservation_reference_sequence.xml',
        'data/reservation_many_quotation.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
