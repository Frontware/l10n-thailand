# Copyright 2019 Ecosoft Co., Ltd (https://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "Thailand Localization - TAX Reports",
    "version": "14.0.1.0.0",
    "author": "Frontware, Ecosoft, Odoo Community Association (OCA)",
    "website": "https://github.com/Frontware/l10n-thailand",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": [
        "date_range",
        "report_xlsx_helper",
        "l10n_th_partner",
        "l10n_th_tax_invoice",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/paper_format.xml",
        "data/report_data.xml",
        "reports/tax_report.xml",
        "wizard/tax_report_wizard_view.xml",
    ],
    "installable": True,
}
