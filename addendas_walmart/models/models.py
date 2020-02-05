# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddFieldsAdendaWalmart(models.Model):
    _inherit = 'res.partner'

    addres_contact_name = fields.Char(string="Child Contact Name")
