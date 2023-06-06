#-*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    number_order = fields.Char(required=True)
    date_addenda_order = fields.Date(required=True)


class ResPartner(models.Model):
    _inherit = "res.partner"

    shipping_number_cedis = fields.Char(required=True)