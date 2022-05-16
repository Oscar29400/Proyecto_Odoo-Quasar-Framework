<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="q-py-sm" style="background-color: rgba(0, 0, 0, 0.7)">
      <q-toolbar class="text-h4">
        <q-tabs v-model="selected_tab" shrink>
        <q-tab
        style>
        <q-img src="../assets/botin.png" style="max-width: 70%; max-height: 100%;"></q-img>
        </q-tab>
          <q-tab
            class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('')"
            style="width: 120px; min-height: auto !important; color: white"
            label="Productos"
          />
          <q-tab
            class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('compras')"
            style="width: 120px; min-height: auto !important; color: white"
            label="Compras"
          />
          <q-tab
            class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('ventacompleta')"
            style="width: 120px; min-height: auto !important; color: white"
            label="Ventas"
          />
          <q-tab
            class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('clientes')"
            style="width: 120px; min-height: auto !important; color: white"
            label="Clientes"
          />
          <q-tab
            class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('proveedores')"
            style="width: 120px; min-height: auto !important; color: white"
            label="Proveedores"
          />
          <q-tab
            class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('empleados')"
            style="width: 120px; min-height: auto !important; color: white"
            label="Empleados"
          />
          <q-tab
            class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('reparacion')"
            style="width: 120px; min-height: auto !important; color: white"
            label="Reparacion"
          />
        </q-tabs>
      </q-toolbar>
    </q-header>

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
  name: "MainLayout",
  components: {
    EssentialLink,
  },
  setup() {
    const leftDrawerOpen = ref(false);
    return {};
  },
  data() {
    return {
      selected_tab: "t_1",
    };
  },
  methods: {
    scrollToElement(id) {
      this.$router.push("/" + id);
    },
  },
});
</script>
