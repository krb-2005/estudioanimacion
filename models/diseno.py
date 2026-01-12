# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class diseno(models.Model):
    _name = 'estudioanimacion.diseno'
    _description = 'estudioanimacion.diseno'
    
    nombre = fields.Char(string="Nombre del diseño", readonly=False, required=True)
    descripcion = fields.Char(string="Descripción del diseño", required=True)
    
    supervisor_id = fields.Many2one("estudioanimacion.supervisor", string="Supervisor de diseño", required=True, ondelete="cascade")