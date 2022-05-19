<template>
  <q-page style="background-color: #b4b4b4">
    <section>
      <div
        class="full-height full-width flex flex-center text-center q-pt-xl"
        style="height: 15vh !important"
      >
        <div
          style="border-top: 3px solid black; border-bottom: 3px solid black"
        >
          <div class="text-h3 text-black q-pa-md">Añadir Productos</div>
        </div>
      </div>
    </section>
    <section>
      <div>
        <div
          style="border-top: 3px solid black; border-bottom: 3px solid black"
          class="q-ma-xl"
        >
          <q-form @submit="submitForm">
            <div class="row text-center flex flex-center q-py-lg">
              <div
                class="col-md-6 col-lg-6 col-sx-12 col-sm-12 q-gutter-lg q-px-xl q-pb-none q-ma-none"
              >
                <q-input
                  required
                  v-model="formData.nombre"
                  name="name"
                  color="black"
                  bg-color="grey-3"
                  label-color="black"
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
                  color="black"
                  bg-color="grey-3"
                  label-color="black"
                  outlined
                  label="Precio de Coste *"
                  mask="#.##"
                  fill-mask="0"
                  reverse-fill-mask
                  input-class="text-right"
                >
                  <template v-slot:append>
                    <q-icon name="ti-money" style="color: darkcyan" />
                  </template>
                </q-input>
                <q-input
                  required
                  v-model="formData.cantidad"
                  name="cantidad"
                  type="number"
                  color="black"
                  bg-color="grey-3"
                  label-color="black"
                  outlined
                  label="Cantidad *"
                  input-class="text-right"
                >
                  <template v-slot:append>
                    <q-icon name="ti-package" style="color: darkcyan" />
                  </template>
                </q-input>
              </div>
              <div
                class="col-md-6 col-lg-6 col-sx-12 col-sm-12 q-gutter-lg q-px-xl q-pt-sm q-mt-sm"
              >
                <q-input
                   v-model="formData.imagen"
                  name="imagen"
                  type="file"
                  color="black"
                  bg-color="grey-3"
                  label-color="black"
                  outlined
                  label="Imagen"
                  input-class="text-right"
                >
                  <template v-slot:append>
                    <q-icon name="comment" style="color: darkcyan" />
                  </template>
                </q-input>

                <q-input
                  v-model="formData.descripcion"
                  name="descripcion"
                  class=""
                  type="textarea"
                  color="black"
                  bg-color="grey-3"
                  label-color="black"
                  outlined
                  label="Descripción"
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
                  style="background: grey; color: black"
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
import { useQuasar } from "quasar";

export default {
  name: "PageAbout",
  data() {
    return {
      formData: {
        nombre: "",
        descripcion: "",
        precioCoste: "",
        cantidad: null,
        file: null,
      },
    };
  },
  setup() {
    const $q = useQuasar();
    return {
      file: ref(null),
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
          message: "Se ha añadido el producto con exito.",
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
    submitForm() {
      console.log(this.formData.file)
      this.$axios
        .get(
          "http://localhost:8069/gestion/addProducto/" +
            this.formData.nombre +
            "/" +
            this.formData.descripcion +
            "/" +
            this.formData.precioCoste +
            "/" +
            this.formData.cantidad +
            "/" +
            this.formData.imagen
        )
        .then((response) => {
          console.log("Everything is awesome.");
          this.showNotifGood();
        })
        .catch((error) => {
          console.warn("Not good man :(");
          this.showNotif();
        });
    },
  },
};
</script>
