# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    number_order = fields.Char(related="x_studio_orden_de_compra")

class AccountMove(models.Model):
    _inherit = "account.move.line"

    def get_type_product_uom(self, register):
        for rec in register:
            if rec.product_uom_id.name in ('Caja', 'caja', 'CAJA'):
                return 'AE'
            else:
                return 'EA'
