# -*- coding: utf-8 -*-

{
    'name' : 'Procurement paid',
    'version' : '1.0',
    'summary': 'Only create procurements after Sale Order as been paid.',
    'description': """Sale Orders generate procurements only after been fully paid.
    Adds the button "Create Procurement" in Sale Order to bypass the module functionality, in case the account manager 
    wants to create a procurement even if the sale order invoices are not fully paid.
    After disabling this module procurements are generated automatically for sale orders that don't have any.
    """,
    'category': 'Sales',
    'depends' : ['sale_stock', 'base_setup'],
    'data': ['views/sale_order_view.xml', 'views/res_config_settings_views.xml'],
    'installable': True,
    'application': False,
}
