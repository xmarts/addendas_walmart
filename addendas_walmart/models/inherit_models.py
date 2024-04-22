# -*- coding: utf-8 -*-
from odoo import api, models, fields, tools, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_round, float_is_zero

import logging
import re
import base64
import json
import requests
import random
import string

from collections import defaultdict
from lxml import etree
from lxml.objectify import fromstring
from math import copysign
from datetime import datetime
from zeep import Client
from zeep.transports import Transport
from json.decoder import JSONDecodeError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    number_order = fields.Char(required=True)
    date_addenda_order = fields.Date(required=True)


class ResPartner(models.Model):
    _inherit = "res.partner"

    shipping_number_cedis = fields.Char(required=True)
    is_walmart = fields.Boolean()

class AccountEdiFormat(models.Model):
    _inherit = 'account.edi.format'

    def _l10n_mx_edi_export_invoice_cfdi(self, invoice):
        ''' Create the CFDI attachment for the invoice passed as parameter.

        :param move:    An account.move record.
        :return:        A dictionary with one of the following key:
        * cfdi_str:     A string of the unsigned cfdi of the invoice.
        * error:        An error if the cfdi was not successfuly generated.
        '''
        res = super(AccountEdiFormat, self)._l10n_mx_edi_export_invoice_cfdi(invoice)
        
        # == CHANGE URL schemaLocation IF PARTNER IS WALMART ==
        if invoice.partner_id.is_walmart and res.get('cfdi_str', False):
            res['cfdi_str'] = re.sub(rb'(xsi:schemaLocation=")[^"]*(")', rb'\g<1>' + b'http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd http://www.sat.gob.mx/ComercioExterior11 http://www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xsd http://www.pegasotecnologia.com/secfd/Schemas/Receptor/Walmart http://www.pegasotecnologia.com/secfd/Schemas/Receptor/Walmart' + rb'\g<2>', res['cfdi_str'], count=1)

        return res

    def _l10n_mx_edi_post_invoice_pac(self, invoice, exported):
        res = super(AccountEdiFormat, self)._l10n_mx_edi_post_invoice_pac(invoice, exported)
        
        # == CHANGE URL schemaLocation IF PARTNER IS WALMART ==
        if invoice.partner_id.is_walmart and res.get('cfdi_signed', False):
            res['cfdi_signed'] = re.sub(rb'(xsi:schemaLocation=")[^"]*(")', rb'\g<1>' + b'http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd http://www.sat.gob.mx/ComercioExterior11 http://www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xsd http://www.pegasotecnologia.com/secfd/Schemas/Receptor/Walmart http://www.pegasotecnologia.com/secfd/Schemas/Receptor/Walmart' + rb'\g<2>', res['cfdi_signed'], count=1)

        return res