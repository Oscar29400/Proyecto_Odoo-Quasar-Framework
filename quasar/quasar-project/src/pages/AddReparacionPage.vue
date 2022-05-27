<template>
  <q-page>
    <div id="q-app">
      <q-page class="window-height window-width row justify-center items-center" style="background-color: #b4b4b4">
        <div class="column q-pa-md">
          <div class="row">
            <q-card square class="shadow-24" style="width: 400px; height: 570px">
              <q-card-section style="background-color: rgba(0, 0, 0, 0.7)">
                <h4 class="text-h5 text-white q-my-md">{{ title }}</h4>
              </q-card-section>
              <q-card-section>
                <q-form class="q-px-sm q-pt-xl">
                  <q-select ref="tipo" v-model="tipo" :options="options" label="Tipo de Reparación" lazy-rules
                    :rules="[this.required]" square input-class="text-right">
                    <template v-slot:prepend>
                      <q-icon name="ti-list" />
                    </template>
                  </q-select>

                  <q-input ref="fecha" square clearable v-model="fecha" lazy-rules :rules="[this.required]" type="date"
                    label="Fecha entrega" input-class="text-right">
                    <template v-slot:prepend>
                      <q-icon name="ti-calendar" />
                    </template>
                  </q-input>
                  <q-select ref="cliente" v-model="cliente" :options="clientela" label="Cliente" lazy-rules
                    :rules="[this.required]" square input-class="text-right" emit-value map-options>
                    <option v-for="c in cliente" :value="cliente">
                      {{ c.nombre }}
                    </option>
                    <template v-slot:prepend>
                      <q-icon name="ti-user" />
                    </template>
                  </q-select>

                  <q-select ref="empleado" v-model="empleado" :options="empleados" label="Vendedor" lazy-rules
                    :rules="[this.required]" square input-class="text-right" emit-value map-options>
                    <option v-for="e in empleado" :value="empleado">
                      {{ e.nombre }}
                    </option>
                    <template v-slot:prepend>
                      <q-icon name="ti-user" />
                    </template>
                  </q-select>
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
  name: "PageAbout",
  setup() {
    const $q = useQuasar();
    return {
      options: [
        "Cambiar Suelas",
        "Pintar Zapatos",
        "Coser Pantalon",
        "Limpieza Zapatos",
        "Reparacion Completa y Limpieza",
      ],
      showNotif() {
        $q.notify({
          message:
            "<b>ERROR.</b><br> Estas intentando añadir una Reparación en una fecha anterior a hoy.",
          html: true,
          color: "red",
          progress: true,
          multiLine: true,
          actions: [
            {
              label: "Aceptar",
              color: "black",
              handler: () => {
                this.$router.push("/addReparacion");
              },
            },
          ],
        });
      },
      showNotifGood() {
        $q.notify({
          message: "Has añadido la Reparación correctamente.",
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
      title: "Añadir Reparación",
      tipo: "",
      fecha: "",
      cliente: "",
      empleado: "",
      clientela: [],
      idclientela: [],
      empleados: [],
      idempleados: [],
      btnLabel: "Añadir Reparación",
      diccionario: {},
      diccionarioclientes: {},
    };
  },
  mounted() {
    this.sesion();
    this.getClientes();
    this.getEmpleados();
  },
  methods: {
    required(val) {
      return (val && val.length > 0) || "El campo no puede estar vacio";
    },
    submit() {
      console.log(this.cliente);
      var emp = 0;
      for (let i in this.diccionario) {
        console.log(this.diccionario[i]);
        if (this.diccionario[i] == this.empleado) {
          console.log(this.diccionario[i]);
          var emp = i;
        }
      }
      var cli = 0;
      for (let i in this.diccionarioclientes) {
        console.log(this.diccionarioclientes[i]);
        if (this.diccionarioclientes[i] == this.cliente) {
          console.log(this.diccionarioclientes[i]);
          var cli = i;
        }
      }
      this.addReparacion(emp, cli);
    },
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
    getClientes() {
      this.$axios
        .get("http://localhost:8069/gestion/cargamento/clientes")
        .then((res) => {
          var dict = {};
          for (var i = 0; i < res.data.length; i++) {
            this.clientela.push(res.data[i].nombre);
            this.idclientela.push(res.data[i].nombre);
            dict[res.data[i].id] = res.data[i].nombre;
          }
          this.diccionarioclientes = dict;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getEmpleados() {
      this.$axios
        .get("http://localhost:8069/gestion/cargamento/empleados")
        .then((res) => {
          var dict = {};
          for (var i = 0; i < res.data.length; i++) {
            this.empleados.push(res.data[i].nombre);
            this.idempleados.push(res.data[i].id);
            dict[res.data[i].id] = res.data[i].nombre;
          }
          this.diccionario = dict;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addReparacion(emp, cli) {
      this.$axios
        .get(
          "http://localhost:8069/gestion/addReparacion/" +
          this.tipo +
          "/Recién entregado/" +
          emp + "/" + cli + "/" + this.fecha
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
