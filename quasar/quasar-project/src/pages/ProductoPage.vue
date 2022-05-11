<template>
  <q-page>
    <div
      class="col-md-12 col-md-12 col-xs-12 col-sm-12 q-mb-xl flex flex-center q-pt-xl"
    >
      <q-card class="my-card">
        <q-card-section>
          <div class="row">
            <div class="col-lg-6 col-md-6 col-xs-12 col-sm-12">
              <q-card-section class="q-py-xs">
                <div class="text-h5 q-mt-sm q-mb-xs">
                  <div style="text-decoration: none; color: black">
                    {{ nombre }}
                  </div>
                </div>
                <div class="text-body text-grey-9">{{descripcion}}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

                  <ul>
                    <li>Stock {{ cantidad }}</li>
                    <li>
                      Precio Coste <b>{{ precioCoste }} €</b>
                    </li>
                    <li>
                      Precio Venta <b>{{ precioVenta }} €</b>
                    </li>
                  </ul>
                </div>
                <div class="text-overline text-black q-pa-xl">
                  <q-btn @click="goTo" class="q-mt-xl">
                    <q-icon name="ti-arrow-left" size="32px"
                  /></q-btn>
                </div>
              </q-card-section>
            </div>
            <div class="col-lg-6 col-md-6 col-xs-12 col-sm-12">
              <q-card-section class="col-5 flex flex-center">
                <q-img
                  class="rounded-borders"
                  style="border: 1px solid darkgrey"
                  :src="url"
                />
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
  name: "PageProducto",
  data() {
    return {
      id: true,
      url: [],
      nombre: [],
      descripcion: [],
      precioVenta: [],
      cantidad: [],
      precioCoste: [],
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
        .get('http://localhost:8069/gestion/apirest/productos?data={"id":"1"}')
        .then((res) => {
          (this.url = res.data.img),
            (this.nombre = res.data.nombre),
            (this.precioCoste = res.data.precioCoste),
            (this.precioVenta = res.data.precioVenta),
            (this.cantidad = res.data.cantidad),
            (this.descripcion = res.data.descripcion);
          console.log(this.url);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(event, row) {
      this.$router.push("/");
    },
  },
};
</script>
