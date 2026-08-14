{
    'name': 'Custom Delivery Note QWeb Report',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Delivery',
    'summary': 'Custom professional PDF delivery note report for Odoo Stock/Delivery',
    'author': 'Mochammad Doni Febrian',
    'depends': ['stock'],
    'data': [
        'reports/delivery_report_action.xml',
        'reports/delivery_report_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}