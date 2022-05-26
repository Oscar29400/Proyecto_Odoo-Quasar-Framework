# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Productos(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'productos'
    _description = 'Modelo de la lista de Productos'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nombre"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    nombre = fields.Char('Nombre')
    img = fields.Image(max_width=1000,max_height=1000, string='Imagen')
    descripcion = fields.Html(sanitaze=True,strp_style=False)
    marca= fields.Many2one('proveedores', string='Marca')
    cargamento = fields.Many2one('compras')
    cantidad = fields.Integer()
    precioCoste = fields.Float('Precio Coste', digits=(12,2))
    precioVenta = fields.Float(compute='_precio',store=True,string='Precio Venta', digits=(12,2))
    nuevoc = fields.Integer(compute='_cantidad', store=True,string='Cantidad')
    @api.depends('precioCoste')
    def _precio(self):
        for rec in self:
           rec.update({'precioVenta': rec.precioCoste*1.50})
    
    @api.depends('cantidad')
    def _cantidad(self):
        for rec in self:
            rec.nuevoc = rec.cantidad
    