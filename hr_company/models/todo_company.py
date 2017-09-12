#-*- coding:utf-8 -*-

from  odoo import api, models, fields


class TodoCompany(models.Model):

    _inherit = 'res.company'

    compile_number = fields.Integer(u'编制最大数量', required=False)
    company_contract = fields.Selection([(u'1', u'已签署'), (u'2', u'已终止')],string = u'派遣协议')
    employee_ids =  fields.One2many('hr.employee', 'company_id', 'Employee ids')
    employee_numbers = fields.Integer(string=u'已有编制数量', compute="_compute_employee_numbers")
    '''
    Company contact info
    
    '''
    leader_name = fields.Char(u'分区领导姓名',required=False)
    leader_tel = fields.Char(u'分区领导手机', required=False)
    leader_work_tel = fields.Char(u'分区领导工作电话', required=False)


    leader_name_1= fields.Char(u'分区领导1姓名',required=False)
    leader_tel_1 = fields.Char(u'分区领导1手机', required=False)
    leader_work_tel_1 = fields.Char(u'分区领导1工作电话', required=False)


    @api.depends('employee_ids')
    def _compute_employee_numbers(self):

        for r in self:
            # self.employee_numbers = len(r.employee_ids)
            self.employee_numbers = 0
            for i in r.employee_ids:
                if i.active == True:
                    self.employee_numbers += 1

            if self.employee_numbers == 0:
                self.sudo().write({'company_contract': u'2'})

