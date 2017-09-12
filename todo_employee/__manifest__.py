#-*- coding:utf-8 -*-

{
    'name': 'To-Do Employee',
    'description': 'Todo Employee Extension  & User Extension',
    'author': 'John',
    'version': '0.1',
    'depends': ['hr','resource','base','hr_holidays','hr_contract','base_setup'],

    'data': [
        'views/assets.xml',
        'security/employee_user_security.xml',
        'security/employee_rule_security.xml',
        'views/employee_views.xml',
        'security/ir.model.access.csv',
    ],
    'qweb':['static/src/xml/*.xml'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'bootstrap': True,
}
