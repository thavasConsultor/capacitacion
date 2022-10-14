# -*- coding: utf-8 -*-
{
    'name': "curso",

    'summary': """Academy app to manage Training""",

    'description': """
        Academy Module to manage Training:
        - Course
        - Sessions
        - Attendeess
    """,

    'author': "Thavas",
    'website': "http://www.thavasconsultoria.com/odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "security/academy_security.xml",
        "security/ir.model.acces.csv",
        "views/academy_menuitems.xml",
        "views/module_views.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/academy_demo.xml',
    ],
    'license': 'LGPL-3',
}