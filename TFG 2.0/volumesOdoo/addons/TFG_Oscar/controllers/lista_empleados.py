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

    @http.route('/gestion/cargamento/empleados', auth='public', cors='*', type='http')
    def obtenerDatosProductos(self, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "productos")
        productos = request.env['empleados'].sudo().search([])
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')

        #Generamos la lista de cargamentos
        lista_productos=[]
        for s in productos:
            imgurl = base_url + '/web/image?' + 'model=empleados&id=' + str(s.id) + '&field=foto'
            lista_productos.append({'id':s.id,'nombre':s.nombre,'apellidos':s.apellidos,
            'seguridadSocial':s.seguridadSocial,'dni':s.dni,'img':imgurl})
        json_result= http.Response(json.dumps(lista_productos, default=str)
        ,status=200,mimetype='application/json')
        return json_result

    
    #TROZO  POST PARA EMPLEADOS

    #Definimos la operacion para metodos POST, PUT y MATCH
    @http.route('/gestion/apirest/empleados', auth="none", cors='*', csrf=False,
                methods=["POST", "PUT", "PATCH"], type='http')
    def apiPost(self, **args):
        #Obtenemos el modelo de los argumentos

        #Pasamos lo recibido en "data" a un diccionario
        dicDatos=json.loads(args['data'])
        #Si se ha indicado id, hay busqueda
        if dicDatos["id"]:
            search = [('id', '=', int(dicDatos["id"]))]
        else:
            return "{'estado':'CARGAMENTO NO INDICADO'}"
        #Si la peticion es de tipo POST,ejecutamos esto
        #En este caso, crearemos un nuevo registro con los datos indicados en "data"
        if (http.request.httprequest.method == 'POST'):
            #Creamos el nuevo registro
            record = request.env['empleados'].sudo().create(
                #Proporcionamos un diccionario con los datos del registro a crear
                dicDatos
                )
            
            #Devolvemos el registro creado, siguiendo este esquema
            return http.Response(
                json.dumps(
                
                    record.read(), #Lectura del registro
                    default=str #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
                    ),
                    status=200, # Respuesta de la aplicación al navegador
                    mimetype='application/json'
                )
        #Si la peticion es de tipo PUT o PATCH, ejecutamos esto
        #En este caso, modificaremos un registro con un numero de socio concreto, cambiando 
        #a los valores pasados en "data"
        if (http.request.httprequest.method == 'PUT' or http.request.httprequest.method == 'PATCH'):

            record = http.request.env['empleados'].sudo().search(search)
            if record and record[0]:
                record[0].write(dicDatos)
                #Devolvemos el registro creado, siguiendo este esquema
                return http.Response(
                    json.dumps(
                    
                        record.read(), #Lectura del registro
                        default=str #Funcion de conversion por defecto (str, para convertir a String elementos como los datetime)
                        ),
                        status=200, # Respuesta de la aplicación al navegador
                        mimetype='application/json'
                    )
            #Caso de que el registro no sea encontrado
            return "Registro no encontrado"
        #Si no es POST, PUT ni PATCH
        return http.request.env['ir.http'].session_info()

    #TROZO GET PARA EMPLEADOS   
    @http.route('/gestion/apirest/empleados', auth="none", cors='*', csrf=False, methods=["GET", "DELETE"],
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
            record = http.request.env['empleados'].sudo().search(search)
            if record and record[0]:
                lista_productos=[]
                base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            for s in record:
                imgurl = base_url + '/web/image?' + 'model=empleados&id=' + str(s.id) + '&field=foto'
                lista_productos.append({'id':s.id,'nombre':s.nombre,'apellidos':s.apellidos,
                'seguridadSocial':s.seguridadSocial,'dni':s.dni,'img':imgurl})
                return http.Response( 
                json.dumps(lista_productos, default=str)[1:-1], 
                    status=200,
                    mimetype='application/json'
                )

            return "{'estado':'NO ENCONTRADO'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        if (http.request.httprequest.method == 'DELETE'):

            record = http.request.env[ 'empleados'].sudo().search(search)
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
        #Si no es GET ni DELETE
        return http.request.env['ir.http'].session_info()