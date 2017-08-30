#-*- coding:utf-8 -*-

from  odoo import api, models, fields


class TodoContrat(models.Model):

    _inherit = "hr.contract"

    state = fields.Selection([
        ('draft', u'新建'),
        ('open', u'进行中'),
        ('pending', u'待续约'),
        ('close', u'过期'),
        ('Cancelled', u'已终止')
    ], string='Status', track_visibility='onchange', help='Status of the contract', default='draft')