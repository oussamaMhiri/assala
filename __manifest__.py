# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Reports',
    'category': '',
    'description': """
             
    """,
    'website': '',
    'depends': ['web',
        'base','sale_management'
    ],
    'data': [
        'report/external_layout.xml',
        'report/sale_report_inherit.xml',

    ],
    'demo': [
       
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}





