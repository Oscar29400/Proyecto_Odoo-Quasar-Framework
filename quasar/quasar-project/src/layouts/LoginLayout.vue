<template>
  <q-layout view="lHh Lpr lFf">

    <q-page-container>
      <router-view />
    </q-page-container>
    <q-toolbar
      class="flex flex-center text-white"
      style="background-color: #1c1b21; border-top: 2px solid white"
      id="id_contact_me"
    >
      <div class="q-pa-sm q-gutter-sm">
        <q-btn
          target="_blank"
          style="border: 2px solid red"
          round
          type="a"
          href="http://localhost:8069/"
          glossy
          icon="ti-world"
          size="1.2rem"
        />
        &nbsp;
        <q-btn
          target="_blank"
          style="border: 2px solid red"
          round
          type="a"
          href="https://www.facebook.com/botinreparaciondecalzado"
          glossy
          icon="ti-facebook"
          size="1.2rem"
        />
        &nbsp;
        <q-btn
          style="border: 2px solid red"
          round
          type="a"
          href="mailto:botinreparar@gmail.com"
          glossy
          icon="ti-email"
          size="1.2rem"
        />
      </div>
    </q-toolbar>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";

export default defineComponent({
  name: "LoginLayout",
  components: {
    EssentialLink,
  },
  setup() {
    const leftDrawerOpen = ref(false);
    return {};
  },
});
</script>
