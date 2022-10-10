# -*- coding: utf-8 -*-

from odoo import models, fields, api

class curso(models.Model):
    _name = 'curso.curso'
    _description = 'curso.curso'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="description")

    level = fields.Selection(string="level", selection=[("beginner", "Beginner"), ("intermediate", "Intermediate"), ("advanced", "Advanced")],
    copy=False)

    active = fields.Boolean(string="Active", default=True)