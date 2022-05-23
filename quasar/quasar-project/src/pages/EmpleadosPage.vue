<template>
  <q-page style="background-color: #b4b4b4; ">
    <div class="row">
      <q-table grid :rows="rows" :columns="columns" row-key="name" class="col" card-class="bg-grey-1 text-black">
        <template v-slot:item="props">
          <q-card
            bordered
            class="q-ma-sm tileBGColor"
            style="max-width: 400px; min-width: 300px"
          >
            <div class="q-ma-sm">
              <div class="text-h5">
                {{ props.row.nombre }} {{ props.row.apellidos }}
              </div>
              <div>
                <q-img :src="props.row.img" basic style="max-width: 300px;" />
              </div>
              <div></div>
              <div>
                <div class="row text-subtitle1">
                  <div class="column"><b>DNI: &nbsp;</b></div>
                  <div class="column">{{ props.row.dni }}</div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Seguridad Social: &nbsp;</b></div>
                  <div class="column">{{ props.row.seguridadSocial }}</div>
                </div>

              </div>
              <q-btn
                icon="ti-trash"
                color="negative"
                size="md"
                @click="deletePosts(props.row)"
                dense
              >
                <q-tooltip class="bg-black text-body2" :offset="[10, 10]"
                  >Eliminar Producto</q-tooltip
                > </q-btn
              >&nbsp;
              <q-btn
                icon="ti-info-alt"
                color="primary"
                size="md"
                @click="goTo(props.row.id)"
                dense
              >
                <q-tooltip class="bg-black text-body2" :offset="[10, 10]"
                  >Mas Información</q-tooltip
                >
              </q-btn>
            </div>
          </q-card>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { useQuasar } from "quasar";

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
            "Se ha eliminado el Empleado con éxito",
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
        .get("http://localhost:8069/gestion/cargamento/empleados")
        .then((res) => {
          this.rows = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(row) {
      this.$router.push("/empleado?id=" + row);
    },
    deletePosts(idPosts) {
      this.$axios
        .get(
          'http://localhost:8069/gestion/apirest/delete/empleados?data={"id":"' +
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
    },
  },
};
</script>
