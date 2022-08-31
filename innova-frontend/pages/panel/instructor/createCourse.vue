<template>
  <div class="container-md">
    <h3 class="mb-10">Creacion del Curso:</h3>

    <p>Titulo</p>
    <v-text-field label="Solo" v-model="request_data.title" solo></v-text-field>
    <p>Subtitulo</p>
    <v-text-field
      label="Solo"
      v-model="request_data.subtitle"
      solo
    ></v-text-field>

    <p>Descripcion</p>
    <v-textarea
      solo
      name="input-7-4"
      v-model="request_data.description"
      label="Solo textarea"
    ></v-textarea>

    <v-row>
      <v-col class="d-flex" cols="6" sm="2">
        <v-select
          :items="nivel"
          label="Nivel"
          v-model="request_data.level"
          solo
        ></v-select>
      </v-col>

      <v-col class="d-flex" cols="6" sm="2">
        <v-select
          :items="categoria"
          label="Categoria"
          solo
          v-model="request_data.category"
        ></v-select>
      </v-col>

      <v-col class="d-flex" cols="6" sm="2">
        <v-select
          :items="tipo_producto"
          label="Tipo de producto"
          solo
          v-model="request_data.tipo_producto"
        ></v-select>
      </v-col>
    </v-row>

    <p>Imagen del Curso</p>
    <div style="min-height: 4px">
      <v-progress-linear
        v-model="value"
        :active="show"
        :indeterminate="query"
        :query="true"
      ></v-progress-linear>
    </div>
    <input type="file" class="mt-5 mb-13" @change="previewFiles" multiple />
    <button class="layout-btn button-font button-m btn-w" @click="create_course" dark >Crear</button>
  </div>
</template>

<script>
import {path} from "@/api/conf_api";
export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {
      // propiedades del progress
      value: 0,
      query: false,
      show: true,
      interval: 0,

      nivel: ["Todos los niveles", "Basico", "Intermedio", "Avanzado"],
      categoria: [
        "Tegnologia",
        "Administracion",
        "Negocios",
        "Contabilidad",
        "Comunicacion",
      ],
      tipo_producto: ["Curso", "Programa Especializados"],
      request_data: {
        author: "",
        title: "",
        subtitle: "",
        description: "",
        level: "",
        category: "",
        tipo_producto: "",
        img_course: null,
      },
    };
  },
  methods: {
    previewFiles(event) {
      this.request_data.img_course = event.target.files[0];
    },
    async create_course() {
      let df = new FormData();

      df.append("title", this.request_data.title);
      df.append("author", this.request_data.author);
      df.append("img_course", this.request_data.img_course);

      df.append("subtitle", this.request_data.subtitle);
      df.append("description", this.request_data.description);
      df.append("level", this.request_data.level);

      df.append("category", this.request_data.category);
      df.append("tipo_producto", this.request_data.tipo_producto);

      let token = localStorage.getItem("token");
      this.$axios
        .request({
          method: "post",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/create-course/`,
          data: df
        })
        .then((response) => {
          console.log("creado con exito");
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
  },
  computed: {},
  mounted() {
    this.request_data.author = parseInt(localStorage.getItem("id_proffesor"));
    console.log(this.request_data.author);
  },
};
</script>

<style lang="scss" scoped>


.container-md {
  width: 80%;
  margin: 0 auto;
  margin-top: 90px;
  margin-bottom: 20px;
}


.container-element-btn {
  width: 100%;
}


.detail-img-desing {
  height: 200px;
  object-fit: cover;
  object-position: center;
}

.button-m:hover {
    background-color: #0e54bd;
}

.btn-w {
    max-width: 250px;
}

.btn-w100 {
  width: 100%;
}

.button-m {
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    background-color: #0D47A1;
    transition: background-color .35s ease-in-out,color .15s ease-in-out,border .15s ease-in-out;
    height: 48px;
    padding-left: 40px;
    padding-right: 40px;
    border-radius: 5px;
    color: #ffff;
}

.button-font {
  text-decoration: none;
  font-family: Gilroy,SF Pro Display,-apple-system,BlinkMacSystemFont,Roboto,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;
  font-weight: 700;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: .4px;
}

.dim-input-file {
  width: 1000px;
}
</style>
