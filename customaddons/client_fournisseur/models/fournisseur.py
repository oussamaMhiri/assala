# -*- coding: utf-8 -*-

from odoo import models, fields, api


class supplier(models.Model):

    _name = 'mh.supplier'
    _description = 'Fournisseur'

    name = fields.Many2one('res.partner', string='Partner', ondelete='restrict')
    total = fields.Float()
    total_deadline = fields.Date()
    is_paid = fields.Boolean(default=False)
    notebook_ids = fields.One2many('notebook.supplier', 'main_class_id', string="Notebook")

class NotebookSupplier(models.Model):
    _name = 'notebook.supplier'

    main_class_id = fields.Many2one('mh.supplier', string="Fournisseur")
    subtotal = fields.Float()
    subtotal_deadline = fields.Date()
    is_paid = fields.Boolean(default=False)