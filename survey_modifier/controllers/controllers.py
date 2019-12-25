# -*- coding: utf-8 -*-
from odoo import http

# class SurveyModifier(http.Controller):
#     @http.route('/survey_modifier/survey_modifier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/survey_modifier/survey_modifier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('survey_modifier.listing', {
#             'root': '/survey_modifier/survey_modifier',
#             'objects': http.request.env['survey_modifier.survey_modifier'].search([]),
#         })

#     @http.route('/survey_modifier/survey_modifier/objects/<model("survey_modifier.survey_modifier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('survey_modifier.object', {
#             'object': obj
#         })