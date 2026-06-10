/** @odoo-module **/

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";

patch(PaymentScreen.prototype, {
    async validateOrder(isForceValidate = false) {
        const order = this.pos.get_order();
        if (order) {
            const deliveryDate = document.getElementById('custom_delivery_date')?.value;
            const isPickup = document.getElementById('custom_is_pickup')?.checked;
            
            if (deliveryDate) {
                order.delivery_datetime = deliveryDate;
            }
            if (isPickup !== undefined) {
                order.is_mobil_pickup = isPickup;
            }
        }
        return super.validateOrder(isForceValidate);
    }
});
