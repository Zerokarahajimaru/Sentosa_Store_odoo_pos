/** @odoo-module **/

import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { patch } from "@web/core/utils/patch";
import { Component, useState } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";

export class RefundReasonPopup extends Component {
    static template = "toko_utama_sentosa_custom.RefundReasonPopup";
    static components = { Dialog };
    setup() {
        this.state = useState({ reason: "Barang Cacat Pabrik" });
    }
    confirm() {
        if (this.props.onConfirm) {
            this.props.onConfirm(this.state.reason);
        }
        this.props.close();
    }
    cancel() {
        this.props.close();
    }
}

patch(TicketScreen.prototype, {
    async onDoRefund() {
        let confirmed = false;
        let selectedReason = "";
        
        await new Promise((resolve) => {
            this.env.services.dialog.add(RefundReasonPopup, {
                onConfirm: (reason) => {
                    confirmed = true;
                    selectedReason = reason;
                    resolve();
                },
                onClose: () => {
                    resolve();
                }
            });
        });

        if (!confirmed) {
            return false; // cancel refund
        }

        const result = await super.onDoRefund();
        const order = this.pos.getOrder();
        if (order && order.isRefund) { // Adjust if needed to ensure we mark the refund reason
            order.refund_reason = selectedReason;
        }
        return result;
    }
});
