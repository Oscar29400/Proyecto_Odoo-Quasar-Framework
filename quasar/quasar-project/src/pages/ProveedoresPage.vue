<template>
  <q-page style="background-color: #b4b4b4; ">
    <div class="row">
      <q-table title="Proveedores" :rows="rows" :columns="columns" row-key="name" class="col">
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
              <q-tooltip class="bg-black text-body2" :offset="[10, 10]">Eliminar Proveedor</q-tooltip>
            </q-btn>&nbsp;
            <q-btn icon="ti-info-alt" color="primary" size="md" @click="goTo(props.row.id)" dense>
              <q-tooltip class="bg-black text-body2" :offset="[10, 10]">Mas Información</q-tooltip>
            </q-btn>
          </q-td>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { useQuasar } from "quasar";

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
        {
          name: "action",
          label: "Acciones",
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
  setup() {
    const $q = useQuasar();
    return {
      showNotif() {
        $q.notify({
          message:
            "Foreign Key ERROR.\n" +
            "Estas intentando modificar o eliminar un objeto que esta siendo usado por otro modelo en Odoo.",
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
      showNotifGood() {
        $q.notify({
          message:
            "Se ha eliminado el Proveedor con éxito",
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
        .get("http://localhost:8069/gestion/cargamento/proveedores")
        .then((res) => {
          this.rows = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deletePosts(idPosts) {
      this.$axios
        .get(
          'http://localhost:8069/gestion/apirest/delete/proveedores?data={"id":"' +
          idPosts.id +
          '"}'
        )
        .then((response) => {
          console.log("Everything is awesome.");
          this.showNotifGood();
        })
        .catch((error) => {
          console.warn("Not good man :(");
          this.showNotif();
        });
      console.log(idPosts.id);
    },
    goTo(row) {
      this.$router.push("/proveedor?id=" + row);
    },
  },
};
</script>
