# -*- coding: utf-8 -*-

from odoo import models, fields, api;
import datetime

class proyecto(models.Model):
    _name = 'estudioanimacion.proyecto'
    _description = 'estudioanimacion.proyecto'
    
    nombre = fields.Char(string="Nombre", readonly=False, required=True)
    descripcion = fields.Char(string="Sinopsis del proyecto")
    duracion = fields.Integer(string="Duración", default=10)
    fecha_inicio = fields.Datetime(string="Fecha de inicio", default=lambda p: datetime.datetime.now())
    fecha_salida = fields.Datetime(string="Fecha de salida", compute="_get_fecha_salida", store=True)
    imagen = fields.Image(string="Imagen")
    
    director_id = fields.Many2one("res.partner", string="Director", ondelete="cascade")
    tecnica_id = fields.Many2one("estudioanimacion.tecnica", string="Técnica de animación", ondelete="cascade")
    diseno_id = fields.One2many(string="Diseños", comodel_name="estudioanimacion.diseno", inverse_name="proyecto_id")
    storyboard_id = fields.One2many(string="Storyboards", comodel_name="estudioanimacion.storyboard", inverse_name="proyecto_id")
    
    @api.depends('fecha_inicio', 'duracion')
    def _get_fecha_salida(self):
        for proyecto in self:
            if isinstance(proyecto.fecha_inicio, datetime.datetime) and proyecto.duracion > 0:
                proyecto.fecha_salida = proyecto.fecha_inicio + datetime.timedelta(days = proyecto.duracion)
            else:
                proyecto.fecha_salida = proyecto.fecha_inicio
    
    def f_create(self):
        proyecto = {
            "nombre": "Proyecto de prueba",
            "descripcion": "Un proyecto básico",
            "duracion": 1,
        }
        print(proyecto)
        self.env["estudioanimacion.proyecto"].create(proyecto)
    
    def f_search_update(self):
        proyecto = self.env["estudioanimacion.proyecto"].search([('nombre', '=', 'Proyecto de prueba')])
        print('search()', proyecto, proyecto.name)
        
        proyecto.write({
            "nombre": "Proyecto actualizado"
        })
    
    def f_delete(self):
        proyecto = self.env["estudioanimacion.proyecto"].browse([1])
        proyecto.unlink()