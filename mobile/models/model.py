# --*-- coding:utf-8 --*--
from odoo import fields,models

class Mobile(models.Model):
    _name = 'mobile.data'
    _rec_name ='tendienthoai'
    tendienthoai = fields.Char(string='Tên điện thoại',required = True,translate=True,help='blabla')
    hang_sx = fields.Char(string='Hãng sản xuất',required = True,translate=True)
    ngay_sx = fields.Date('Ngày sản xuất',required = True,translate=True)
    chieu_dai = fields.Float('Chiều dài',translate=True)
    chieu_rong = fields.Float('Chiều rộng',translate=True)
    do_day = fields.Float('Độ dầy',translate=True)
    kich_thuoc = fields.Char('Kích thước',translate=True)
    do_phan_giai = fields.Char('Độ phân giải',translate=True)
    he_dieu_hanh = fields.Char('Hệ điều hành',translate=True)
    cpu = fields.Char('Thông số CPU',translate=True)
    ram = fields.Char('Thông số Ram',translate=True)
    gia_ban = fields.Integer('Giá bán',translate=True)


class AModel(models.Model):

    _name = 'a_name'

    name = fields.Char(
        string="Name",                   # Optional label of the field
        compute="_compute_name_custom",  # Transform the fields in computed fields
        store=True,                      # If computed it will store the result
        select=True,                     # Force index on field
        readonly=True,                   # Field will be readonly in views
        inverse="_write_name"            # On update trigger
        required=True,                   # Mandatory field
        translate=True,                  # Translation enable
        help='blabla',                   # Help tooltip text
        company_dependent=True,          # Transform columns to ir.property
        search='_search_function'        # Custom search function mainly used with compute
    )

   # The string key is not mandatory
   # by default it wil use the property name Capitalized

   name = fields.Char()  #  Valid definition