# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
{
    "name": "Thai Localization - Account Tax Invoice",
    "version": "14.0.1.0.3",
    "author": "Frontware, Ecosoft, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/Frontware/l10n-thailand",
    "category": "Localization / Accounting",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/account_view.xml",
        "views/account_move_view.xml",
        "views/account_payment_view.xml",
    ],
    "installable": True,
    "development_status": "Alpha",
    "maintainers": ["kittiu"],
}
