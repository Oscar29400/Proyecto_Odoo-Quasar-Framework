# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
#Definimos el modelo de datos
class reparacion(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'reparacion'
    _description = 'Modelo de la lista de Reparacion'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="id"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    id = fields.Integer()
    idventa = fields.Char(string='ID Venta')
    empleado = fields.Many2one('empleados', string='Vendedor')
    cliente = fields.Many2one('clientes', string='Cliente')
    reparar = fields.Selection([('cat1','Cambiar Suelas'),
    ('cat2','Pintar Zapatos'),('cat3','Coser Pantalon'),('cat4','Coser Pantalon'),
    ('cat5','Reparacion Completa y Limpieza')]
    ,string='Tipo Reparación')
    precioRNeto = fields.Float(compute='_precioR',string='Precio Neto', digits=(12,2))
    precioRTotal = fields.Float( string='Precio Total', compute='_precioRT', digits=(12,2))
    report_file = fields.Binary()

    @api.depends('precioRNeto')
    def _precioR(self):
        for record in self:
             #Para cada registro
            if record.reparar == "cat1":
                record.precioRNeto = 8.20
            elif record.reparar == "cat2":
                record.precioRNeto = 12.40
            elif record.reparar == "cat3":
                record.precioRNeto = 15.50
            elif record.reparar == "cat4":
                record.precioRNeto = 2.40
            elif record.reparar == "cat5":
                record.precioRNeto = 35.50

    @api.depends('precioRTotal')
    def _precioRT(self):
        for rec in self:
                rec.precioRTotal = rec.precioRNeto * 1.21            

    def action_get_attachment(self):
            pdf = self.env.ref('TFG_Oscar.report_reparacion_view')._render_qweb_pdf(self.ids)
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