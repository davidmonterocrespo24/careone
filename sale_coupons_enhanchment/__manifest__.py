{
    'name': 'Sales Coupons Module',
    'version': '13.0.1.0.0',
    'author': 'White-code (Omnya Rashwan)',
    'category': 'Sale',
    'depends': [
        'sale', 'fleet', 'partner_fleet_sale_enhancement', 'sale_coupon'
    ],
    'data': [
        'views/sale_coupons_view.xml',
        'wizard/sale_coupon_apply_code_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
