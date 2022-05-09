<template>
  <q-page>
    <div class="row">
      <q-table
        @row-click="goTo"
        title="Productos"
        :rows="rows"
        :columns="columns"
        row-key="name"
        class="col"
      />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
export default {
  name: "PageProductos",
  data() {
    return {
      columns: [
        {
          name: "id",
          label: "ID",
          align: "left",
          field: "id",
          sortable: true,
        },
        {
          name: "nombre",
          label: "Nombre",
          align: "left",
          field: "nombre",
          sortable: true,
        },
        {
          name: "descripcion",
          label: "Descripción",
          align: "left",
          field: "descripcion",
          sortable: true,
        },
        {
          name: "marca",
          label: "Marca",
          align: "left",
          field: "marca",
          sortable: true,
        },
        {
          name: "cantidad",
          label: "Cantidad",
          align: "left",
          field: "cantidad",
          sortable: true,
        },
        {
          name: "precioCoste",
          label: "Precio Coste",
          align: "left",
          field: "precioCoste",
          sortable: true,
        },
        {
          name: "precioVenta",
          label: "Precio Venta",
          align: "left",
          field: "precioVenta",
          sortable: true,
        },
        {
          name: "img",
          label: "Imagen",
          align: "left",
          field: "img",
          sortable: true,
        }
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
        .get("http://localhost:8069/gestion/cargamento/productos")
        .then((res) => {
          this.rows = res.data;
          var image = new Image(200, 200);
          image.src = this.rows[0].img;
          this.rows[0].foto = image;
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
