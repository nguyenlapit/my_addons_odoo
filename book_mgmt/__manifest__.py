# -*- coding: utf-8 -*-
{
    'name': "Book Mgmt",

    'summary': """Quản lý thư viện""",

    'description': """
        Quản lý thư viện ITPLUS
    """,

    'author': "Mr. Right",
    'website': "http://www.mright.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/book_category_view.xml',
        'views/books_view.xml',
        'views/tickets_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
