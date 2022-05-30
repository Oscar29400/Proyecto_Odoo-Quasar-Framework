<template>
  <q-page style="background-color: #b4b4b4; ">
    <div class="row">
      <q-table grid :rows="rows" :columns="columns" row-key="name" class="col">
        <template v-slot:item="props">
          <q-card
            bordered
            class="q-ma-sm tileBGColor"
            style="max-width: 400px; min-width: 300px"
          >
            <div class="q-ma-sm">
              <div class="text-h5">
                {{ props.row.nombre }}
              </div>
              <div>
                <q-img :src="props.row.img" basic style="max-height: 250px;" />
              </div>
              <div></div>
              <div>
                <div class="row text-subtitle1">
                  <div class="column"><b>CIF: &nbsp;</b></div>
                  <div class="column">{{ props.row.cif }}</div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Direccion: &nbsp;</b></div>
                  <div class="column">{{ props.row.direccion }} </div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Ciudad: &nbsp;</b></div>
                  <div class="column">{{ props.row.ciudad }} </div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Email: &nbsp;</b></div>
                  <div class="column">{{ props.row.email }}</div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Telefono: &nbsp;</b></div>
                  <div class="column">{{ props.row.tlfno }}</div>
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
    this.sesion();
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
    sesion() {
      const $q = useQuasar()
      const sesion = $q.sessionStorage.getItem('email')
      console.log('Comprobando sesion: ' + sesion)

      if (sesion === 'undefined' || sesion === '' || sesion === null) {
        this.$router.push("/login");
        console.log('NO SE HA INICIADO SESION')
        // console.log('ESE USUARIO ' + otherValue)
      }
    },
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
