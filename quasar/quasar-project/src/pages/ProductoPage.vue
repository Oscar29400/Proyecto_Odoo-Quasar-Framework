<template>
  <q-page>
    <div class="q-pa-md q-gutter-sm">
      <q-card class="my-card">
      <h5>PRODUCTO:</h5>
      <q-img
      :src="url"
      style="height: 500px; max-width: 750px"
    />
    </q-card>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { ref } from 'vue'
export default {
  name: "PageProducto",
  data() {
    return {
      id: true,
      url: []
    };
  },
  mounted() {
    this.getProductos();
  },
  setup () {
    return {
      url: []
    }
  },
  methods: {
    getProductos() {
      this.$axios
        .get('http://localhost:8069/gestion/apirest/productos?data={"id":"1"}')
        .then((res) => {
          this.url = res.data.img
          console.log(this.url);

        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
