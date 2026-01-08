# -*- coding: utf-8 -*-
# from odoo import http


# class Estudioanimacion(http.Controller):
#     @http.route('/estudioanimacion/estudioanimacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estudioanimacion/estudioanimacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estudioanimacion.listing', {
#             'root': '/estudioanimacion/estudioanimacion',
#             'objects': http.request.env['estudioanimacion.estudioanimacion'].search([]),
#         })

#     @http.route('/estudioanimacion/estudioanimacion/objects/<model("estudioanimacion.estudioanimacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estudioanimacion.object', {
#             'object': obj
#         })

