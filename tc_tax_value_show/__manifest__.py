# -*- coding: utf-8 -*-

{
    'name': 'Show Taxes value',
    'version': '2018.07.22.02.57',
    'author' : 'Terra Colligo',
    'category': 'Extra',
    'summary':  '',
    'depends': ['account',],
    'description': """
        Show tax value in invoice line.
    """,
    'data': [
            "views/invoice_view.xml",
            "views/report_invoice.xml",
     ],
    'installable': True,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
