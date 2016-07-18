# -*- coding: utf-8 -*-
{
    'name': "mod_electrolab",

    'summary': """
        Modification toward running Odoo @ Electrolab
    """,

    'description': """
        This module compiles the modifications mades on the Electrolab's
        Odoo instance to add the necessary fields and modify views and models.
    """,

    'author': "Electrolab",
    'website': "http://www.electrolab.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Other Extra Rights',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'partner_firstname', 'auth_ldap'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
