/** @odoo-module **/

import { PosStore } from "@point_of_sale/app/services/pos_store";
import { patch } from "@web/core/utils/patch";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PosStore.prototype, {
    async addLineToCurrentOrder(vals, opts = {}, configure = true) {
        let product;
        if (vals.product_id) {
            product = vals.product_id;
        } else if (vals.product_tmpl_id) {
            product = vals.product_tmpl_id;
        }
        
        if (product) {
            const dangerKeywords = ["Alat potong", "Bahan kimia", "Cairan yang mudah terbakar", "Senjata tajam"];
            let isDangerous = false;
            
            if (product.pos_categ_ids) {
                const categoryNames = product.pos_categ_ids.map(c => (typeof c === 'object' ? c.name : "") || "");
                for (const name of categoryNames) {
                    if (name) {
                        for (const keyword of dangerKeywords) {
                            if (name.toLowerCase().includes(keyword.toLowerCase())) {
                                isDangerous = true;
                                break;
                            }
                        }
                    }
                    if (isDangerous) break;
                }
            }

            if (isDangerous) {
                await this.env.services.dialog.add(AlertDialog, {
                    title: "Peringatan Kemasan Khusus",
                    body: "Produk yang dipindai memerlukan penanganan khusus karena termasuk barang berbahaya atau tajam.",
                });
            }
        }
        return super.addLineToCurrentOrder(vals, opts, configure);
    }
});
