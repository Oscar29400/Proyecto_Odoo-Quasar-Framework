<template>
  <q-page>
    <div class="row">
      <q-table title="Ventas" :rows="rows" :columns="columns" row-key="name" class="col">
        <template v-slot:body-cell-action="props">
          <q-td :props="props">
            <q-btn icon="ti-trash" color="negative" size="sm" @click="deletePosts(props.row)" dense />&nbsp;
            <q-btn icon="ti-new-window" color="teal" size="sm" @click="goTo(props.row.id)" dense />
          </q-td>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
export default {
  name: "VentacompletaPage",
  data() {
    return {
      columns: [
        {
          name: "idventa",
          label: "ID Venta",
          align: "left",
          field: "idventa",
          sortable: true,
        },
        {
          name: "producto",
          label: "Producto",
          align: "left",
          field: "producto",
          sortable: true,
        },
        {
          name: "cliente",
          label: "Cliente",
          align: "left",
          field: "cliente",
          sortable: true,
        },
        {
          name: "empleado",
          label: "Vendedor",
          align: "left",
          field: "empleado",
          sortable: true,
        },
        {
          name: "precioNeto",
          label: "Precio Neto",
          align: "left",
          field: "precioNeto",
          sortable: true,
        },
        {
          name: "precioTotal",
          label: "Precio Total",
          align: "left",
          field: "precioTotal",
          sortable: true,
        },
        {
          name: "action",
          label: "Precio Acciones",
          align: "left",
          sortable: true,
        },
      ],
      pagination: {
        descending: false,
        page: 1,
        rowsPerPage: 10,
      },
      rows: [],
    };
  },
  mounted() {
    this.getProductos();
  },
  methods: {
    getProductos() {
      this.$axios
        .get("http://localhost:8069/gestion/cargamento/ventacompleta")
        .then((res) => {
          this.rows = res.data;


        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(row) {
      this.$router.push("/venta/?id=" + row);
    },
  },
};
</script>
