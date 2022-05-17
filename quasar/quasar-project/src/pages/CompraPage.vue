<template>
  <q-page style="background-color: rgba(0, 0, 0, 0.7)">
    <div
      class="col-md-12 col-md-12 col-xs-12 col-sm-12 q-mb-xl flex flex-center q-pt-xl"
      style="float:inherit; "
    >
      <q-card class="my-card">
        <q-card-section>
          <div class="row">
            <div >
              <q-card-section class="q-py-xs">
                <div class="text-h5 q-mt-sm q-mb-xs">
                  <div style="text-decoration: none; color: black" class="text-h3">
                    ID Compra: {{ idcompra }}
                  </div>
                </div>
                <br>
                <div class="text-h6 text-grey-9" style="width: 900px; ">&nbsp;&nbsp; Producto: <b><a :href="url">{{ productos}}</a></b>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                Precio Coste Unidad: <b>{{precioCosteUnidad}}</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                Cantidad: <b>{{cantidad}}</b><br><br>&nbsp;&nbsp;&nbsp;Proveedor: <b><a :href="urlp">{{proveedor}}</a></b>
                </div>
                <div class="text-overline text-black q-pa-xl">
                  <q-btn @click="goTo" class="q-mt-xl">
                    <q-icon name="ti-arrow-left" size="32px"
                  /></q-btn>
                </div>
              </q-card-section>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";
export default {
  name: "PageVenta",
  data() {
    return {
      idcompra: [],
      proveedor: [],
      productos: [],
      precioCosteUnidad: [],
      cantidad: [],
      url: [] ,
      urlp:[]
    };
  },
  mounted() {
    this.getProductos();
  },
  setup() {
    return {};
  },
  methods: {
    getProductos() {
      this.$axios
        .get('http://localhost:8069/gestion/apirest/compras?data={"id":"' + this.$route.query.id +'"}')
        .then((res) => {
            (this.idcompra = res.data.idCompra),
            (this.proveedor = res.data.proveedor),
            (this.productos = res.data.productos),
            (this.idprod = res.data.idprod),
            (this.idproveedor = res.data.idproveedor),
            (this.precioCosteUnidad = res.data.precioCosteUnidad.toFixed(2)),
            (this.cantidad = res.data.cantidad);
            this.url = "http://localhost:8080/#/producto?id="+ res.data.idprod
            this.urlp = "http://localhost:8080/#/proveedor?id="+ res.data.idproveedor
          console.log(this.url);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(event, row) {
      this.$router.push("/compras");
    },
  },
};
</script>
