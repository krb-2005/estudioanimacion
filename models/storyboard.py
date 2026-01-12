# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class storyboard(models.Model):
    _name = 'estudioanimacion.storyboard'
    _description = 'estudioanimacion.storyboard'
    
    codigo = fields.Char(compute="get_code", string="Código del storyboard", readonly=True, required=True)
    
    def get_code(self):
        for storyboard in self:
            storyboard.codigo = "Escena " + str(storyboard.id)