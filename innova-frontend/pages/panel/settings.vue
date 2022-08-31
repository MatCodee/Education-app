<template>
  <div class="container-md">
    <h3>Actualizar la informacion: </h3>
    <v-text-field
      v-model="request_user.username"
      label="Nombre de usuario"
      persistent-hint
      solo
    ></v-text-field>
    <v-text-field
      v-model="request_user.fullname"
      label="Nombre completo"
      persistent-hint
      solo
    ></v-text-field>
    <v-text-field
      v-model="request_user.email"
      label="Email"
      persistent-hint
      solo
    ></v-text-field>

    <p class="mt-5">Imagen de usuario: </p>
    <input type="file" @change="documentFile" class="mb-13" multiple />

    <v-btn block color="primary" @click="updateProffesorClass" dark>
      Actualizar
    </v-btn>
  </div>
</template>

<script>
import {path} from "@/api/conf_api";
export default {
  layout: "LayoutPanel",
  data() {
      return {
          request_user: {
              id: "",
              username: "",
              fullanme: "",
              is_instructor: false,
              email: "",
              image_user: null,
          }
      }
  },
  methods: {
    async get_user_info() {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: 'Token ' + token },
          baseURL: path + `/account/infoUser/`,
        })
        .then((result) => {
            this.request_user = result.data;
            this.request_user.image_user = null;
            if(result.data.is_instructor) {
              this.request_user.is_instructor = true;
            }
            console.log(this.request_user)
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    }, 
    async updateProffesorClass() {
      let df = new FormData();

      if(this.request_user.username != "") {
        df.append('username',this.request_user.username);
      }
      if(this.request_user.fullname != "") {
        df.append('fullname',this.request_user.fullname);
      }
      if(this.request_user.email != "") {
        df.append('email',this.request_user.email);
      }
      df.append('is_instructor', this.request_user.is_instructor);
      df.append('user',this.request_user.id)

      if(this.request_user.image_user) {
          df.append("image_user", this.request_user.image_user);
      }
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "put",
          headers: { Authorization: 'Token ' + token},
          baseURL: path + `/account/update_usuario/`,
          data: df,
        })
        .then((result) => {
          console.log("Actualizado los datos");
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    documentFile(event) {
      this.request_user.image_user = event.target.files[0];
    },
  },
  mounted() {
      this.get_user_info()
  }
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