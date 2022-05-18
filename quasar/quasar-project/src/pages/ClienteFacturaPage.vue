<template>
  <q-page style="background-color: rgba(0, 0, 0, 0.7)">
    <div
      class="col-md-12 col-md-12 col-xs-12 col-sm-12 q-mb-xl flex flex-center q-pt-xl"
      style="float: inherit"
    >
      <q-table
        dense
        title="Facturas"
        :rows="rows"
        :columns="columns"
        row-key="id"
        class="col"
      >
        <template v-slot:body-cell-action="props">
          <q-td :props="props">
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
    <div class="text-overline text-black q-pa-xl">
      <q-btn @click="goTo" class="q-mt-xl" style="background-color: white;">
        <q-icon name="ti-arrow-left" size="32px"
      /></q-btn>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";
export default {
  name: "PageFacturas",
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
          name: "cliente",
          label: "Nombre",
          align: "left",
          field: "cliente",
          sortable: true,
        },
        {
          name: "action",
          label: "Factura",
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
    return {};
  },
  methods: {
    getProductos() {
      this.$axios
        .get(
          'http://localhost:8069/gestion/apirest/facturas?data={"cliente":"' +
            this.$route.query.id +
            '"}'
        )
        .then((res) => {
          this.rows = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(event, row) {
      this.$router.push("/clientes");
    },
  },
};
</script>
