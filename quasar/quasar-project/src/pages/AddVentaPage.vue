<template>
  <q-page>
    <div id="q-app">
      <q-page class="window-height window-width row justify-center items-center" style="background-color: #b4b4b4">
        <div class="column q-pa-md">
          <div class="row">
            <q-card square class="shadow-24" style="width: 400px; height: 500px">
              <q-card-section style="background-color: rgba(0, 0, 0, 0.7)">
                <h4 class="text-h5 text-white q-my-md">{{ title }}</h4>
              </q-card-section>
              <q-card-section>
                <q-form class="q-px-sm q-pt-xl">
                  <q-select ref="producto" v-model="producto" :options="productos" label="Producto" lazy-rules
                    :rules="[this.required]" square input-class="text-right" emit-value map-options>
                    <option v-for="c in producto" :value="producto">
                      {{ c.nombre }}
                    </option>
                    <template v-slot:prepend>
                      <q-icon name="ti-package" />
                    </template>
                  </q-select>
                  <q-input v-model="cantidad" type="number" lazy-rules :rules="[this.required]" square
                    input-class="text-right" emit-value map-options label="Cantidad" />

                </q-form>
              </q-card-section>

              <q-card-actions class="q-px-lg">
                <q-btn unelevated size="lg" color="red" @click="submit" class="full-width text-white"
                  :label="btnLabel" />
              </q-card-actions>
            </q-card>
          </div>
        </div>
      </q-page>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";
import { useQuasar } from "quasar";

export default {
  name: "AddVenta",
  setup() {
    const $q = useQuasar();
    return {
      showNotif() {
        $q.notify({
          message:
            "<b>ERROR.</b><br> Estas intentando realizar una Venta de un producto que no tiene existencias.",
          html: true,
          color: "red",
          progress: true,
          multiLine: true,
          actions: [
            {
              label: "Aceptar",
              color: "black",
              handler: () => {
                this.$router.push("/addVenta");
              },
            },
          ],
        });
      },
      showNotifGood() {
        $q.notify({
          message: "Has añadido la Venta correctamente.",
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
  data() {
    return {
      title: "Añadir Venta",
      cantidad: 0,
      producto:"",
      productos: [],
      idproductos: [],
      btnLabel: "Añadir Venta",
      diccionarioclientes: {},
    };
  },
  mounted() {
    this.getProductos();
  },
  methods: {
    required(val) {
      return (val && val.length > 0) || "El campo no puede estar vacio";
    },
    submit() {
      var cli = 0;
      for (let i in this.diccionarioclientes) {
        if (this.diccionarioclientes[i] == this.producto) {
          console.log(this.diccionarioclientes[i]);
          var cli = i;
        }
      }
      this.addReparacion(cli);
    },
    getProductos() {
      this.$axios
        .get("http://localhost:8069/gestion/cargamento/productos")
        .then((res) => {
          var dict = {};
          for (var i = 0; i < res.data.length; i++) {
            this.productos.push(res.data[i].nombre);
            this.idproductos.push(res.data[i].nombre);
            dict[res.data[i].id] = res.data[i].nombre;
          }
          this.diccionarioclientes = dict;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addReparacion(cli) {
      this.$axios
        .get(
          "http://localhost:8069/gestion/addventa/" +
          cli +
          "/" +
          this.cantidad
        )
        .then((res) => {
          this.showNotifGood();

        })
        .catch((err) => {
          console.log(err);
          this.showNotif();

        });
    },
    goTo() {
      this.$router.push("/productos");
    },
  },
};
</script>
