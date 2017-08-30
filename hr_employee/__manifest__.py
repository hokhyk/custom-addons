#-*- coding:utf-8 -*-

{
     'name': 'To-Do Employee',
     'description': 'Employee Extension',
     'author': 'John',
     'version': '0.1',
     'depends': ['hr','resource','base'],

     'data': [
          'views/employee_views.xml',
          'security/employee_security.xml',
     ],
     'application': True,
     'installable': True,
     'auto_install': False,
}