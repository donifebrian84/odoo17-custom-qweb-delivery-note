# Odoo 17 Custom QWeb Report Design - Delivery Note (Surat Jalan)

An enterprise-ready custom QWeb PDF report module for **Odoo 17 Inventory / Stock Delivery Orders**. This module replaces the standard delivery slip with a localized, clean, and highly functional Delivery Note (Surat Jalan) compliant with standard business verification workflows.

---

## 📌 Business Case & Objectives
Standard Odoo delivery slips often lack clear multi-party verification areas and localized document formatting. This custom QWeb report addresses these needs by providing:
1. Dynamic state-based quantity and status badges.
2. Clean layout structured with Bootstrap grid and modern typography.
3. Dedicated signature blocks for three-party validation (Sender, Driver/Carrier, Recipient).

---

## 🚀 Key Features & Technical Highlights

* **QWeb Logic & Conditionals (`t-if`, `t-else`):** Dynamic display of delivery status (e.g., pending badge vs. confirmed delivered quantity).
* **Dynamic Iteration (`t-foreach`, `t-set`):** Auto-incrementing line item counters and line item descriptions.
* **Safe Attribute Evaluators:** Code level handling for missing or optional fields (e.g., `carrier_id`).
* **Bootstrap Styling:** Professional layout using Bootstrap grid system (`row`, `col-6`, badges, table borders).
* **Native Odoo Integration:** Integrated directly into the `stock.picking` model under the standard **Print** action menu.

---

## 📂 Deliverables & Sample Output
* **Source Code:** Available in the [`custom_delivery_report/`](./custom_delivery_report) directory.
* **Sample PDF Output:** Download the generated PDF sample from [`docs/Surat_Jalan_WH_OUT_00001.pdf`](./docs/Surat_Jalan_WH_OUT_00001.pdf).

---

## ⚙️ Installation & Usage
1. Download or clone this repository.
2. Copy the `custom_delivery_report` directory into your Odoo `custom_addons` path.
3. Restart your Odoo Server and activate **Developer Mode**.
4. Go to **Apps** -> **Update Apps List**, search for `Custom Delivery Note QWeb Report`, and click **Activate**.
5. Navigate to **Inventory** -> **Delivery Orders** -> Open any record -> Click **Print** -> Select **Custom Surat Jalan**.