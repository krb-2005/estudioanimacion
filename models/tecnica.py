# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class tecnica(models.Model):
    _name = 'estudioanimacion.tecnica'
    _description = 'estudioanimacion.tecnica'
    
    nombre = fields.Char(string="Nombre de la técnica", readonly=False, required=True)
    descripcion = fields.Char(string="Descripción de la técnica", required=True)
    programa_utilizado = fields.Char(string="Programa utilizado", required=True)