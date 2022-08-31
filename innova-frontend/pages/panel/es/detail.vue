<template>
  <div>
    <v-app-bar
      absolute
      color="primary"
      class="py-0 app-bar-layout"
      elevation="0"
    >
      <p class="text-h6 mt-5 white--text content-hide">{{ course.title }}</p>
      <v-spacer></v-spacer>
      <v-form action="/search" class="form-box" method="get">
        <v-text-field
          class="mt-7 size-text-field"
          outlined
          label="Buscar cualquier cosa"
          background-color="white"
          clearable
          solo
          type="text"
          rounded
          dense
          name="query"
        >
          <template v-slot:append>
            <v-icon color="primary"> mdi mdi-feature-search-outline </v-icon>
          </template>
        </v-text-field>
      </v-form>
      <v-btn rounded color="white" dark to="/panel/mycourses" icon>
        <v-icon>mdi-logout</v-icon>
      </v-btn>

      <!--
         <app-bar-user-menu></app-bar-user-menu>
        -->
    </v-app-bar>

    <v-navigation-drawer
      class="margin-element-drawer"
      absolute
      app
      hide-overlay
      height="100%"
      right
      v-model="notDrawer"
      width="23%"
    >
        <v-list v-if="course.course_data">
          <v-list-group
            :value="true"
            prepend-icon="mdi-folder-account"
            v-for="(item,index) in course.course_data" :key="index"
          >
            <template v-slot:activator>
              <v-list-item-title> Semana  {{index + 1}} </v-list-item-title>
            </template>

            <v-list-item
              v-for="week in item.week_data"
              :key="week.id"
              link
              @click="getVideo(week)"
            >
              <v-list-item-action>
                 <v-checkbox color="primary"  v-if="week.histoty_class[0]" v-model="week.histoty_class[0].completed_class"></v-checkbox>
                 <v-checkbox color="primary" v-else :v-model="default_checkbox"></v-checkbox>
              </v-list-item-action>

              <v-list-item-content>
                <v-list-item-title v-html="week.title"></v-list-item-title>
                <v-list-item-subtitle
                  v-html="week.resumen"
                ></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

          </v-list-group>

        </v-list>
    </v-navigation-drawer>

    <div
      class="container-element-class margin-center-element"
    >

    <div v-if="vista_select_page == 2">
      <div class="my-10 margin-content-badge" v-if="course_select" >
        <h3 class="mb-3">{{ course_select.title }}</h3>
      </div>
      <div class="desing-video" v-if="course_select && course_select.video">
        <video
          class="content-video"
          @ended="finalVideo(course_select)"
          controls
          :src="course_select.video"
        ></video>
      </div>
      <div v-else-if="course_select && course_select.link">
        <a :href="course_select.link" target="_blank">{{
          course_select.link}}</a>
      </div>
      <div class="my-10 margin-content-badge" v-if="course_select">
        <h3 class="mb-5">Recursos de la clase:</h3>
        <p class="mb-3">
          {{ course_select.resumen }}
        </p>
        <a :href="course_select.document" target="_blank">{{
          process_link(course_select.document)}}</a>


        <div v-for="item,index in course_select.documents" :key="index">
          <a class="a-link"  target="_blank" :href="item.document">{{index+1}}) &nbsp; {{item.title}}</a>
        </div>
      </div>
      <div />
      </div>
      
      


      <div class="margin-content-badge list-down-hide">
        <v-list v-if="course.course_data">
          <v-list-group
            :value="true"
            prepend-icon="mdi-folder-account"
            v-for="(item,index) in course.course_data" :key="index"
          >
            <template v-slot:activator>
              <v-list-item-title> Semana {{item.id}} </v-list-item-title>
            </template>

            <v-list-item
              v-for="week in item.week_data"
              :key="week.id"
              link
              @click="getVideo(week)"
            >
              <v-list-item-action>
                <v-checkbox color="primary" v-if="week.histoty_class" v-model="week.histoty_class.completed_class"></v-checkbox>
                <v-checkbox color="primary" v-else :v-model="default_checkbox"></v-checkbox>
              </v-list-item-action>

              <v-list-item-content>
                <v-list-item-title v-html="week.title"></v-list-item-title>
                <v-list-item-subtitle
                  v-html="week.resumen"
                ></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

          </v-list-group>

        </v-list>
      </div>

      <div class="margin-content-badge mt-10"  v-if="vista_select_page == 1">
        <h2>Acerca de este curso</h2>

        <p class="mt-2">{{ course.subtitle }}</p>
        <span class="textarea-edit">
          {{ course.description }}
        </span>
        <div class="mt-5 content-button-certificate">
          <v-btn :href="certificate.certificate" target="_blank" v-if="course.end_course && certificate" rounded color="primary" :disabled="!course.end_course" depressed>
              Obtener Certificado
            </v-btn>
          <v-btn v-else rounded color="primary" :disabled="!course.end_course" depressed>
              Obtener Certificado
            </v-btn>
        </div>

      </div>

      <v-divider />

      
      <div class="margin-content-badge" v-if="foro.length != 0">
        <div>
          <h3 class="my-5 user-title">Deja un comentario</h3>
          <v-textarea
            height="100"
            outlined
            class="textarea-style"
            name="input-7-4"
            label="Outlined textarea"
            v-model="message_foro"
          ></v-textarea>
          <button
            @click="add_foro"
            class="float-right button-font button-m btn-w"
          >
            Comentar
          </button>
        </div>

        <h3 class="my-5">Comentarios de estudiantes</h3>
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
            --></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";
import { date_element, relativeDate } from "@/helpers/time_function";

