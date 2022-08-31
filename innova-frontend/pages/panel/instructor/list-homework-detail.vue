<template>
  <div class="container-md">
    <h3>{{ course.title }}</h3>
    <p>{{ course.description }}</p>

    <p>Complementar la tarea: (opcional)</p>
    <v-textarea
      v-model="form_homework.message"
      solo
      name="input-7-4"
      label="Solo textarea"
    ></v-textarea>
    <p>Subir la tarea aqui: .pdf, .word, .ppt</p>
    <figure>
      <v-img :src="form_homework.document">

      </v-img>
    </figure>
    <a :href="form_homework.document"> {{form_homework.document}}</a>

  </div>
</template>

<script>
import { path } from "@/api/conf_api";
export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {
      course: {},

      form_homework: {
        homework: "",
        message: "",
        document: null,
      },
    };
  },
  methods: {
    get_detail_homework() {
      let token = localStorage.getItem("token");
      let id_homework = this.$store.state.current_id_homework;
      this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/get_homework/${id_homework}`,
        })
        .then((response) => {
          console.log(response.data);
          this.course = response.data;
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
    get_detail_send_homework() {
      let token = localStorage.getItem("token");
      let id_homework = this.$store.state.current_id_homework_send;
      this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/get_send_homework/${id_homework}`,
        })
        .then((response) => {
          console.log(response.data);
          this.form_homework = response.data;
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
  },
  mounted() {
    this.get_detail_homework();
    this.get_detail_send_homework();
  },
};
</script>

<style lang="scss" scoped>
.container-md {
  margin: 0 auto;
  width: 80%;
  max-width: 1000px;
  margin-top: 60px;
}

/* botones estilos */
.button-m {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  background-color: #0d47a1;
  transition: background-color 0.35s ease-in-out, color 0.15s ease-in-out,
    border 0.15s ease-in-out;
  height: 48px;
  width: 100%;
  padding-left: 40px;
  padding-right: 40px;
  border-radius: 5px;
  color: #fff;
}

.button-font {
  text-decoration: none;
  font-family: Gilroy, SF Pro Display, -apple-system, BlinkMacSystemFont, Roboto,
    Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji,
    Segoe UI Symbol;
  font-weight: 700;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: 0.4px;
}

.btn-w {
  max-width: 183px;
}
</style>