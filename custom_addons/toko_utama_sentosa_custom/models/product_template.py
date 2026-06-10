# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_dimension = fields.Char(string="Dimensi Barang (P x L x T)")
    custom_material = fields.Char(string="Material")
    
    is_bundle = fields.Boolean(string="Apakah ini Barang Paket?")
    bundle_item_id = fields.Many2one('product.product', string="Item Satuan Hasil Pecahan")
    bundle_qty = fields.Integer(string="Jumlah Satuan per Paket", default=1)

    @api.model
    def _load_pos_data_fields(self, config_id):
        res = super()._load_pos_data_fields(config_id)
        res += ['custom_dimension', 'custom_material']
        return res

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_unbundle_product(self):
        self.ensure_one()
        if not self.is_bundle or not self.bundle_item_id or self.bundle_qty <= 0:
            raise UserError("Konfigurasi paket tidak valid. Pastikan produk ditandai sebagai Barang Paket dan Item Satuan terisi.")
        
        # Cari stok di lokasi internal
        quants = self.env['stock.quant'].search([
            ('product_id', '=', self.id), 
            ('location_id.usage', '=', 'internal')
        ])
        
        total_qty = sum(quants.mapped('quantity'))
        if total_qty < 1:
            raise UserError("Stok fisik barang paket tidak cukup (kurang dari 1) untuk dipecah.")
            
        location = quants[0].location_id
        
        # Kurangi stok paket sebesar 1
        self.env['stock.quant']._update_available_quantity(self, location, -1)
        # Tambah stok satuan
        self.env['stock.quant']._update_available_quantity(self.bundle_item_id, location, self.bundle_qty)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Pecah Paket Berhasil',
                'message': f'Berhasil memecah 1 paket {self.name} menjadi {self.bundle_qty} {self.bundle_item_id.name}.',
                'type': 'success',
                'sticky': False,
            }
        }
