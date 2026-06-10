# -*- coding: utf-8 -*-

{
    'name': 'Toko Utama Sentosa Custom',
    'version': '1.0',
    'category': 'Customizations',
    'summary': 'Custom UI/UX, PoS modifications, and Inventory features for Toko Utama Sentosa',
    'description': """
        This module contains all custom features for Toko Utama Sentosa including:
        - UI/UX Styling for PoS
        - Special packaging notifications
        - Refund reasons
        - Delivery & Pickup scheduling
        - Out of stock blocking
        - Product dimensions & material fields
        - Unbundling features
        - Auto-bundling discount
    """,
    'author': 'Your Name',
    'depends': ['base', 'point_of_sale', 'stock', 'product', 'web', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/stock_picking_views.xml',
        'views/pos_order_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'toko_utama_sentosa_custom/static/src/scss/pos_ui.scss',
            'toko_utama_sentosa_custom/static/src/js/pos_notifications.js',
            'toko_utama_sentosa_custom/static/src/js/pos_refund_reason.js',
            'toko_utama_sentosa_custom/static/src/js/pos_stock_validation.js',
            'toko_utama_sentosa_custom/static/src/xml/pos_refund_reason.xml',
            'toko_utama_sentosa_custom/static/src/xml/pos_delivery_schedule.xml',
        ],
        'web.assets_backend': [
            'toko_utama_sentosa_custom/static/src/scss/backend_dashboard.scss',
            'toko_utama_sentosa_custom/static/src/scss/pos_login.scss',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
