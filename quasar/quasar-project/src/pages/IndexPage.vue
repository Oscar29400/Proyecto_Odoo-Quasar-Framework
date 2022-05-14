<template>
  <q-page>
    <div class="row">
      <q-table dense title="Productos" :rows="rows" :columns="columns" row-key="id" class="col">

        <template v-slot:body-cell-img="props">
          <q-tr :props="props">
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
              <span v-if="col.name != 'img'">
                {{ col.value }}
              </span>
              <img :src="props.row.img" style="max-width:100px;" v-if="col.name == 'img'" size="100px">
            </q-td>
          </q-tr>
        </template>
        <template v-slot:body-cell-action="props">
          <q-td :props="props">
            <q-btn icon="ti-trash" color="negative" size="sm" @click="deletePosts(props.row)" dense />&nbsp;
            <q-btn icon="ti-new-window" color="teal" size="sm" @click="goTo(props.row.id)" dense />
          </q-td>
        </template>
      </q-table>
    </div>
    <div>{{ selected }}</div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { Notify } from 'quasar';
import { useQuasar } from 'quasar'

export default {
  name: "PageProductos",
  data() {
    return {
      columns: [
        {
          name: "id",
          label: "ID",
          align: "left",
          field: "id",
          sortable: true,
        },
        {
          name: "nombre",
          label: "Nombre",
          align: "left",
          field: "nombre",
          sortable: true,
        },
        {
          name: "descripcion",
          label: "Descripción",
          align: "left",
          field: "descripcion",
          sortable: true,
        },
        {
          name: "marca",
          label: "Marca",
          align: "left",
          field: "marca",
          sortable: true,
        },
        {
          name: "cantidad",
          label: "Cantidad",
          align: "left",
          field: "cantidad",
          sortable: true,
        },
        {
          name: "precioCoste",
          label: "Precio Coste",
          align: "left",
          field: "precioCoste",
          sortable: true,
        },
        {
          name: "precioVenta",
          label: "Precio Venta",
          align: "left",
          field: "precioVenta",
          sortable: true,
        },
        {
          name: "img",
          label: "Imagen",
          align: "left",
          sortable: true,
        },
        {
          name: "action",
          label: "Action",
          align: "left",
          sortable: true,
        },
      ],
      pagination: {
        descending: false,
        page: 1,
        rowsPerPage: 10,
      },
      rows: [],
      url: [],
    };
  },
  mounted() {
    this.getProductos();
  },
  setup() {
    const $q = useQuasar()
    return {
      showNotif() {
        $q.notify({
          message: 'Foreign Key ERROR.\n' +
            'Estas intentando modificar o eliminar un objeto que esta siendo usado por otro modelo en Odoo.',
          color: 'primary',
          progress: true,
          multiLine: true,
          actions: [
            { label: 'Aceptar', color: 'yellow', handler: () => { /* ... */ } }
          ]
        })
      }
    }
  },
  methods: {
    getProductos() {
      this.$axios
        .get("http://localhost:8069/gestion/cargamento/productos")
        .then((res) => {
          this.rows = res.data;
          for (let i = 0; i < this.rows.length; i++) {
            this.url = "http://localhost:8069/web/image?model=productos&id=" + this.rows[i].id + "&field=img";
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goTo(row) {
      this.$router.push("/producto?id=" + row);
    },
    deletePosts(idPosts) {
      this.$axios
        .get('http://localhost:8069/gestion/apirest/delete/productos?data={"id":"' + idPosts.id + '"}').then((response) => {
          console.log('Everything is awesome.');
        }).catch((error) => {
          console.warn('Not good man :(');
          this.showNotif();
        })
      console.log(idPosts.id);

    }
  },
};
</script>
