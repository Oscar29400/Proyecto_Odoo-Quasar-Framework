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
                    {{ nombre }} {{apellidos}}
                  </div>
                </div>
                <br>
                <div class="text-h6 text-grey-9"> DNI: <b>{{ dni}}</b><br> Nº Seguridad Social: <b>{{seguridadSocial}}</b>
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
                  style="border: 1px solid darkgrey; max-width:500px; min-width: 250px;"
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
import { useQuasar } from "quasar";
export default {
  name: "PageVenta",
  data() {
    return {
      id: [],
      url: [],
      nombre: [],
      dni: [],
      apellidos: [],
      seguridadSocial: [],
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
        this.$router.push("/login");
        console.log('NO SE HA INICIADO SESION')
        // console.log('ESE USUARIO ' + otherValue)
      }
    },
    getProductos() {
      this.$axios
        .get('http://localhost:8069/gestion/apirest/empleados?data={"id":"' + this.$route.query.id +'"}')
        .then((res) => {
            (this.nombre = res.data.nombre),
            (this.id = res.data.id),
            (this.apellidos = res.data.apellidos),
            (this.seguridadSocial = res.data.seguridadSocial),
            (this.dni = res.data.dni),
            (this.url = res.data.img),
          console.log(this.url);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(event, row) {
      this.$router.push("/empleados");
    },
  },
};
</script>
