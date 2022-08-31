<template>
    <div class="container-md">
    <v-select
      :items="course_names"
      label="Selecciona el curso"
      v-model="select_item"
      solo
    ></v-select>
    <button
      class="button-font button-m btn-w"
      @click="filter_foro(select_item)"
    >
      filtrar
    </button>

<div v-if="foro.length!=0">
    <h3 class="my-5">Foro del curso: </h3>
    <div class="box-foro">

    <div class="mt-2" v-for="(f, index) in foro" :key="index">
      <div class="content-user">
        <v-avatar>
          <img :src="f.user.image_user" alt="" />
        </v-avatar>
        <div class="content-body">
          <div class="title-content-foro">
            <h5 class="user-title">{{ f.user.username }}</h5>
            <p>{{ relativeDate(f.date_created) }}</p>
          </div>

          <p>{{ f.message }}</p>

          <!--
            <p class="user-question">¿Te sirvio el comentario?</p>

            <v-btn class="mx-2" fab dark icon small color="primary">
              <v-icon dark> mdi-thumb-up-outline </v-icon>
            </v-btn>
            <v-btn class="mx-2" fab dark icon small color="primary">
              <v-icon dark> mdi-thumb-down-outline </v-icon>
            </v-btn>
            -->
        </div>
      </div>
    </div>
    </div>
    <h3 class="my-5 user-title">Deja un comentario</h3>
    <v-textarea
      height="100"
      outlined
      class="textarea-style"
      name="input-7-4"
      v-model="message_foro"
    ></v-textarea>
    <button @click="add_foro" class="button-font button-m btn-w">
      Comentar
    </button>
</div>
    </div>
</template>

<script>
import { path } from "@/api/conf_api";
import { date_element, relativeDate } from "@/helpers/time_function";

export default {
    layout: "LayoutPanelProffesor",
    data() {
        return {
            foro: [],
            message_foro: "",
            select_item: "",
            course_names: [],
            current_slug: "",
        }
    },
    methods: {
    date_element: date_element,
    relativeDate: relativeDate,

    async filter_foro(selected_item) {
        if(selected_item){
            for (let it = 0; it < this.items.length; it++) {
                if (this.items[it].title === selected_item) {
                    console.log("entro");
                    this.current_slug = this.items[it].slug;
                    console.log(this.items[it])
                    break;
                }
            }
            console.log(this.current_slug);
            this.get_foro(this.current_slug);
            console.log(this.foro);
        }
    },

    async add_foro() {
      let token = localStorage.getItem("token");
      let formForo = {
        user: parseInt(localStorage.getItem("user_id")),
        course: this.$store.state.current_course.id,
        message: this.message_foro,
      };
      await this.$axios
        .request({
          method: "post",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/add_foro_course/`,
          data: formForo,
        })
        .then((response) => {
          //this.foro.push(formForo);
          console.log("agregado con exito");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_foro(slug) {
      let token = localStorage.getItem("token");
      this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/get_foro_course/${slug}`,
        })
        .then((response) => {
          this.foro = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async get_course_name() {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/proffesor-course-names/`,
        })
        .then((response) => {
          if (response.data != "error") {
            for (let it = 0; it < response.data.length; it++) {
              this.course_names.push(response.data[it].title);
            }
            this.items = response.data;
          }
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
    },
    mounted() {
        this.get_course_name();  
    },
}
</script>


<style lang="scss">
.container-md {
  margin: 0 auto;
  width: 80%;
  max-width: 1300px;
  margin-top: 60px;
}


// container foro 
.box-foro {
  background-color: rgb(242, 242, 242);
  padding: 20px;
  height: 500px;
  border-radius: 16px;
  overflow-y: auto;
}

@media screen and (max-width: 1600px) {
  .box-foro {
    background-color: rgb(242, 242, 242);
    padding: 20px;
    height: 330px;
    border-radius: 16px;
    overflow-y: auto;
  } 
}


//layout foro contenedor
.content-user {
  display: flex;
  align-items: flex-start;
}
.content-body {
  margin-left: 15px;
}
.title-content-foro {
  display: flex;
  align-items: baseline;
  margin-bottom: -15px;
}
.title-content-foro h5 {
  margin-right: 10px;
}
.user-title {
  font-size: 18px;
  font-weight: 700;
  color: rgb(0, 0, 0);
}

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