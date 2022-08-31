<template>
  <div class="container-md">
    <h1>Configuracion</h1>

    <p>Actualizar la informacion del profesor:</p>
    <v-textarea
      solo
      name="input-7-4"
      v-model="request_proffesor.resumen"
      label="Solo textarea"
      class="mt-10"
    ></v-textarea>

    <p>Descripcion</p>
    <v-textarea
      solo
      v-model="request_proffesor.description"
      name="input-7-4"
      label="Solo textarea"
      class="mt-10"
    ></v-textarea>
    <v-btn color="primary" @click="updateProffesor" dark> Actualizar </v-btn>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";
export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {
      request_proffesor: {
        user: "",
        resumen: "",
        description: "",
      },
    };
  },
  methods: {
    async get_proffesor_info() {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/account/infoProffesor/`,
        })
        .then((result) => {
          this.request_proffesor = result.data;
          console.log(this.request_proffesor);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    async updateProffesor() {
      let formData = {
        user: this.request_proffesor.user,
        resumen: this.request_proffesor.resumen,
        description: this.request_proffesor.description,
      };
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "put",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/account/update_proffesor/`,
          data: formData,
        })
        .then((result) => {
          this.request_proffesor = result.data;
          console.log(this.request_user);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
  },
  computed: {},
  mounted() {
    this.get_proffesor_info();
  },
};
</script>

<style lang="scss" scoped>
.container-md {
  width: 80%;
  margin: 0 auto;
  max-width: 1000px;
  margin-top: 60px;
}
</style>
