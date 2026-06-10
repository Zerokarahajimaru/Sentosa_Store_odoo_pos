/** @odoo-module **/

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PaymentScreen.prototype, {
    async validateOrder(isForceValidate = false) {
        const order = this.pos.getOrder();
        if (!order) {
            return super.validateOrder(isForceValidate);
        }

        // 1. Capture Delivery Data (From UI)
        const deliveryDate = document.getElementById('custom_delivery_date')?.value;
        const isPickup = document.getElementById('custom_is_pickup')?.checked;
        
        if (deliveryDate) {
            order.delivery_datetime = deliveryDate;
        }
        if (isPickup !== undefined) {
            order.is_mobil_pickup = isPickup;
        }

        // 2. Perform Stock Validation
        const lines = order.lines;
        if (lines.length > 0) {
            const productData = lines.map(line => ({
                product_id: line.product_id.id,
                qty: line.qty,
            }));

            try {
                // Memeriksa stok ke backend Odoo menggunakan data.orm.call
                const stockCheck = await this.pos.data.orm.call('pos.order', 'check_stock_availability', [productData, this.pos.config.id]);
                
                if (stockCheck && stockCheck.has_empty_stock) {
                    await this.env.services.dialog.add(AlertDialog, {
                        title: "Transaksi Ditolak: Stok Kosong",
                        body: "Produk berikut memiliki stok fisik kurang dari 0: " + stockCheck.error_products.join(', '),
                        confirmClass: "btn-terracotta",
                        contentClass: "custom-warning-dialog",
                    });
                    return false; // Stop validation flow
                }
            } catch (error) {
                console.warn("RPC Check failed, POS might be offline. Bypassing strict stock validation.", error);
            }
        }

        // 3. Continue with core validation
        return super.validateOrder(isForceValidate);
    }
});
