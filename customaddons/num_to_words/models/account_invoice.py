# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.move"

    text_amount = fields.Char(string="Montant en lettre", required=False, compute="amount_to_words", store=True)

    @api.depends('amount_total')
    def amount_to_words(self):
        if self.company_id.text_amount_language_currency:
            intpart, decimalpart = int(self.amount_total), int((self.amount_total - int(self.amount_total))*1000)
            self.text_amount = num2words(intpart, lang='fr') + ' Dinars et ' + num2words(decimalpart, lang='fr') + ' Millimes '
