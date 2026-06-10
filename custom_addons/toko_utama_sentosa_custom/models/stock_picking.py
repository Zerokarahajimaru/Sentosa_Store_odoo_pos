# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    delivery_datetime = fields.Datetime(string="Jadwal Pengiriman Khusus", related='pos_order_id.delivery_datetime', store=True)
    is_mobil_pickup = fields.Boolean(string="Kirim via Mobil Pickup", related='pos_order_id.is_mobil_pickup', store=True)
