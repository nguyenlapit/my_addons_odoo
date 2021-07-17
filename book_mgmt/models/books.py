# -*- coding:utf-8 -*-

from odoo import models,fields,api
from datetime import datetime

class Books(models.Model):
    _name = 'books'
    _rec_name = 'name_book'

    name_book = fields.Char('Tên Sách')
    author = fields.Char('Tác Giả')
    number_page = fields.Integer('Số Trang')
    category = fields.Many2one('book.category','Thể loại')
    num_in = fields.Integer('Số lượng nhập')
    num_remain = fields.Integer('Số lượng còn lại')
    emp_borrow = fields.Many2one('tickets','Nhân viên mượn')