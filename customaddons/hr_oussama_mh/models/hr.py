# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hr_employee(models.Model):
    _name = 'mh.hr_employee'
    _description = 'Employee'

    notebook_ids = fields.One2many('notebook.hr', 'main_class_id', string="Notebook")
    name = fields.Char()
    phone = fields.Char()
    mail = fields.Char()
    cin = fields.Integer()
    birth = fields.Date()
    adress = fields.Char()
    cnss = fields.Char()
    daily_cost = fields.Float()
    extra_hour_cost = fields.Float()
    total_leave = fields.Float()
    work_bonus = fields.Float()


class NotebookHr(models.Model):
    _name = 'notebook.hr'

    @api.depends('working_days','working_extra_hours','advance_salary','advance_bonus','advance_day')
    def _compute_rest(self):
        for each in self:
            salary = each.main_class_id.daily_cost*each.working_days+each.main_class_id.extra_hour_cost*each.working_extra_hours+each.main_class_id.work_bonus+each.main_class_id.total_leave*each.main_class_id.daily_cost
            each.rest = salary-each.advance_salary-each.advance_bonus-each.advance_day*each.main_class_id.daily_cost

    main_class_id = fields.Many2one('mh.hr_employee', string="Employés")
    working_days = fields.Float()
    working_extra_hours = fields.Float()
    advance_salary = fields.Float()
    advance_bonus = fields.Float()
    advance_day = fields.Float()
    start_month = fields.Date()
    end_month = fields.Date()
    rest = fields.Float(compute="_compute_rest", store=True)