export default {
  layout: "LayoutDetailEstudent",
  components: {
    /*
        AppBarUserMenu: () => import("@/components/ComponentsPanel/AppBarUserMenu")
        */
  },
  data() {
    return {
      default_checkbox: false,
      vista_select_page: -1,
      foro: [],
      message_foro: "",

      vista_select: 2,
      checkbox: true,
      notDrawer: true,
      course: [],
      ite: 0,
      settings: [],
      course_select: null,

      interval: {},
      value: 0,

      certificate: '',
    };
  },
  beforeDestroy() {
    clearInterval(this.interval);
  },

  methods: {
    date_element: date_element,
    relativeDate: relativeDate,

    process_link(link) {
      if(link) {
        let link_list = link.split("/");
        return link_list[link_list.length - 1];
      }
    },

    change_tab(number) {
      this.vista_select = number;
    },
    finalVideo(item) {
      console.log("Detecta final video");
      console.log(item.histoty_class.length == 0);
      if(item.histoty_class.length == 0) {
        let token = localStorage.getItem("token");
        // cuando el video finalice guardare en la data de historial donde a cada historial le corresponde un curso
        let clase_data = this.course_select;
        console.log(clase_data);
        // cuando finaliza el video se crea un objeto con el usuario y el el video completado
      

        let formData = {
          user: localStorage.getItem('user_id'),
          class_course: clase_data.id,
          completed_class: true,
        }
        this.$axios
          .request({
            method: "post",
            headers: { Authorization: "Token " + token },
            baseURL: path + `/courses/create_history_class/`,
            data: formData,
          })
          .then((response) => {
            this.getCourse();
            console.log("agregado con exito");
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    // Esta es la funcion que se encarga de detectar cuando se termina el video
    myHandler() {
      let aud = document.getElementById("myAudio");
      aud.onended = function () {
        alert("The audio has ended");
      };
    },
    async initial_content() {
      // qui debemos cargar el estado en el que quedo el video
      this.course_select = this.course.course_data[0];
      console.log("paso por aqui");
    },
    getVideo(item) {
      console.log(item.id)
      let token = localStorage.getItem("token");
      this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/get_class_from_week/${item.id}`,
        })
        .then((response) => {
          this.course_select = response.data;
          console.log(this.course_select);
        })
        .catch((error) => {
          console.log(error);
        });


      this.vista_select_page = 2;
    },
    async get_certificate(course) {
      let token = localStorage.getItem("token");

      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/get_certiifcate/${course.id}/${this.$store.state.user_information.id}`,
        })
        .then((response) => {
          this.certificate = response.data;
          console.log(this.certificate);
        })
        .catch((error) => {
          console.log(error);
        });   
    },
    async getCourse() {
      let token = localStorage.getItem("token");
      let course = this.$store.state.current_course;
      console.log(course);
      console.log("Mostrando la informacion de los cursos en el proceso de la informacion")

      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/detail-course/${course.slug}`,
        })
        .then((response) => {
          this.course = response.data;
          console.log(this.course);
          console.log("Esta disponible el certificado: ",this.course.end_course);
          if(this.course.end_course) {
            console.log("Entrando");
            this.get_certificate(this.course);
          }
          console.log(this.course);
          //this.initial_content();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.vista_select_page = 1;
    this.getCourse();
    //this.get_foro();

    this.interval = setInterval(() => {
      if (this.value === 100) {
        return (this.value = 0);
      }
      this.value += 10;
    }, 1000);
  },
};
</script>

<style lang="scss" scoped>
.app-bar-layout {
  z-index: 100;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
}
.margin-content {
  margin-top: 64px;
  width: 77%;
}
.desing-video {
  width: 800px;
  background-color: rgb(0, 0, 0);
  max-width: 77%;
}
.content-video {
  margin-top: 20px;
  width: 100%;
}

.v-progress-circular {
  margin: 1rem;
}

/* debemos hacer response el video que se esta reproduciendo */

.form-x {
  width: 400px;
}
.margin-content-badge {
  width: 77%;
  margin-bottom: 50px;
}

.list-down-hide {
  display: none;
}
//1212
@media (max-width: 1212px) {
  .content-hide {
    display: none;
  }
  .margin-element-drawer {
    display: none;
  }

  .list-down-hide {
    display: block;
  }

  .margin-center-element {
    margin: 0 20px;
  }
}

.margin-center-element {
  margin: 0 50px;
}

@media (max-width: 1252px) {
  .margin-content {
    margin-top: 56px;
    width: 100%;
  }
  .form-x {
    width: 100%;
    margin-right: 50px;
  }
  .margin-content-badge {
    width: 100%;
    margin-bottom: 50px;
  }
  .margin-center-element {
    margin: 0 15px;
  }
}
.badge-color {
  color: black;
}

.content-user {
  display: flex;
  align-items: flex-start;
}
.content-body {
  margin-left: 15px;
}

.form-box {
  max-width: 700px;
  width: 100%;
}

.margin-element-drawer {
  margin-top: 58px;
}

.user-title {
  font-size: 18px;
  font-weight: 700;
  color: rgb(0, 0, 0);
}



.user-question {
  font-size: 13px;
}

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

.textarea-style {
  border-radius: 16px;
}

.title-content-foro {
  display: flex;
  align-items: baseline;
  margin-bottom: -15px;
}
.title-content-foro h5 {
  margin-right: 10px;
}

.container-element-class {
  margin-top: 150px;
}

.textarea-edit {
  white-space: pre-wrap;
}

.content-button-certificate {
  display: flex;
  justify-content: center;
}

.a-link {
  text-decoration: none;
}
</style>