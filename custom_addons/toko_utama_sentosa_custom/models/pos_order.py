# -*- coding: utf-8 -*-
from odoo import models, api, fields

class PosOrder(models.Model):
    _inherit = 'pos.order'

    delivery_datetime = fields.Datetime(string="Jadwal Pengiriman Khusus")
    is_mobil_pickup = fields.Boolean(string="Kirim via Mobil Pickup Khusus")
    refund_reason = fields.Char(string="Alasan Refund / Retur")

    @api.model
    def _load_pos_data_fields(self, config_id):
        res = super()._load_pos_data_fields(config_id)
        res += ['delivery_datetime', 'is_mobil_pickup', 'refund_reason']
        return res

    @api.model
    def check_stock_availability(self, product_data, config_id):
        """
        Endpoint RPC yang dipanggil oleh frontend PoS sebelum memvalidasi order.
        Mengecek apakah stok produk <= 0 (kosong/minus).
        """
        error_products = []
        pos_config = self.env['pos.config'].browse(config_id)
        location = pos_config.picking_type_id.default_location_src_id

        for line in product_data:
            product = self.env['product.product'].browse(line['product_id'])
            if product.is_storable:
                quant = self.env['stock.quant'].search([
                    ('product_id', '=', product.id),
                    ('location_id', '=', location.id)
                ], limit=1)
                available = quant.quantity if quant else 0.0
                
                if available - line['qty'] < 0:
                    error_products.append(product.display_name)
                    
        return {
            'has_empty_stock': len(error_products) > 0,
            'error_products': error_products
        }

    @api.model
    def _process_order(self, order, existing_order):
        order_data = order
        
        lines = order_data.get('lines', [])
        product_ids = [line[2]['product_id'] for line in lines if line[2] and line[2].get('product_id')]
        
        products = self.env['product.product'].browse(product_ids)
        has_meja = any(p.name and 'Meja' in p.name for p in products)
        has_kursi = any(p.name and 'Kursi' in p.name for p in products)
        
        if has_meja and has_kursi:
            for line in lines:
                line_data = line[2]
                if line_data and 'discount' in line_data:
                    line_data['discount'] = max(line_data['discount'], 10.0)

        res = super(PosOrder, self)._process_order(order, existing_order)
        
        pos_order_id = self.browse(res)
        if pos_order_id:
            if order_data.get('delivery_datetime'):
                pos_order_id.delivery_datetime = order_data.get('delivery_datetime')
            if order_data.get('is_mobil_pickup') is not None:
                pos_order_id.is_mobil_pickup = order_data.get('is_mobil_pickup')
            if order_data.get('refund_reason'):
                pos_order_id.refund_reason = order_data.get('refund_reason')
                
        return res
