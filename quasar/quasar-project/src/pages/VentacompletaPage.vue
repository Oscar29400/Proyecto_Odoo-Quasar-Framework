<template>
  <q-page>
    <div class="row">
      <q-table
        title="Ventas"
        :rows="rows"
        :columns="columns"
        row-key="name"
        class="col"
      >
        <template v-slot:body-cell-action="props">
          <q-td :props="props">
            <q-btn
              icon="ti-trash"
              color="negative"
              size="md"
              @click="deletePosts(props.row)"
              dense
            >
              <q-tooltip class="bg-black text-body2" :offset="[10, 10]"
                >Eliminar Campo</q-tooltip
              > </q-btn
            >&nbsp;
            <q-btn
              icon="ti-download"
              color="teal"
              size="md"
              :href="props.row.pdf"
              target="_blank"
              dense
            >
              <q-tooltip class="bg-black text-body2" :offset="[10, 10]"
                >Descargar Factura</q-tooltip
              >
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
  name: "VentacompletaPage",
  data() {
    return {
      columns: [
        {
          name: "idventa",
          label: "ID Venta",
          align: "left",
          field: "idventa",
          sortable: true,
        },
        {
          name: "idventasimple",
          label: "ID Cargamento",
          align: "left",
          field: "idventasimple",
          sortable: true,
        },
        {
          name: "producto",
          label: "Producto",
          align: "left",
          field: "producto",
          sortable: true,
        },
        {
          name: "cliente",
          label: "Cliente",
          align: "left",
          field: "cliente",
          sortable: true,
        },
        {
          name: "empleado",
          label: "Vendedor",
          align: "left",
          field: "empleado",
          sortable: true,
        },
        {
          name: "precioNeto",
          label: "Precio Neto",
          align: "left",
          field: "precioNeto",
          sortable: true,
        },
        {
          name: "precioTotal",
          label: "Precio Total",
          align: "left",
          field: "precioTotal",
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
          message: "Se ha eliminado la Venta con éxito",
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
        .get("http://localhost:8069/gestion/cargamento/ventacompleta")
        .then((res) => {
          this.rows = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(row) {
      this.$router.push("/venta/?id=" + row);
    },
    deletePosts(idPosts) {
      this.$axios
        .get(
          'http://localhost:8069/gestion/apirest/delete/ventacompleta?data={"id":"' +
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
      this.$axios.get(
        'http://localhost:8069/gestion/apirest/delete/venta?data={"id":"' +
          idPosts.idventasimple +
          '"}'
      );
      console.log(idPosts.id);
    },
  },
};
</script>
