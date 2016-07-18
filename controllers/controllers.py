# -*- coding: utf-8 -*-
from openerp import http

# class ModElectrolab(http.Controller):
#     @http.route('/mod_electrolab/mod_electrolab/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mod_electrolab/mod_electrolab/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mod_electrolab.listing', {
#             'root': '/mod_electrolab/mod_electrolab',
#             'objects': http.request.env['mod_electrolab.mod_electrolab'].search([]),
#         })

#     @http.route('/mod_electrolab/mod_electrolab/objects/<model("mod_electrolab.mod_electrolab"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mod_electrolab.object', {
#             'object': obj
#         })