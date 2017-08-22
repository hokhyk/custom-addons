#-*- coding:utf-8 -*-

from  odoo import api, models, fields

class TodoEmployee(models.Model):

    _inherit = 'hr.employee'

    member_no = fields.Char(u'派遣员工 编号', required=False)
    school = fields.Char(u'毕业院校', requeired = False)
    education = fields.Selection([(u'1',u'本科'),(u'2',u'硕士'),(u'3',u'博士')],string= u'教育程度', groups='hr.group_hr_user')
    bank = fields.Char(u'工资卡 开户行', required = False)
    age = fields.Integer(u'年龄', required=False)
    political_status = fields.Selection([(u'1',u'群众'),(u'2',u'团员'),(u'3',u'党员')], string=u'政治面貌', groups='hr.group_hr_user')
    census = fields.Selection([(u'1', u'农村'), (u'2', u'城市')],string = u'户籍性质', groups='hr.group_hr_user')

    emergency_name = fields.Char(u'紧急联系人', required=False)
    emergency_tel = fields.Char(u'紧急联系电话', required=False)
    # emergency_contact = fields.Char(u'紧急联系wechat/QQ', required=False)
    qq = fields.Char(u'QQ', required=False)
    wechat = fields.Char(u'微信', required=False)
    remark = fields.Text(u'备注')


