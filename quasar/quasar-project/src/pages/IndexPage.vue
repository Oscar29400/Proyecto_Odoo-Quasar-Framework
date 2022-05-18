<template>
  <q-page>
    <div class="row">
      <q-table dense title="Productos" :rows="rows" :columns="columns" row-key="id" class="col">
        <template v-slot:body-cell-img="props">
          <q-tr :props="props">
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
              <span v-if="col.name != 'img'">
                {{ col.value }}
              </span>
              <img :src="props.row.img" style="max-width: 100px" v-if="col.name == 'img'" size="100px" />
            </q-td>
          </q-tr>
        </template>
        <template v-slot:body-cell-action="props">
          <q-td :props="props">
            <q-btn icon="ti-trash" color="negative" size="md" @click="deletePosts(props.row)" dense>
              <q-tooltip class="bg-black text-body2" :offset="[10, 10]">Eliminar Producto</q-tooltip>
            </q-btn>&nbsp;
            <q-btn icon="ti-new-window" color="teal" size="md" @click="goTo(props.row.id)" dense>
              <q-tooltip class="bg-black text-body2" :offset="[10, 10]">Mas Información</q-tooltip>
            </q-btn>
          </q-td>
        </template>
      </q-table>
    </div>
    <div>{{ selected }}</div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { Notify } from "quasar";
import { useQuasar } from "quasar";

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
      url: [],
    };
  },
  mounted() {
    this.getProductos();
  },
  setup() {
    const $q = useQuasar();
    return {
      showNotif() {
        $q.notify({
          message:
            "<b>ERROR.</b><br> Estas intentando eliminar un Producto que se esta vendiendo todavia. <br> Elimina la Venta primero.",
          html: true,
          color: "red",
          progress: true,
          multiLine: true,
          actions: [
            {
              label: "Aceptar",
              color: "black",
              handler: () => {
                this.$router.push("/ventacompleta");
              },
            },
          ],
        });
      },
      showNotifGood() {
        $q.notify({
          message:
            "Has eliminado el Producto correctamente.",
          color: "primary",
          progress: true,
          multiLine: true,
          actions: [
            {
              label: "Aceptar",
              color: "yellow",
              handler: () => {
                /* ... */
              },
            },
          ],
        });
      },
    };
  },
  methods: {
    getProductos() {
      this.$axios
        .get("http://localhost:8069/gestion/cargamento/productos")
        .then((res) => {
          this.rows = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    goTo(row) {
      this.$router.push("/producto?id=" + row);
    },
    deletePosts(idPosts) {
      this.$axios
        .get(
          'http://localhost:8069/gestion/apirest/delete/productos?data={"id":"' +
          idPosts.id +
          '"}'
        )
        .then((response) => {
          console.log("Everything is awesome.");
          this.showNotifGood();
        })
        .catch((error) => {
          this.showNotif();

        });
    },
  },
};
</script>
