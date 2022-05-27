# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Usuarios(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'usuario'
    _description = 'Modelo de la lista de usuario'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="email"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    email = fields.Char()
    contrasena = fields.Char()
