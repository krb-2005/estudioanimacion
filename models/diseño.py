# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class diseño(models.Model):
    _name = 'estudioanimacion.diseño'
    _description = 'estudioanimacion.diseño'
    
    nombre = fields.Char(string="Nombre del diseño", readonly=False, required=True)
    descripcion = fields.Char(string="Descripción del diseño", required=True)