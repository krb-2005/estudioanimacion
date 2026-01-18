# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class supervisor(models.Model):
    _name = 'estudioanimacion.supervisor'
    _description = 'estudioanimacion.supervisor'
    
    nombre = fields.Char(string="Nombre", readonly=False, required=True)
    apellido = fields.Char(string="Apellido", readonly=False, required=True)
    email = fields.Char(string="Email", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    
    diseno_id = fields.One2many(string="Diseños", comodel_name="estudioanimacion.diseno", inverse_name="supervisor_id")
    storyboard_id = fields.One2many(string="Storyboards", comodel_name="estudioanimacion.storyboard", inverse_name="supervisor_id")
    
    def f_create(self):
        supervisor = {
            "nombre": "Supervisor",
            "apellido": "Prueba",
            "email": "ejemplo@gmail.com",
            "telefono": "123456789"
        }
        print(supervisor)
        self.env["estudioanimacion.supervisor"].create(supervisor)
    
    def f_search_update(self):
        supervisor = self.env["estudioanimacion.supervisor"].search([('nombre', '=', 'Supervisor')])
        print('search()', supervisor, supervisor.name)
        
        supervisor.write({
            "nombre": "Supervisor actualizado"
        })
    
    def f_delete(self):
        supervisor = self.env["estudioanimacion.supervisor"].browse([1])
        supervisor.unlink()