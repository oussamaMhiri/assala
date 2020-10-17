# -*- coding: utf-8 -*-

from odoo import models, fields, api


class client(models.Model):
    _name = 'mh.client'
    _description = 'Client'

    @api.depends('advance', 'total')
    def _compute_rest(self):
        for each in self:
            each.rest = each.total-each.advance
    @api.depends('employee', 'material', 'extra')
    def _compute_charge(self):
        for each in self:
            each.charge = each.employee+each.material+each.extra

    name = fields.Many2one('res.partner', string='Partner', ondelete='restrict')
    total = fields.Float()
    advance= fields.Float()
    rest = fields.Float(compute="_compute_rest", store=True)
    charge = fields.Float(compute="_compute_charge", store=True)
    employee= fields.Float()
    material= fields.Float()
    extra= fields.Float()