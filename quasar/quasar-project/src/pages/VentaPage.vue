<template>
  <q-page style="background-color: rgba(0, 0, 0, 0.7)">
    <div
      class="col-md-12 col-md-12 col-xs-12 col-sm-12 q-mb-xl flex flex-center q-pt-xl"
      style="float:inherit"
    >
      <q-card class="my-card">
        <q-card-section>
          <div class="row">
            <div >
              <q-card-section class="q-py-xs">
                <div class="text-h5 q-mt-sm q-mb-xs">
                  <div style="text-decoration: none; color: black">
                    {{ idventa }}
                  </div>
                </div>

                  <ul v-for="field in producto">Productos
                    <li>{{ field }}</li>

                  </ul>
                <div class="text-overline text-black q-pa-xl">
                  <q-btn @click="goTo" class="q-mt-xl">
                    <q-icon name="ti-arrow-left" size="32px"
                  /></q-btn>
                </div>
              </q-card-section>
            </div>
            <div class="col-lg-6 col-md-6 col-xs-12 col-sm-12">
              <q-card-section class="col-5 flex flex-center">

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
import { useQuasar } from "quasar";
export default {
  name: "PageVenta",
  data() {
    return {
      idventa: [],
      cliente: [],
      empleado: [],
      precioTotal: [],
      precioNeto: [],
      producto: [],

    };
  },
  mounted() {
    this.sesion();
    this.getProductos();
  },
  setup() {
    return {};
  },
  methods: {
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
    getProductos() {
      this.$axios
        .get('http://localhost:8069/gestion/apirest/ventacompleta?data={"id":"' + this.$route.query.id +'"}')
        .then((res) => {
          (this.idventa = res.data.idventa),
            (this.cliente = res.data.cliente),
            (this.precioTotal = res.data.precioTotal),
            (this.precioNeto = res.data.precioNeto),
            (this.empleado = res.data.empleado),
            (this.producto = res.data.producto);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(event, row) {
      this.$router.push("/ventacompleta");
    },
  },
};
</script>
