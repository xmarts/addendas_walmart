# -*- coding: utf-8 -*-
from odoo import http

# class AddendasWalmart(http.Controller):
#     @http.route('/addendas_walmart/addendas_walmart/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addendas_walmart/addendas_walmart/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addendas_walmart.listing', {
#             'root': '/addendas_walmart/addendas_walmart',
#             'objects': http.request.env['addendas_walmart.addendas_walmart'].search([]),
#         })

#     @http.route('/addendas_walmart/addendas_walmart/objects/<model("addendas_walmart.addendas_walmart"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addendas_walmart.object', {
#             'object': obj
#         })