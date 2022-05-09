# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json, base64

# Clase del controlador web



class ListaProductos(http.Controller):
    
    '''
    Llamada web para obtener lista completa de productos. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/cargamento/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/cargamento/productos
    Y nos devolvera informacion sobre cada producto

    '''

    @http.route('/gestion/cargamento/clientes', auth='public', cors='*', type='http')
    def obtenerDatosProductos(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "productos")
        productos = request.env['clientes'].sudo().search([])
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')

        #Generamos la lista de cargamentos
        lista_productos=[]
        for s in productos:
            imgurl = base_url + '/web/image?' + 'model=clientes&id=' + str(s.id) + '&field=foto'
            lista_productos.append({'id':s.id,'nombre':s.nombre,'direccion':s.direccion,
            'email':s.email,'tlfno':s.tlfno,'dni':s.cif,'img':imgurl})
        json_result= http.Response(json.dumps(lista_productos, default=str)
        ,status=200,mimetype='application/json')
        return json_result
