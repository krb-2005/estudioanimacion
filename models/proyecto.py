# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class proyecto(models.Model):
    _name = 'estudioanimacion.proyecto'
    _description = 'estudioanimacion.proyecto'
    
    nombre = fields.Char(string="Nombre", readonly=False, required=True)
    descripcion = fields.Char(string="Sinopsis del proyecto", required=True)
    fecha_inicio = fields.Date(string="Fecha de inicio", required=True)
    fecha_salida = fields.Date(string="Fecha de salida")
    
    director_id = fields.Many2one("estudioanimacion.director", string="Director", required=True, ondelete="cascade")
    tecnica_id = fields.Many2one("estudioanimacion.tecnica", string="Técnica de animación", required=True, ondelete="cascade")
    diseno_id = fields.One2many(string="Diseños", comodel_name="estudioanimacion.diseno", inverse_name="proyecto_id")