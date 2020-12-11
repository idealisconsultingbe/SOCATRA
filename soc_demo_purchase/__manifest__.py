{
    'name': 'Socatra : Purchase Requisition',
    'summary': 'Demo Socatra : Purchase Requisition Adaptation',
    'version': '1.0',
    'category': 'Inventory/Purchase',
    'author': 'Idealis Consulting',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'purchase',
        'purchase_enterprise',
        'purchase_requisition',
    ],
    'data': [
        'views/soc_purchase_requisition_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
