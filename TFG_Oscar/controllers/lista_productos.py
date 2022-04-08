# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class ListaProductos(http.Controller):
    
    '''
    Llamada web para obtener lista completa de productos. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/cargamento/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/cargamento/productos
    Y nos devolvera informacion sobre cada producto

    '''

    @http.route('/gestion/cargamento/<modelo>', auth='public', cors='*', type='http')
    def obtenerDatosProductos(self, modelo, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "productos")
        productos = request.env[modelo].sudo().search([])

        #Generamos la lista de cargamentos
        lista_productos=[]
        for s in productos:
            lista_productos.append(s.read())
        json_result= http.Response(json.dumps(lista_productos, default=str)[1:-1].replace("], [",","),status=200,mimetype='application/json') 
        return json_result
