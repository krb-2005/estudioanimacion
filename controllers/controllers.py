# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class estudio_controller(http.Controller):
    @http.route("/api/estudioanimacion/findAll", auth="public", method=["GET"], csrf=False)
    def get_proyectos(self, **kw):
        try:
            proyectos = http.request.env["estudioanimacion.proyecto"].sudo().search_read([], ['id', 'nombre', 'descripcion', 'duracion', 'director_id', 'tecnica_id', 'diseno_id', 'storyboard_id'])
            res = json.dumps(proyectos, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type="application/json;charset=utf-8", status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)