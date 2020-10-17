# -*- coding: utf-8 -*-
# from odoo import http


# class HrOussamaMh(http.Controller):
#     @http.route('/hr_oussama_mh/hr_oussama_mh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_oussama_mh/hr_oussama_mh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_oussama_mh.listing', {
#             'root': '/hr_oussama_mh/hr_oussama_mh',
#             'objects': http.request.env['hr_oussama_mh.hr_oussama_mh'].search([]),
#         })

#     @http.route('/hr_oussama_mh/hr_oussama_mh/objects/<model("hr_oussama_mh.hr_oussama_mh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_oussama_mh.object', {
#             'object': obj
#         })
