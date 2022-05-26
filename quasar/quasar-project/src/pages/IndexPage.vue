<template>
  <q-page style="background-color: #b4b4b4">
    <div class="row">
      <q-table
        :rows="rows"
        :columns="columns"
        row-key="id"
        class="col"
        card-class="bg-grey-1 text-black"
        grid
      >
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
                <q-img :src="props.row.img" basic style="max-height: 250px"/>
              </div>
              <div></div>
              <div>
                <div class="row text-body1">
                  <div class="column"><br>{{ props.row.descripcion }}</div>
                </div>
                <br />
              </div>
              <div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Proveedor: &nbsp;</b></div>
                  <div class="column">{{ props.row.marca }}</div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Precio de Coste: &nbsp;</b></div>
                  <div class="column">{{ props.row.precioCoste }} €</div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Precio de Venta: &nbsp;</b></div>
                  <div class="column">{{ props.row.precioVenta }} €</div>
                </div>
                <div class="row text-subtitle1">
                  <div class="column"><b>Cantidad: &nbsp;</b></div>
                  <div class="column">{{ props.row.cantidad }}</div>
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
    this.sesion();
    console.log("srgrdhthg")
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
          message: "Has eliminado el Producto correctamente.",
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
    sesion() {
      const $q = useQuasar()
      const sesion = $q.sessionStorage.getItem('email')
      console.log('Comprobando sesion: ' + sesion)

      if (sesion === 'undefined' || sesion === '' || sesion === null) {
        document.location.href = 'http://localhost:8080/#/login'
        console.log('NO SE HA INICIADO SESION')
        // console.log('ESE USUARIO ' + otherValue)
      }
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
