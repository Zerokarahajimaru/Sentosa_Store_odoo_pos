/** @odoo-module **/

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PaymentScreen.prototype, {
    async validateOrder(isForceValidate = false) {
        const order = this.pos.get_order();
        if (!order) return super.validateOrder(isForceValidate);
        
        const lines = order.get_orderlines();
        if (lines.length === 0) return super.validateOrder(isForceValidate);

        const productData = lines.map(line => ({
            product_id: line.get_product().id,
            qty: line.get_quantity(),
        }));

        try {
            // Memeriksa stok ke backend Odoo
            const stockCheck = await this.pos.orm.call('pos.order', 'check_stock_availability', [productData, this.pos.config.id]);
            
            if (stockCheck && stockCheck.has_empty_stock) {
                await this.env.services.dialog.add(AlertDialog, {
                    title: "Transaksi Ditolak: Stok Kosong",
                    body: "Produk berikut memiliki stok fisik kurang dari 0: " + stockCheck.error_products.join(', '),
                });
                return false; // Memblokir transaksi
            }
        } catch (error) {
            // Edge case: Internet terputus atau RPC gagal
            // Kita log error dan membiarkan transaksi dilanjutkan jika offline (agar kasir tetap bisa melayani, data sinkron nanti)
            console.warn("RPC Check failed, POS might be offline. Bypassing strict stock validation.", error);
        }

        return super.validateOrder(isForceValidate);
    }
});
