<template>
  <q-page>
    <div class="row">
      <q-table
        @row-click="goTo"
        title="Proveedores"
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
  name: "ProveedoresPage",
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
          name: "direccion",
          label: "Direccion",
          align: "left",
          field: "direccion",
          sortable: true,
        },
        {
          name: "email",
          label: "Email",
          align: "left",
          field: "email",
          sortable: true,
        },
        {
          name: "tlfno",
          label: "Telefono",
          align: "left",
          field: "tlfno",
          sortable: true,
        },
        {
          name: "cif",
          label: "CIF ",
          align: "left",
          field: "cif",
          sortable: true,
        },
        {
          name: "img",
          label: "Imagen",
          align: "left",
          field: "img",
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
        .get("http://localhost:8069/gestion/cargamento/proveedores")
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
