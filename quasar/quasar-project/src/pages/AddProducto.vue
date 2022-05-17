<template>
  <q-page style="background-color: rgba(0, 0, 0, 0.68) !important">
    <section>
      <div
        class="full-height full-width flex flex-center text-center"
        style="height: 15vh !important"
      >
        <div class="">
          <div class="text-h3 text-white">Añadir Productos</div>
        </div>
      </div>
    </section>
    <section>
      <div>
        <div style="">
          <q-form @submit="submitForm">
            <div class="row text-center flex flex-center q-py-lg">
              <div
                class="col-md-6 col-lg-6 col-sx-12 col-sm-12 q-gutter-lg q-px-xl q-pb-none q-ma-none"
              >
                <q-input
                  required
                  v-model="formData.nombre"
                  name="name"
                  bg-color="white"
                  outlined
                  label="Nombre del Producto *"
                >
                  <template v-slot:append>
                    <q-icon name="list" style="color: darkcyan" />
                  </template>
                </q-input>

                <q-input
                  required
                  v-model="formData.precioCoste"
                  name="precioCoste"
                  bg-color="white"
                  outlined
                  label="Precio de Coste *"
                >
                  <template v-slot:append>
                    <q-icon name="ti-money" style="color: darkcyan" />
                  </template>
                </q-input>
              </div>
              <div
                class="col-md-6 col-lg-6 col-sx-12 col-sm-12 q-gutter-lg q-px-xl q-pb-none q-ma-none"
              >
                <q-input
                  required
                  v-model="formData.descripcion"
                  name="descripcion"
                  class=""
                  type="textarea"
                  bg-color="white"
                  outlined
                  label="Descripción *"
                >
                  <template v-slot:append>
                    <q-icon name="comment" style="color: darkcyan" />
                  </template>
                </q-input>
              </div>
            </div>
            <div class="row flex flex-center text-center q-pb-xl q-mt-md">
              <div class="col-md-12 col-lg-12 col-sx-12 col-sm-12">
                <q-btn
                  type="submit"
                  size="lg"
                  style="background: green; color: white"
                  label="Añadir Producto"
                />
              </div>
            </div>
          </q-form>
        </div>
      </div>
    </section>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";
export default  {
  name: "PageAbout",
  data() {
    return {
      formData: {
        nombre: null,
        descripcion: null,
        precioCoste: null
      }
    };
  },
  setup() {
    return {
    };
  },
  methods: {
    submitForm() {
      this.$axios
        .get(
          'http://localhost:8069/gestion/addProducto/'+this.nombre+'/'+this.descripcion+'/'+this.precioCoste
        )
        .then((response) => {
          console.log("Everything is awesome.");
        })


}

  }
};
</script>
