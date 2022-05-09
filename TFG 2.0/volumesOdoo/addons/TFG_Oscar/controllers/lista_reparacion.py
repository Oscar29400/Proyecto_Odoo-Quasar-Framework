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

    @http.route('/gestion/cargamento/reparacion', auth='public', cors='*', type='http')
    def obtenerDatosProductos(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "productos")
        productos = request.env['reparacion'].sudo().search([])
        #Generamos la lista de cargamentos
        lista_productos=[]
        for s in productos:
            lista_productos.append({'id':s.id,'idventa':s.idventa,'empleado':s.empleado.nombre,'cliente':s.cliente.nombre,
            'reparacion':s.reparar,'precioTotal':s.precioRTotal,
            'precioNeto':s.precioRNeto,'fechaEntrega':s.fecha_entrega,'fechaCompra':s.fecha_compra})
        json_result= http.Response(json.dumps(lista_productos, default=str)
        ,status=200,mimetype='application/json')
        return json_result
