# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    text_amount_language_currency = fields.Selection([('fr', 'French'),
                                                      ], string='Text amount language/currency')


class AccountConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    text_amount_language_currency = fields.Selection(related="company_id.text_amount_language_currency",
                                                     string='language_currency', readonly=False)

    @api.onchange('text_amount_language_currency')
    def save_text_amount_language_currency(self):
        if self.text_amount_language_currency:
            self.company_id.text_amount_language_currency = self.text_amount_language_currency