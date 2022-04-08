# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class ventar(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'ventar'
    _description = 'Modelo de la lista de Venta y Reparacion'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nombre"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    nombre = fields.Char()
    precioVenta = fields.Float(compute='_precio')

    @api.depends('precioCoste')
    def _precio(self):
        for rec in self:
           rec.update({'precioVenta': rec.precioCoste*1.50})