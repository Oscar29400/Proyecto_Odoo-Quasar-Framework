# -*- coding: utf-8 -*-
{
    'name': "Botín",

    'summary': """
    Gestionar y Administrar la empresa Botín""",

    'description': """
    Gestionar y Administrar los Pedidos
    """,

    'author': "Oscar Murciano",
    #Indicamos que es una aplicación
    'application': True,

    # En la siguiente URL se indica que categorias pueden usarse
    # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoria Productivity
    'category': 'Productivity',
    'version': '0.1',

    # Indicamos lista de modulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del modulo "base"
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
        #Este primero indica la politica de acceso del modulo
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas
        'views/empleados_views2.xml',
        'views/productos_views.xml',
        'views/compras_views.xml',
        'views/ventar_views.xml',
        'views/proveedores_views.xml',
        'views/clientes_views.xml',
        'views/venta_completa_views.xml',
        'views/reparacion_views.xml',
        'report/report_ventas_view.xml',
        'report/report_reparacion_view.xml',

    ]
}
