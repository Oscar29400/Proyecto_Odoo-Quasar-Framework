<template>
  <q-page>
    <div class="row">
      <q-table
        dense

        title="Productos"
        :rows="rows"
        :columns="columns"
        row-key="id"
        class="col"
        selection="multiple"
        v-model:selected="selected"
      >
        <template v-slot:body-cell-action="props">
          <q-td><q-img :src="url" /></q-td>
          <q-td :props="props">
            <q-btn icon="ti-trash" color="negative" size="sm" @click="deletePosts(props.row)" dense/>
            <q-btn icon="ti-new-window" color="teal" size="sm" @click="goTo(props.row.id)" dense/>
          </q-td>
        </template>
      </q-table>
    </div>
    <div>{{ selected }}</div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
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
          name: "name",
          label: "Imagen",
          align: "left",
          field: "img",
          sortable: true,
        },
        {
          name: "action",
          label: "Action",
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
      selected: [],
      url: [],
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
          for (let i = 0; i < this.rows.length; i++) {
            this.url ="http://localhost:8069/web/image?model=productos&id=" +this.rows[i].id +"&field=img";
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(row) {
      this.$router.push("/producto?id=" + row);
    },
    deletePosts (idPosts) {
      this.$axios
        .delete('http://localhost:8069/gestion/apirest/productos?data={"id":"'+idPosts.id+'"}')
          console.log(idPosts);

    }
  },
};
</script>
