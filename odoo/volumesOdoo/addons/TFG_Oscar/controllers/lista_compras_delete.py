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
    Se puede probar accediendo a http://localhost:8069//gestion/apirest/delete/cliente
    Y nos devolvera informacion sobre cada producto

    '''
    #TROZO GET PARA PRODUCTOS
    @http.route('/gestion/apirest/delete/compras', auth="none", cors='*', csrf=False, methods=["GET"],
                type='http')
    def apiGet(self, **args):
        #Obtenemos el modelo y si hay id, hacemos la busqueda
        search = []
        #Pasamos lo recibido en "data" a un diccionario
        dicDatos=json.loads(args['data'])
        #Si se ha indicado id, hay busqueda
        if dicDatos["id"]:
            search = [('id', '=', int(dicDatos["id"]))]
        else:
            return "{'estado':'CARGAMENTO NO INDICADO'}"

        #Si es GET, devolvemos el registro de la busqueda
        if (http.request.httprequest.method == 'GET'):
            record = http.request.env[ 'compras'].sudo().search(search)
        #Si hay algun elemento
            if record and record[0]:
                #Eliminamos el registro encontrado
                record[0].unlink()
                #Devolvemos el registro eliminado, siguiendo este esquema
                return http.Response(
                    json.dumps(
                    
                        record[0].read(), #Lectura del registro
                        default=str #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
                        ),
                        status=200, # Respuesta de la aplicación al navegador
                        mimetype='application/json'
                    )
            return "{'estado':'NO ENCONTRADO'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        #Si no es GET ni DELETE