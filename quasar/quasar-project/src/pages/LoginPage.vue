<template>
  <q-page>
    <div id="q-app">
      <q-page class="window-height window-width row justify-center items-center" style="background-color: #b4b4b4">
        <div class="column q-pa-lg">
          <div class="row">
            <q-card square class="shadow-24" style="width: 400px; height: 540px">
              <q-card-section style="background-color: rgba(0, 0, 0, 0.7)">
                <h4 class="text-h5 text-white q-my-md">{{ title }}</h4>
              </q-card-section>
              <q-card-section>
                <q-fab color="primary" @click="switchTypeForm" icon="add" class="absolute"
                  style="top: 0; right: 12px; transform: translateY(-50%)">
                </q-fab>
                <q-form class="q-px-sm q-pt-xl">
                  <q-input ref="email" square clearable v-model="email" type="email" lazy-rules
                    :rules="[this.required, this.isEmail, this.short]" label="Email">
                    <template v-slot:prepend>
                      <q-icon name="email" />
                    </template>
                  </q-input>
                  <q-input ref="username" v-if="register" square clearable v-model="username" lazy-rules
                    :rules="[this.required, this.short]" type="username" label="Nombre de Usuario">
                    <template v-slot:prepend>
                      <q-icon name="person" />
                    </template>
                  </q-input>
                  <q-input ref="password" square clearable v-model="password" :type="passwordFieldType" lazy-rules
                    :rules="[this.required, this.short]" label="Contraseña">
                    <template v-slot:prepend>
                      <q-icon name="lock" />
                    </template>
                    <template v-slot:append>
                      <q-icon :name="visibilityIcon" @click="switchVisibility" class="cursor-pointer" />
                    </template>
                  </q-input>
                  <q-input ref="repassword" v-if="register" square clearable v-model="repassword"
                    :type="passwordFieldType" lazy-rules :rules="[this.required, this.short, this.diffPassword]"
                    label="Repetir Contraseña">
                    <template v-slot:prepend>
                      <q-icon name="lock" />
                    </template>
                    <template v-slot:append>
                      <q-icon :name="visibilityIcon" @click="switchVisibility" class="cursor-pointer" />
                    </template>
                  </q-input>
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
import { useQuasar } from "quasar"
export default {
  name: "PageLogin",
  setup() {
    const $q = useQuasar()
      },
  data() {
    return {
      title: "Iniciar Sesion",
      email: "",
      username: "",
      password: "",
      repassword: "",
      register: false,
      passwordFieldType: "password",
      btnLabel: "Iniciar Sesion",
      visibility: false,
      visibilityIcon: "visibility",
    };
  },
  methods: {
    required(val) {
      return (val && val.length > 0) || "El campo no puede estar vacio";
    },
    crearSesion(email) {
      const $q = useQuasar()
      $q.sessionStorage.set('email', email)
      console.log(email)
    },
    diffPassword(val) {
      const val2 = this.$refs.password.value;
      return (val && val === val2) || "La contraseña no coincide!";
    },
    isEmail(val) {
      const emailPattern =
        /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
      return (
        emailPattern.test(val) ||
        "Por favor introduzca una dirección de correo electrónico válida"
      );
    },
    submit() {
      if (this.register) {
        this.$refs.email.validate();
        this.$refs.username.validate();
        this.$refs.password.validate();
        this.$refs.repassword.validate();
      } else {
        this.$refs.email.validate();
        this.$refs.password.validate();
      }

      if (!this.register)
        if (
          !this.$refs.email.hasError &&
          !this.$refs.password.hasError &&
          this.password == "botin" && this.email == "botin@gmail.com") {
          console.log(this.password);
          this.crearSesion(this.email);
          this.$q.notify({
            icon: "done",
            color: "positive",
            message: "Inicio Sesion Correcto",
          });
          this.goTo(this.email)

        } else {
          this.$q.notify({
            icon: "done",
            color: "negative",
            message: "Inicio Sesion Incorrecto",
          });
        }
    },
    switchTypeForm() {
      this.register = !this.register;
      this.title = this.register ? "Registrarse" : "Iniciar Sesion";
      this.btnLabel = this.register ? "Registrarse" : "Iniciar Sesion";
    },
    switchVisibility() {
      this.visibility = !this.visibility;
      this.passwordFieldType = this.visibility ? "text" : "password";
      this.visibilityIcon = this.visibility ? "visibility_off" : "visibility";
    },
    goTo(email) {
      this.$router.push("/productos?email=" + email);
    },
  },
};
</script>
