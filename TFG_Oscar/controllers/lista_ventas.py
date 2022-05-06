# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from base64 import b64decode


# Clase del controlador web



class ListaVentas(http.Controller):
    
    '''
    Llamada web para obtener lista completa de productos. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/cargamento/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/cargamento/productos
    Y nos devolvera informacion sobre cada producto

    '''

    @http.route('/gestion/cargamento/ventacompleta', auth='public', cors='*', type='http')
    def obtenerDatosProductos(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "productos")
        productos = request.env['ventacompleta'].sudo().search([])
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        #Generamos la lista de cargamentos
        lista_productos=[]
        for s in productos:

            b64 = s.report_file
            bytes = b64decode(b64, validate=True)

            lista_productos.append({'id':s.id,'pdf':bytes})
        json_result= http.Response(json.dumps(lista_productos, default=str)
        ,status=200,mimetype='application/json')
        return json_result
