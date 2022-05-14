<template>
  <q-page>
    <div class="row">
      <q-table
        @row-click="goTo"
        title="Empleados"
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
  name: "ClientessPage",
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
          name: "apellidos",
          label: "Apellidos",
          align: "left",
          field: "apellidos",
          sortable: true,
        },
        {
          name: "seguridadSocial",
          label: "Nº Seguridad Social",
          align: "left",
          field: "seguridadSocial",
          sortable: true,
        },
        {
          name: "dni",
          label: "DNI",
          align: "left",
          field: "dni",
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
        .get("http://localhost:8069/gestion/cargamento/empleados")
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
