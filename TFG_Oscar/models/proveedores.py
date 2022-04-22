# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Proveedores(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'proveedores'
    _description = 'Modelo de la lista de proveedores'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nombre"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    nombre = fields.Char('Nombre del Proveedor')
    direccion = fields.Char('Dirección del Proveedor')
    ciudad = fields.Char('Ciudad')
    email = fields.Char('Email')
    tlfno = fields.Char('Telefono')
    cif = fields.Char(string='CIF')
    foto = fields.Image(max_width=50,max_height=50)