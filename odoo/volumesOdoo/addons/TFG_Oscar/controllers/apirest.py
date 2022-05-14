# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class ApiRest(http.Controller):
    

    '''
    DEFINIMOS LA API REST
    https://geekytheory.com/que-es-una-api-rest-y-para-que-se-utiliza/

    INFORMACION SOBRE LA API REST
    Se accedera mediante "/gestion/apirest/<model>" (aunque el programa esta pensando para que sea socio)
    La operación que se realizará depende de si es una llamada POST, PUT, PATCH, GET o DELETE
    La información sobre la operación se enviara formateada en JSON en un parametro llamada "data"
    FIN INFORMACION SOBRE LA API REST

    SE PUEDE PROBAR CON LA EXTENSION THUNDER CLIENT
    Nombre: Thunder Client
    Vínculo de VS Marketplace: https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
    
    '''




    '''

    Probar POST (Creando el cargamento cuyo id es 3)
    Valor de data: {"id":"3", "nombre":"Materiales"}
    URL COMPLETA (Enviada con POST): http://localhost:8069/gestion/apirest/cargamento?data={"id":"3", "nombre":"Materiales"}

    --------------
    Probar PUT/PATCH (Modificando el cargamento cuyo id es 3)
    Valor de data: {"id":"3", "nombre":"Electronica"}

    URL COMPLETA (Enviada con PUT/PATCH): http://localhost:8069/gestion/apirest/cargamento?data={"id":"3", "nombre":"Electronica"}

    '''

    """#TROZO POST PARA PRODUCTOS

    #Definimos la operacion para metodos POST, PUT y MATCH
    @http.route('/gestion/apirest/productos', auth="none", cors='*', csrf=False,
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
            record = request.env['productos'].sudo().create(
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

            record = http.request.env['productos'].sudo().search(search)
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
"""

    """#TROZO APIREST PARA EMPLEADOS

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
        return http.request.env['ir.http'].session_info()"""
        


    '''

    Probar GET (Consultando el cargamento 1)
    Valor de data: {"id":"1"}
    URL COMPLETA (Enviada con GET): http://localhost:8069/gestion/apirest/cargamento?data={"id":"1"} 

    --------------
    Probar DELETE (Consultando el cargamento 1)
    Valor de data: {"id":"1"}

    URL COMPLETA (Enviada con DELETE): http://localhost:8069/gestion/apirest/productos?data={"id":"1"}  

    '''
    """#TROZO GET PARA PRODUCTOS
    @http.route('/gestion/apirest/productos', auth="none", cors='*', csrf=False, methods=["GET", "DELETE"],
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
            record = http.request.env['productos'].sudo().search(search)
            if record and record[0]:
                lista_productos=[]
                base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
                for s in record:
                    imgurl = base_url + '/web/image?' + 'model=productos&id=' + str(s.id) + '&field=img'
                    descripcion = s.descripcion.replace("<p>","").replace("<br>","").replace("</p>","")
                    lista_productos.append({'id':s.id,'nombre':s.nombre,'descripcion':descripcion,
                    'marca':s.marca.nombre,'cantidad':s.nuevoc,'precioCoste':s.precioCoste,'precioVenta':s.precioVenta,'img':imgurl})
                return http.Response( 
                json.dumps(lista_productos, default=str)[1:-1], 
                    status=200,
                    mimetype='application/json'
                )

            return "{'estado':'NO ENCONTRADO'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        if (http.request.httprequest.method == 'DELETE'):

            record = http.request.env[ 'productos'].sudo().search(search)
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
        return http.request.env['ir.http'].session_info()"""


    """    #TROZO GET PARA EMPLEADOS   
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
        return http.request.env['ir.http'].session_info()"""

    """    #TROZO GET PARA CLIENTES   
    @http.route('/gestion/apirest/clientes', auth="none", cors='*', csrf=False, methods=["GET", "DELETE"],
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
            record = http.request.env['clientes'].sudo().search(search)
            if record and record[0]:
                lista_productos=[]
                base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            for s in record:
                imgurl = base_url + '/web/image?' + 'model=clientes&id=' + str(s.id) + '&field=foto'
                lista_productos.append({'id':s.id,'nombre':s.nombre,'direccion':s.direccion,
                'email':s.email,'tlfno':s.tlfno,'dni':s.cif,'img':imgurl})
                return http.Response( 
                json.dumps(lista_productos, default=str)[1:-1], 
                    status=200,
                    mimetype='application/json'
                )

            return "{'estado':'NO ENCONTRADO'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        if (http.request.httprequest.method == 'DELETE'):

            record = http.request.env[ 'clientes'].sudo().search(search)
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
        return http.request.env['ir.http'].session_info()"""

    """    #TROZO GET PARA COMPRAS    
    @http.route('/gestion/apirest/compras', auth="none", cors='*', csrf=False, methods=["GET", "DELETE"],
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
            record = http.request.env['compras'].sudo().search(search)
            if record and record[0]:
                lista_productos=[]
                base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
                for s in record:
                    lista_productos.append({'idCompra':s.idcompra,'proveedor':s.proveedor.nombre,'productos':s.productos.nombre,
                    'precioCosteUnidad':s.precioCompra,'cantidad':s.cantidad})
                return http.Response( 
                json.dumps(lista_productos, default=str)[1:-1], 
                    status=200,
                    mimetype='application/json'
                )

            return "{'estado':'NO ENCONTRADO'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        if (http.request.httprequest.method == 'DELETE'):

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
        #Si no es GET ni DELETE
        return http.request.env['ir.http'].session_info()"""


