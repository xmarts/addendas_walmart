# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    number_order = fields.Char(related="x_studio_orden_de_compra")