# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class director(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    proyecto_id = fields.One2many(string="Proyectos", comodel_name="estudioanimacion.proyecto", inverse_name="director_id")