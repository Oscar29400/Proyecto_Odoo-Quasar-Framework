# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Empleados(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'empleados'
    _description = 'Modelo de la lista de empleados'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nombre"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    nombre = fields.Char()
    apellidos = fields.Char()
    seguridadSocial = fields.Char(string='Nº Seguridad Social')
    dni = fields.Char(string='DNI')
    foto = fields.Image(max_width=1000,max_height=1000)