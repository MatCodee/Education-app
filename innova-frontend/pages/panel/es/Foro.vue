<template>
  <div class="container-md">
    <h2 class="my-5">Foro del curso:</h2>
    <div class="d-flex">
      <h2 class="my-5 user-title mr-6">Deja un comentario</h2>
      <button
        class="button-font button-m btn-w"
        @click="dialog_foro = !dialog_foro"
      >
        Comentar
      </button>
    </div>

    <div class="mt-2" v-for="(f, index) in foro" :key="index">
      <v-card class="max-auto py-6 px-10 layout-card">
        <div class="content-user">
          <v-avatar>
            <img :src="f.user.image_user" class="img-dim" alt="" />
          </v-avatar>
          <div class="content-body">
            
            <h5 class="user-title">{{ f.user.username }}</h5>
            
            <div class="d-flex">
              <p>{{f.user.email}}</p> &nbsp;
              <p class="ml-2">{{ f.date_created }}</p>
            </div>

            <p class="textarea-edit">{{ f.message }}</p>
            <div class="d-flex">
              <div class="d-flex">
                <v-btn
                  x-small
                  @click="add_like(f.id)"
                  icon
                  color="green"
                > <v-icon dark> mdi-thumb-up </v-icon></v-btn>
                <p class="ml-2">0</p>
              </div>
              <div class="d-flex ml-4">
                <v-btn
                  x-small
                  color="primary"
                  icon
                > <v-icon dark> mdi-comment </v-icon></v-btn>
                <p class="ml-2">0</p>
              </div>
            </div>

          </div> 
        </div>
      </v-card>
    </div>
    <h2 class="my-5 user-title mr-6">Deja un comentario</h2>
    <div class="d-flex">
      <v-file-input
        chips
        multiple
        label="Archivos o documentos"
      ></v-file-input>
      <v-file-input
        small-chips
        multiple
        label="Imagenes o Videos"
      ></v-file-input>
      </div>
    <v-textarea
      height="80"
      outlined
      class="textarea-style"
      name="input-7-4"
      v-model="message_foro"
    ></v-textarea>

    <button @click="add_foro_client_down" class="button-font button-m btn-w">
      Comentar
    </button>

    <v-dialog v-model="dialog_foro" width="700px">
      <v-card class="px-6 py-12">
        <h2 class="my-5 user-title mr-6">Deja un comentario</h2>
      <div class="d-flex">
        <v-file-input
          chips
          multiple
          label="Archivos o documentos"
        ></v-file-input>
        <v-file-input
          small-chips
          multiple
          label="Imagenes o Videos"
        ></v-file-input>
        </div>
        <v-textarea
          height="80"
          outlined
          class="textarea-style"
          name="input-7-4"
          v-model="message_foro"
        ></v-textarea>
        <button @click="add_foro_client" class="button-font button-m btn-w">
          Comentar
        </button>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";
import { date_element, relativeDate } from "@/helpers/time_function";

export default {
  layout: "LayoutPanel",
  data() {
    return {
      foro: [],
      message_foro: "",
      current_user: {},
      dialog_foro: false,
      like: false,
    };
  },
  methods: {
    date_element: date_element,
    relativeDate: relativeDate,

    process_date(date) {
      let mont_calc = parseInt((date.getMonth() + 1)/10)
      let day_calc = parseInt((date.getDate()) /10)
      console.log(mont_calc)
      console.log(day_calc)
      if(mont_calc === 0) {
        mont_calc = `0${parseInt(date.getMonth() + 1)}`
      }else {
        mont_calc = date.getMonth() + 1;
      }
      if(day_calc === 0) {
        day_calc = `0${parseInt(date.getDate())}`
      }else {
        day_calc = date.getDate();
      }
      return date.getFullYear() + "-" + mont_calc + "-" + day_calc;
    },
    add_foro_client_down() {
      if(this.message_foro) {
        let date = this.process_date(new Date())
        let new_form = {
          user: this.current_user,
          message: this.message_foro,
          date_created: date,
        };
        console.log("Este es el formulario")
        console.log(new_form);
        this.foro.push(new_form);
        this.add_foro();
      }
    },
    add_foro_client() {
      if(this.message_foro) {
        let date = this.process_date(new Date())
        let new_form = {
          user: this.current_user,
          message: this.message_foro,
          date_created: date,
        };
        console.log(new_form);
        this.foro.push(new_form);
        this.add_foro();
      }
      this.dialog_foro = !this.dialog_foro;
    },
    async add_foro() {
      let token = localStorage.getItem("token");
      let formForo = {
        user: parseInt(localStorage.getItem("user_id")),
        course: this.$store.state.current_course.id,
        message: this.message_foro,
      };
      console.log(formForo);
      await this.$axios
        .request({
          method: "post",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/comunication/add_foro_course/`,
          data: formForo,
        })
        .then((response) => {
          //this.foro.push(new_form);
          this.message_foro = '';
          console.log("agregado con exito");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async get_foro() {
      let slug = this.$store.state.current_course.slug;
      console.log(slug)
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/comunication/get_foro_course/${slug}`,
        })
        .then((response) => {
          this.foro = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // funciones del usuario ya sea para poder dar un like
    async add_like(id_foro) {
      let token = localStorage.getItem("token");
      let form_user = this.$store.state.user_information;
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/comunication/like_acction/${id_foro}`,
          data:form_user
        })
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // funciones de stilo
    scroll_down() {},
  },
  mounted() {
    this.current_user = this.$store.getters.get_user_information;
    console.log(this.current_user);
    this.get_foro();
  },
};
</script>


<style lang="scss" scoped>
//layout
.container-md {
  width: 80%;
  margin: 20px auto;
}

@media screen and (max-width: 800px) {
  .container-md {
    width: 95%;
    margin: 20px auto;
  }
}

// container foro
.box-foro {
  background-color: rgb(242, 242, 242);
  padding: 20px;
  height: 500px;
  border-radius: 16px;
  overflow-y: scroll;
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

// boton
.button-m {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  background-color: #5631eb;
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

.layout-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
}

.img-dim {
  object-fit: cover;
}

.textarea-edit {
  white-space: pre-wrap;
}

</style>