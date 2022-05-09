<template>
  <q-page>
    <div class="row">
      <q-table
        @row-click="goTo"
        title="Ventas"
        :rows="rows"
        :columns="columns"
        row-key="name"
        class="col"
      />
      <img :src="url">

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
          var image = new Image(200, 200);
          image.src = this.rows[0].img;
         image = this.rows[0].foto;

        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(event, row) {
      this.$router.push("/producto/" + row.id);
    },
  },
};
</script>
