# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Tax reductions",
    'version': "1.5.0.0",
    'author': "AIR-sc",
    'summary': 'Allows to add tax reductions to sale orders and invoices',
    'description': 'Allows to add tax reductions to sale orders and invoices (italian lows such as Ecobonus and Sismabonus)',
    'license': 'OPL-1',
    'category': "Extra Tools",
    'data': [
             'views/sale_view_order_custom_form.xml',
             'views/account_move_custom_form.xml',
             'views/menu.xml',

             'security/ir.model.access.csv'
             ],
    'website': 'https://www.air-srl.com',
    'depends': ['sale','account','l10n_it_fatturapa'],
    'installable': True,
    'auto_install': False,
	"images": ['static/description/icon.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
