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

    @http.route('/gestion/cargamento/ventacompleta', auth='public', cors='*', type='http')
    def obtenerDatosProductos(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "productos")
        productos = request.env['ventacompleta'].sudo().search([])
        ventar = request.env['ventar'].sudo().search([])
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        #Generamos la lista de cargamentos
        lista_productos=[]
        produc= []
        stringa = ""
        i=0
        for s in productos:
            for ventas in ventar:
                produc.append(ventas.producto)
                stringa += str(produc[i].nombre)+","
                i +=1
            stringa = stringa[:-1]
            x = stringa.split(",")
            pdfurl = base64.b64encode(s.report_file)
            lista_productos.append({'id':s.id,'idventa':s.idventa,'empleado':s.empleado.nombre,'cliente':s.cliente.nombre,'producto':x,
            'precioTotal':s.precioTotal,'precioNeto':s.precioNeto,'fechaEntrega':s.fecha_entrega,'fechaCompra':s.fecha_compra})
        json_result= http.Response(json.dumps(lista_productos, default=str)
        ,status=200,mimetype='application/json')
        return json_result
