# -*- coding: utf-8 -*-
{
    'name': 'Facture Tunisie',
    'version': '13.0',
    'author': "Oussama MHIRI",
    'summary': """
    Tunisia Invoice """,
    'website': "",
    'description': """
        Tunisia Invoice 
    """,
    'images': [''],
    'category': 'Accounting',
    'depends': ['base_setup', 'account', 'web'],
    'data': [
        'views/account_move_view.xml',
        'views/report_invoice.xml',
        'views/report_templates.xml',
    ]
}
