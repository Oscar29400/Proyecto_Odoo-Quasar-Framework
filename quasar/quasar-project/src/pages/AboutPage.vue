<template>
  <q-page> </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";
import { useQuasar } from "quasar";

export default {
  name: "PageAbout",
  data() {
    return {};
  },
  methods: {
    sesion() {
      const $q = useQuasar();
      const sesion = $q.sessionStorage.getItem("email");
      console.log("Comprobando sesion: " + sesion);

      if (sesion === "undefined" || sesion === "" || sesion === null) {
        this.$router.push("/login");
        console.log("NO SE HA INICIADO SESION");
        // console.log('ESE USUARIO ' + otherValue)
      }
    },
  },
  mounted() {
    this.sesion();
  },
};
</script>