"""        #TROZO GET PARA PROVEEDORES    
    @http.route('/gestion/apirest/proveedores', auth="none", cors='*', csrf=False, methods=["GET", "DELETE"],
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
            record = http.request.env['proveedores'].sudo().search(search)
            if record and record[0]:
                lista_proveedores=[]
                base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
                for s in record:
                    imgurl = base_url + '/web/image?' + 'model=proveedores&id=' + str(s.id) + '&field=foto'
                    lista_proveedores.append({'id':s.id,'nombre':s.nombre,'direccion':s.direccion,
                    'ciudad':s.ciudad,'email':s.email,'tlfno':s.tlfno,'cif':s.cif,'img':imgurl})
                return http.Response( 
                json.dumps(lista_proveedores, default=str)[1:-1], 
                    status=200,
                    mimetype='application/json'
                )

            return "{'estado':'NO ENCONTRADO'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        if (http.request.httprequest.method == 'DELETE'):

            record = http.request.env[ 'proveedores'].sudo().search(search)
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
        return http.request.env['ir.http'].session_info()"""

"""    #TROZO GET PARA REPARACION    
    @http.route('/gestion/apirest/reparacion', auth="none", cors='*', csrf=False, methods=["GET", "DELETE"],
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
            record = http.request.env['reparacion'].sudo().search(search)
            if record and record[0]:
                lista_reparacion=[]
                base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
                for s in record:
                    lista_reparacion.append({'id':s.id,'idventa':s.idventa,'empleado':s.empleado.nombre,'cliente':s.cliente.nombre,
                    'reparacion':s.reparar,'precioTotal':s.precioRTotal,
                    'precioNeto':s.precioRNeto,'fechaEntrega':s.fecha_entrega,'fechaCompra':s.fecha_compra})
                return http.Response( 
                json.dumps(lista_reparacion, default=str)[1:-1], 
                    status=200,
                    mimetype='application/json'
                )

            return "{'estado':'NO ENCONTRADO'}"
        #Si es delete, cogemos el primer elemento de la busqueda
        if (http.request.httprequest.method == 'DELETE'):

            record = http.request.env[ 'reparacion'].sudo().search(search)
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
        return http.request.env['ir.http'].session_info()"""

