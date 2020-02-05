# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddFieldsAdendaWalmart(models.Model):
    _inherit = 'res.partner'

    child_contact_name1 = fields.Char(string="Child Contact Name")
