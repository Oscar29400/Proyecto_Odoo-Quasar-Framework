<template>
  <q-page style="background-color: rgba(0, 0, 0, 0.7)">
    <div
      class="col-md-12 col-md-12 col-xs-12 col-sm-12 q-mb-xl flex flex-center q-pt-xl"
      style="float:inherit"
    >
      <q-card class="my-card">
        <q-card-section>
          <div class="row">
            <div class="col-lg-6 col-md-6 col-xs-12 col-sm-12">
              <q-card-section class="q-py-xs">
                <div class="text-h5 q-mt-sm q-mb-xs">
                  <div style="text-decoration: none; color: black" class="text-h3">
                    {{ id }}
                  </div>
                </div>
                <br>
                <div class="text-h6 text-grey-9"> Clienteeeee: <b>{{ cliente}}</b>
                </div>
                <div class="text-overline text-black q-pa-xl">
                  <q-btn @click="goTo" class="q-mt-xl">
                    <q-icon name="ti-arrow-left" size="32px"
                  /></q-btn>
                </div>
              </q-card-section>
            </div>
          </div>
        </q-card-section>
      </q-card>
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
      id: [],
      cliente: [],
      pdf: [],
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
        .get('http://localhost:8069/gestion/apirest/facturas')
        .then((res) => {
            (this.id = res.data.id),
            (this.cliente = res.data.cliente);
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