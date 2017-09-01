#-*- coding:utf-8 -*-

{
     'name': 'To-Do Employee',
     'description': 'Todo Employee Extension',
     'author': 'John',
     'version': '0.1',
     'depends': ['hr','resource','base','hr_holidays','hr_contract'],

     'data': [
          'views/employee_views.xml',
          'security/employee_user_security.xml',
          'security/employee_rule_security.xml',
          'security/ir.model.access.csv',
     ],
     'application': True,
     'installable': True,
     'auto_install': False,
}
#
