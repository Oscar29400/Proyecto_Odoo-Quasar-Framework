
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'proveedores', component: () => import('pages/ProveedoresPage.vue') },
      { path: 'clientes', component: () => import('pages/ClientesPage.vue') },
      { path: 'empleados', component: () => import('pages/EmpleadosPage.vue') },
      { path: 'reparacion', component: () => import('pages/ReparacionPage.vue') },
      { path: 'ventacompleta', component: () => import('pages/VentacompletaPage.vue') },
      { path: 'compras', component: () => import('pages/ComprasPage.vue') },
      { path: 'producto', component: () => import('pages/ProductoPage.vue') },
      { path: 'venta', component: () => import('pages/VentaPage.vue') },
      { path: 'aboutus', component: () => import('pages/AboutPage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
