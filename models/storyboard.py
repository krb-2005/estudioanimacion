# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class storyboard(models.Model):
    _name = 'estudioanimacion.storyboard'
    _description = 'estudioanimacion.storyboard'
    
    codigo = fields.Char(string="Código del storyboard", required=True)
    descripcion = fields.Char(string="Descripción", required=True)
    
    supervisor_id = fields.Many2one("estudioanimacion.supervisor", string="Supervisor")
    proyecto_id = fields.Many2one("estudioanimacion.proyecto", string="Proyecto", ondelete="cascade")