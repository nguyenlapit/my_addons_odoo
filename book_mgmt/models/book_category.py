# -*- coding:utf-8 -*-

from odoo import models,fields,api
from datetime import datetime

class BookCategory(models.Model):
    _name = 'book.category'
    _rec_name = 'name_category'

    code = fields.Char('Mã loại Sách')
    name_category = fields.Char('Loại Sách')