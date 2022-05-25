
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'productos', component: () => import('pages/IndexPage.vue') },
      { path: 'proveedores', component: () => import('pages/ProveedoresPage.vue') },
      { path: 'clientes', component: () => import('pages/ClientesPage.vue') },
      { path: 'empleados', component: () => import('pages/EmpleadosPage.vue') },
      { path: 'reparacion', component: () => import('pages/ReparacionPage.vue') },
      { path: 'ventacompleta', component: () => import('pages/VentacompletaPage.vue') },
      { path: 'compras', component: () => import('pages/ComprasPage.vue') },
      { path: 'producto', component: () => import('pages/ProductoPage.vue') },
      { path: 'cliente', component: () => import('pages/ClientePage.vue') },
      { path: 'proveedor', component: () => import('pages/ProveedorPage.vue') },
      { path: 'empleado', component: () => import('pages/EmpleadoPage.vue') },
      { path: 'venta', component: () => import('pages/VentaPage.vue') },
      { path: 'compra', component: () => import('pages/CompraPage.vue') },
      { path: 'facturas', component: () => import('pages/ClienteFacturaPage.vue') },
      { path: '', component: () => import('pages/LoginPage.vue') },
      { path: 'addProducto', component: () => import('pages/AddProducto.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it path: '', component: () => import('pages/LoginPage.vue')
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  },


]

export default routes
