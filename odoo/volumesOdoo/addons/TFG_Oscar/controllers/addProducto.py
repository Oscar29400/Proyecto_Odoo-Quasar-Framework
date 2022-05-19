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
    Se puede probar accediendo a http://localhost:8069/gestion/addProducto/suela/Una suela de graan calidad/12.55/
    Y nos devolvera informacion sobre cada producto

    '''
    #TROZO GET PARA PRODUCTOS
    @http.route('/gestion/addProducto/<nombre>/<descripcion>/<precioCoste>/<cantidad>/<img>', auth="none", cors='*', type='http')
    def apiPost(self,nombre,descripcion,precioCoste,cantidad,img ,**args):
        productos = request.env['productos'].sudo().search([])

        #Generamos la lista de cargamentos
        record = request.env['productos'].sudo().create({'nombre':nombre,'descripcion':descripcion,'precioCoste':precioCoste,'cantidad':cantidad,'img':img})
        json_result= http.Response(json.dumps(record, default=str)
        ,status=200,mimetype='application/json')
        return json_result