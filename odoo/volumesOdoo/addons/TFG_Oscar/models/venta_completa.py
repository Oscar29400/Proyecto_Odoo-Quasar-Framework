# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
#Definimos el modelo de datos
class ventar(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'ventacompleta'
    _description = 'Modelo de la lista de Venta y Reparacion'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="id"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    idventa = fields.Char(string='ID Venta', compute='_idventa')
    empleado = fields.Many2one('empleados', string='Vendedor')
    cliente = fields.Many2one('clientes', string='Cliente')
    producto = fields.Many2many('ventar', string='Producto', required=True)
    precioTotal = fields.Float(compute='_precioT', string='Precio Total', digits=(12,2))
    precioNeto = fields.Float(compute='_precioN', string='Precio Neto', digits=(12,2))
    report_file = fields.Binary(readonly=True, string='Factura')

    @api.depends('idventa')
    def _idventa(self):
        for rec in self:
            rec.idventa = 'V-'+ str(rec.id)
    @api.depends('precioNeto')
    def _precioN(self):
        for rec in self:
            if rec.producto:
                for ventas in self.env['ventar'].search([]):
                    for ventas2 in rec.producto:
                        if ventas.idventa == ventas2.idventa:
                            rec.precioNeto += ventas.precioVenta2

    @api.depends('precioTotal')
    def _precioT(self):
        for rec in self:
                rec.precioTotal = rec.precioNeto * 1.21        

    def action_get_attachment(self):
            pdf = self.env.ref('TFG_Oscar.report_ventas_view')._render_qweb_pdf(self.ids)
            self.report_file = base64.b64encode(pdf[0])
            # save pdf as attachment
            name = "informe"
            return self.env['ir.attachment'].create({
                'name': name,
                'type': 'binary',
                'datas': self.report_file,
                'store_fname': name,
                'res_model': self._name,
                'res_id': self.id,
                'mimetype': 'application/x-pdf'
            })

