#-*- coding:utf-8 -*-

from  odoo import api, models, fields

class TodoEmployee(models.Model):

    _inherit = 'hr.employee'

    member_no = fields.Char(u'派遣员工 编号', required=False)
    school = fields.Char(u'毕业院校', requeired = False)
    education = fields.Selection([(u'1',u'本科'),(u'2',u'硕士'),(u'3',u'博士')],string= u'教育程度')
    bank = fields.Char(u'工资卡 开户行', required = False)
    age = fields.Integer(u'年龄', required=False)
    political_status = fields.Selection([(u'1',u'群众'),(u'2',u'团员'),(u'3',u'党员')], string=u'政治面貌')
    census = fields.Selection([(u'1', u'农村'), (u'2', u'城市')],string = u'户籍性质')
    emergency_name = fields.Char(u'紧急联系人', required=False)
    emergency_tel = fields.Char(u'紧急联系电话', required=False)
    qq = fields.Char(u'QQ', required=False)
    wechat = fields.Char(u'微信', required=False)

    # add employees to company

    company_id = fields.Many2one('res.company', string='公司')

    # add attachments

    trial_attachments = fields.Many2many('ir.attachment', 'trail_ir_attachments_rel',
        'trail_id', 'attachment_id', u'试用期证明')

    entry_attachments = fields.Many2many('ir.attachment', 'entry_ir_attachments_rel', 'entry_id', 'attachment_id',
                                         u'入职证明')

    quit_attachments = fields.Many2many('ir.attachment', 'quit_ir_attachments_rel', 'quit_id', 'attachment_id',
                                         u'离职证明')

    income_attachments = fields.Many2many('ir.attachment', 'income_ir_attachments_rel', 'income_id', 'attachment_id',
                                          u'收入证明')

    # modify the origin attributes

    # birthday = fields.Date('Date of Birth', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # ssnid = fields.Char('SSN No', help='Social Security Number', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # sinid = fields.Char('SIN No', help='Social Insurance Number', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # identification_id = fields.Char(string='Identification No', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # marital = fields.Selection([('single', 'Single'), ('married', 'Married'), ('widower', 'Widower'), ('divorced', 'Divorced')],
    #     string='Marital Status', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    #
    # bank_account_id = fields.Many2one('res.partner.bank', string='Bank Account Number',
    #                                   domain="[('partner_id', '=', address_home_id)]",
    #                                   help='Employee bank salary account', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # passport_id = fields.Char('Passport No', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    #
    # # modify the contracts origin attributes
    #
    # medic_exam = fields.Date(string='Medical Examination Date', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # place_of_birth = fields.Char('Place of Birth', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # children = fields.Integer(string='Number of Children', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # vehicle = fields.Char(string='Company Vehicle', groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    # vehicle_distance = fields.Integer(string='Home-Work Dist.', help="In kilometers", groups='hr.group_hr_manager,todo_company_user,todo_send_company_user')
    #
    #
    # set Leaves Left button invisible

    show_leaves = fields.Boolean('Able to see Remaining Leaves', compute='_compute_show_leaves')
    # groups_id = "[(6, 0, [ref('hr.group_hr_manager'),ref('todo_send_company_user'),ref('todo_company_user')])]"

    # add employee work years

    ever_work_years = fields.Float(string=u'以前工作年限',digits=(4,2))

    leave_status = fields.Boolean(u'离职状态', default=True)


    @api.multi
    def _compute_show_leaves(self):
        for employee in self:
            employee.show_leaves = False


    @api.multi
    def toggle_leaves(self):
        for record in self:
            record.leave_status = not record.leave_status
        return True


    @api.multi
    def toggle_active_new(self):
        for record in self:
            record.active = not record.active
            record.leave_status = True
        return True