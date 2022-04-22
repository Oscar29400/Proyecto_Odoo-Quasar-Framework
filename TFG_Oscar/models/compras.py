# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Compras(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'compras'
    _description = 'Modelo de la lista de compras'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="idcompra"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    idcompra = fields.Char()
    proveedor = fields.Many2one('proveedores')
    productos = fields.Many2one('productos')
    precioCompra = fields.Float(related="productos.precioCoste" ,string='Precio Coste')