<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="text-h4">
        <q-tabs v-model="selected_tab" shrink>
          <q-tab :style="[selected_tab == 't_0' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('')" style="width:120px;min-height:auto !important;color: white"
            label="Productos" />
          <q-tab :style="[selected_tab == 't_1' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('compras')" style="width:120px;min-height:auto !important;color: white"
            label="Compras" />
          <q-tab :style="[selected_tab == 't_2' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('ventacompleta')" style="width:120px;min-height:auto !important;color: white"
            label="Ventas" />
          <q-tab :style="[selected_tab == 't_3' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('clientes')" style="width:120px;min-height:auto !important;color: white"
            label="Clientes" />
          <q-tab :style="[selected_tab == 't_4' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('proveedores')" style="width:120px;min-height:auto !important;color: white"
            label="Proveedores" />
          <q-tab :style="[selected_tab == 't_4' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('empleados')" style="width:120px;min-height:auto !important;color: white"
            label="Empleados" />
          <q-tab :style="[selected_tab == 't_4' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('reparacion')" style="width:120px;min-height:auto !important;color: white"
            label="Reparacion" />
          <q-tab :style="[selected_tab == 't_4' ? { backgroundColor: 'green' } : {}]" class="q-mr-sm q-py-xs custom_tab"
            @click="scrollToElement('aboutus')" style="width:120px;min-height:auto !important;color: white"
            label="Sobre Nosotros" />
        </q-tabs>
      </q-toolbar>
      
    </q-header>



    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
const linksList = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
]
export default defineComponent({
  name: 'MainLayout',
  components: {
    EssentialLink
  },
  setup() {
    const leftDrawerOpen = ref(false)
    return {

    }
  },
  methods: {
    scrollToElement(id) {
      this.$router.push("/" + id);
    }
  },
})
</script>
