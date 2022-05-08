<template>
  <q-page>
    <div class="row">
      
    </div>
  </q-page>

</template>

<script>
import { defineComponent } from 'vue'

export default {
  name: "PageProductos",
  data() {
    return {
      
    };
  },
  mounted() {
    this.getProductos();
  },
  methods: {
    getProductos() {
      this.$axios
        .get("http://localhost:8069/gestion/cargamento/productos")
        .then((res) => {
          this.rows = res.data;
          var image = new Image(200, 200);
          image.src = this.rows[0].img;
          this.rows[0].foto = image;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(event, row) {
      this.$router.push("/producto/" + row.id);
    },
  },
};
</script>
