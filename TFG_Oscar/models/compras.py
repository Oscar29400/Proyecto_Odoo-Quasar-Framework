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
    idcompra = fields.Char('ID Compra')
    proveedor = fields.Many2one('proveedores')
    productos = fields.Many2one('productos')
    precioCompra = fields.Float(related="productos.precioCoste" ,string='Precio Coste Unidad')
    cantidad = fields.Integer('Cantidad')

    @api.model
    def create(self, values):
        result= super().create(values)
        self.actualizarVentas()
        return result

    def write(self, values):
        result= super(Compras,self).write(values)
        self.actualizarVentas()
        return result

    def unlink(self):
        result= super(Compras,self).unlink()
        self.actualizarVentas()
        return result

    def actualizarVentas(self):
        for producto in self.env['productos'].search([]):
            producto.nuevoc = producto.cantidad
            for compras in self.env['compras'].search([]):
                for prod in compras.productos:
                    if producto.id == prod.id:
                        producto.nuevoc = producto.nuevoc + compras.cantidad
                        break