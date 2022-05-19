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
    #TROZO GET PARA PRODUCTOS
    @http.route('/gestion/apirest/facturas', auth="none", cors='*', csrf=False, methods=["GET"], type='http')
    def apiGet(self, **args):  
        #Obtenemos el modelo y si hay id, hacemos la busqueda
        search = []
        #Pasamos lo recibido en "data" a un diccionario
        dicDatos=json.loads(args['data'])
        #Si se ha indicado id, hay busqueda
        if dicDatos["cliente"]:
            search = [('cliente', '=', int(dicDatos["cliente"]))]
        else:
            return "{'estado':'CARGAMENTO NO INDICADO'}"

        record = request.env['ventacompleta'].sudo().search(search)
        rec = request.env['reparacion'].sudo().search(search)
    #Si hay algun elemento
        lista_ventas=[]

        if (record and record[0]) or (rec and rec[0]):
            for s in record:
                pdfurl = str(s.report_file)[2:-1]
                pdfurl = 'data:application/pdf;base64,'+pdfurl
                lista_ventas.append({'id':s.idventa,'cliente':s.cliente.nombre,'pdf':pdfurl})
            for c in rec:
                pdfurlr = str(c.report_file)[2:-1]
                pdfurlr = 'data:application/pdf;base64,'+pdfurlr
                lista_ventas.append({'id':c.idventa,'cliente':s.cliente.nombre,'pdf':pdfurlr})
        json_result= http.Response(json.dumps(lista_ventas, default=str)
        ,status=200,mimetype='application/json')
        return json_result
    #Si es delete, cogemos el primer elemento de la busqueda
    #Si no es GET ni DELETE