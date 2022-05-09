# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web



class ListaCargamentos(http.Controller):
    
    '''
    Llamada web para obtener lista completa de cargamentos. No es parte de la API REST.
    
    
    Decorador que indica que la url "/gestion/<modelo>" atendera por HTTP, sin autentificacion
    Devolvera texto que estará en formato JSON
    Se puede probar accediendo a http://localhost:8069/gestion/cargamento
    Y nos devolvera informacion sobre cada cargamento

    '''

    @http.route('/gestion/<modelo>', auth='public', cors='*', type='http')
    def obtenerDatosCargamentos(self, modelo, **kw):
        # Obtenemos la referencia del modelo (pensado en este programa para ser "cargamento")
        cargamentos = request.env[modelo].sudo().search([])

        #Generamos la lista de cargamentos
        lista_cargamentos=[]
        for s in cargamentos:
            lista_cargamentos.append(s.read())
        json_result= http.Response(json.dumps(lista_cargamentos, default=str)[1:-1].replace("], [",","),status=200,mimetype='application/json') 
        return json_result
