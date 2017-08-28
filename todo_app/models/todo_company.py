#-*- coding:utf-8 -*-

from  odoo import api, models, fields


class TodoCompany(models.Model):

    _inherit = 'res.company'

    compile_number = fields.Integer(u'编制最大数量', required=False)
    company_contract = fields.Selection([(u'1', u'已签署'), (u'2', u'已终止')],string = u'派遣协议')

    employee_ids =  fields.One2many('hr.employee', 'company_id', 'Employee ids')
    employee_numbers = fields.Integer(string=u'已有编制数量', compute="_compute_employee_numbers")

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

    # def _compute_employee_numbers(self):
    #
    #     info  = self.env['hr.employee']
    #
    #     count = 0
    #     for i in info:
    #
    #         if i :
    #             count+=1
    #     # res1  = self.env['re']
    #
    #     # info.search(['company_id.id','=',str(self.id)])


        # length = len(info)
        #
        # self.employee_numbers = 0