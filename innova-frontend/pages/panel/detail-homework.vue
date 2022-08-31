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

    <input type="file" class="mt-5 mb-13" @change="previewFiles" multiple />
    <button
      @click="send_homework"
      class="layout-btn button-font button-m btn-w"
    >
      Enviar tarea
    </button>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";
export default {
  layout: "LayoutPanel",
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
          headers: { Authorization: `Token ${token}` },
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
    async send_homework() {
      let token = localStorage.getItem("token");
      let id_user = localStorage.getItem("user_id");
      console.log(id_user);
      let id = this.$store.state.current_id_homework;
      let formHomework = new FormData();
      formHomework.append("user", id_user);
      formHomework.append("document", this.form_homework.document);
      formHomework.append("message", this.form_homework.message);
      formHomework.append("homework", this.course.id);
      formHomework.append('completed',true);
      await this.$axios
        .request({
          method: "put",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/update_Send_homework/${id}`,
          data: formHomework,
        })
        .then((response) => {
          this.course = response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
    previewFiles(event) {
      this.form_homework.document = event.target.files[0];
    },
  },
  mounted() {
    this.get_detail_homework();
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