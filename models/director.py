# -*- coding: utf-8 -*-

from odoo import models, fields, api;

class director(models.Model):
    _name = 'estudioanimacion.director'
    _inherit = 'res.partner'