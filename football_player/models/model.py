from odoo import fields,models,api,exceptions

POSITIONS = [('0', 'Thủ môn'), ('1', 'Hậu vệ'),('2', 'Trung vệ'),('3', 'Tiền đạo'),('4', 'Hậu vệ trái'),('5', 'Hậu vệ phải'),('6', 'Trung vệ trái'),('7', 'Trung vệ phải')]

class Football_Player(models.Model):
    _name = 'football.player'

    name = fields.Char(string='Tên cầu thủ',required = True)
    avatar = fields.Binary(string='Hình ảnh', attachment=True)
    birthday = fields.Date('Ngày sinh',required = True)
    height = fields.Float('Chiều cao')
    weight = fields.Integer('Cân nặng')
    name_club = fields.Many2one(comodel_name='football.club',string='Tên câu lạc bộ')
    num_club = fields.Integer('Số áo tại câu lạc bộ')
    position = fields.Selection(string="Vị trí sở trường", selection=POSITIONS, default=POSITIONS[0][0], required=True)
    county_team = fields.Many2one(comodel_name='res.country', string='Quốc gia')
    num_county = fields.Integer('Số áo đội quốc gia')
    manager_lv1 = fields.Many2one(comodel_name="football.manager", string="HLV trưởng", required=False, )
    manager_lv2 = fields.Many2many(comodel_name="football.manager", string="Trợ lý", )
    salary = fields.Integer(string='Lương theo tuần')
    salary_year = fields.Integer(string='Lương theo năm', compute = 'func_salary')

    @api.one
    @api.depends('salary')
    def func_salary(self):
        if self.salary != 0:
            print(self.salary)
            self.salary_year = self.salary * 52
            print(self.salary)

    @api.multi
    @api.constrains('manager_lv2','salary')
    def check_manager(self):
        if self.manager_lv1 is not None:
            if self.manager_lv1 in self.manager_lv2:
                print('HLV:', self.manager_lv1)
                print('Trợ lý:', self.manager_lv2)
                raise exceptions.ValidationError("Huấn luyện viên chính không được chọn là trợ lý")
            if self.salary == 0:
                raise exceptions.ValidationError('Lương phải lớn hơn 0!')


class Football_Club(models.Model):
    _name = 'football.club'
    _rec_name = 'nameclub'

    nameclub = fields.Char(size=100,string='Tên câu lạc bộ')
    logoclub = fields.Binary(string='Logo', attachment = True)
    found_year = fields.Date(string='Ngày thành lập', requited = True)
    cup = fields.Many2one(comodel_name='football.cup', string='Giải đấu')
    county = fields.Many2one(comodel_name = 'res.country',string='Quốc gia')

class Football_Cup(models.Model):
    _name = 'football.cup'
    _rec_name = 'name_cup'
    name_cup = fields.Char(size=100,string='Giải đấu')
    cup_note = fields.Html(string='Ghi chú')

class Football_Manager(models.Model):
    _name = 'football.manager'
    _rec_name = 'name_manager'

    name_manager = fields.Char(string='Tên huấn luyện viên',requited=True)
    age = fields.Integer(string='Tuổi')
    county = fields.Many2one(comodel_name='res.country', string='Quốc gia')
