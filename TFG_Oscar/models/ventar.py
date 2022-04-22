# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class ventar(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'ventar'
    _description = 'Modelo de la lista de Venta y Reparacion'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="id"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    empleado = fields.Many2one('empleados')
    producto = fields.Many2one('productos')
    cantidad = fields.Integer()
    precioVenta = fields.Float(related="producto.precioVenta" , string="Precio Venta")
    precioVenta2 = fields.Float(compute='_precio')
    

    @api.depends('precioVenta')
    def _precio(self):
        for rec in self:
           rec.update({'precioVenta2': rec.precioVenta*rec.cantidad})
    
    @api.model
    def create(self, values):
        result= super().create(values)
        self.actualizarVentas()
        return result

    def write(self, values):
        result= super(ventar,self).write(values)
        self.actualizarVentas()
        return result

    def unlink(self):
        result= super(ventar,self).unlink()
        self.actualizarVentas()
        return result

    def actualizarVentas(self):
        for producto in self.env['productos'].search([]):
            producto.nuevoc = producto.cantidad
            for ventas in self.env['ventar'].search([]):
                for prod in ventas.producto:
                    if producto.id == prod.id:
                        if (producto.nuevoc - ventas.cantidad) < 0:
                            raise models.ValidationError('no se puede')
                        else:
                            producto.nuevoc = producto.nuevoc - ventas.cantidad
                            break