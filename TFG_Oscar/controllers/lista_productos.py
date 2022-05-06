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

    @http.route('/gestion/cargamento/productos', auth='public', cors='*', type='http')
    def obtenerDatosProductos(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "productos")
        productos = request.env['productos'].sudo().search([])
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        #Generamos la lista de cargamentos
        lista_productos=[]
        for s in productos:
            imgurl = base_url + '/web/image?' + 'model=productos&id=' + str(s.id) + '&field=img'
            pdfurl = base_url + '/web/pdf?' + 'model=ventacompleta&id=' + str(s.id) + '&field=report_file'
            lista_productos.append({'id':s.id,'nombre':s.nombre,'descripcion':s.descripcion,
            'marca':s.marca.nombre,'cantidad':s.nuevoc,'precioCoste':s.precioCoste,'precioVenta':s.precioVenta,'img':imgurl})
        json_result= http.Response(json.dumps(lista_productos, default=str)
        ,status=200,mimetype='application/json')
        return json_result
