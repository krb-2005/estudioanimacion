# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class director(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    is_director = fields.Boolean(default=True)
    
    proyecto_id = fields.One2many(string="Proyectos dirigidos", comodel_name="estudioanimacion.proyecto", inverse_name="director_id")