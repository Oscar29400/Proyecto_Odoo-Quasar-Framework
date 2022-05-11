<template>
  <q-page>
<section>
        <div class="full-height full-width flex flex-center text-center"
           style="background-color: rgba(0, 0, 0, 0.68) !important;z-index:0;height: 100vh !important;">
        <div class="">
          <div class="text-h5 text-grey-5">BIENVENIDO</div>
          <div class="text-h2 text-white q-py-sm q-my-md"
               style="border-top:3px solid #1595de;border-bottom: 3px solid #2faa64;">BOTÍN
          </div>
          <div class="text-h6" style="color: #f4b825;">
            REPARACIÓN DE CALZADO Y MARROQUINERIA
          </div>
          <div style="color: #1495de !important;" class="text-h4 q-mt-md text-grey-2 my-font">
          <q-img src="https://cdn.quasar.dev/img/parallax2.jpg"></q-img>
          </div>
        </div>
      </div>
      </section>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { ref } from 'vue'
export default {
  name: "PageAbout",
  data() {
    return {

    };
  },
  mounted() {
    this.getProductos();
  },
  setup () {
    return {
    }
  },
  methods: {
    getProductos() {
      this.$axios
        .get('http://localhost:8069/gestion/apirest/productos?data={"id":"1"}')
        .then((res) => {
          console.log(this.url);

        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
