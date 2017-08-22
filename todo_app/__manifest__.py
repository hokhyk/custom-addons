#-*- coding:utf-8 -*-

{
     'name': 'To-Do Task',
     'description': 'Employee & Company Extension',
     'author': 'John',
     'depends': ['hr','resource','base'],

     'data': [
          'views/employee_views.xml',
          'views/company_views.xml',
     ],
     'application': True,
     'installable': True,
     'auto_install': False,
}