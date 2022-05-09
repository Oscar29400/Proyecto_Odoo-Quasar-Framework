<template>
  <q-page>
    <div class="row">
      <q-table
        @row-click="goTo"
        title="Compras"
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
  name: "ComprasPage",
  data() {
    return {
      columns: [
        {
          name: "idCompra",
          label: "ID Compra",
          align: "left",
          field: "idCompra",
          sortable: true,
        },
        {
          name: "productos",
          label: "Productos",
          align: "left",
          field: "productos",
          sortable: true,
        },
        {
          name: "precioCosteUnidad",
          label: "Precio Coste Unidad",
          align: "left",
          field: "precioCosteUnidad",
          sortable: true,
        },
        {
          name: "proveedor",
          label: "Proveedor",
          align: "left",
          field: "proveedor",
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
        .get("http://localhost:8069/gestion/cargamento/compras")
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
