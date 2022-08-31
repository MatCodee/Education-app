<template>
  <div class="margin-content">
      <v-row v-if="course">
        <v-col md="8">
          
            <h2>{{course.title}}</h2>
            <p> {{course.subtitle }}</p>

            <div class="mb-4">
              <div class="d-flex mt-10 mb-3">
                <figure v-if="!info_user.image_user">
                  <v-img class="dimension_image_user" src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
                </figure>
                <figure v-else>
                  <v-img class="dimension_image_user" :src="info_user.image_user"></v-img>
                </figure>
                
                  
                <p>Creado por  <span class="desing_info_user"> {{info_user.username}} </span> </p>

              </div>

              <div class="d-flex">
                <p class="mr-5">Fecha</p>
                <p>Espanol</p>
              </div>

            </div>

          <v-card class="shadow-card mb-16">
            <div class="pa-16">
            <h3 class="mb-5">Que aprenderas </h3>
            <p>{{course.description}}</p>

            </div>
          </v-card>

          <div class="my-10">
          <h3 v-if="course.course_data"  >Contenido del Curso </h3>
          <v-list>

              <v-list-group
                  :value="true"
                  prepend-icon="mdi-folder-account"
                  v-if="course.course_data"                
              >
                  <template v-slot:activator>
                  <v-list-item-title> Clases del Curso </v-list-item-title>
                  </template>

                  <v-list-item
                      v-for="item in course.course_data"
                      :key="item.id"
                      link
                  >
                      <v-list-item-action>
                      <v-checkbox
                          color="primary"
                      ></v-checkbox>
                      </v-list-item-action>
                      
                      <v-list-item-content>
                          <v-list-item-title v-html="item.title"></v-list-item-title>
                          <v-list-item-subtitle v-html="item.resumen"></v-list-item-subtitle>
                      </v-list-item-content>
                  </v-list-item>
              </v-list-group>
              </v-list>
          </div>

      
        </v-col>

        <v-col md="4">

          <figure>
            <img :src="course.get_image" class="dimension_image" alt="">
          </figure>
          <div class="my-4">
            <v-chip
              class="ma-2"
              color="primary"
            >
              {{course.level}}
            </v-chip>

            <v-chip
              class="ma-2"
              color="primary"
            >
              {{course.category}}
            </v-chip>

            <v-chip
              class="ma-2"
              color="secondary"
            >
              {{course.tipo_producto}} 
            </v-chip>
          </div>
          <div class="pl-6">
            <h4 class="mb-3"> Este Curso Incluye </h4>
            <p> Recursos </p>
            <p> Ejercicios </p>
            <p> Acceso a las clases </p>
          </div>
           
        </v-col>
      </v-row>
     
  <div v-if="recomended_courses.length!=0">
    <h3 class="my-3">Cursos relacionados </h3>
    <v-row class="mb-5">
      <v-col
        sm="12"
        md="6"
        lg="4"
        xl="3"
        v-for="course in recomended_courses"
        :key="course.id"
      >
        <v-card class="layout-card" rounded="lg">
          <v-img
            :src="course.get_image"
            @click="detail_course(course.slug)"
            class="detail-img-desing"
          ></v-img>
          <div class="padd-content-card">
            <v-card-title class="title-text-card">
              {{ course.title.substring(0, 24) }}
            </v-card-title>



            <v-card-actions class="button-content-page">
              <div class="container-element-btn">
                <button
                  @click="detail_course(course.slug)"
                  class="layout-btn button-font button-m"
                >
                  Inscribite ahora
                </button>
              </div>
            </v-card-actions>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </div>


  </div>
</template>

<script>
//import axios from "axios";
import {path} from "@/api/conf_api";


export default {
  layout: "LayoutPanel",
  data() {
    return {
      course: {},
      recomended_courses: [],
      category_course: '',
      id_course : -1,
      slug_course: '',
      info_user: {},
    }
  },
  methods: {
    async getCourse() {
      // traemos la informaicon del curso
      let slug = this.slug_course;
      let token = localStorage.getItem("token");
        await this.$axios.request({
            method: "get",
            headers: { Authorization: `Token ${token}` },
            baseURL: path + `/courses/detail_course_buy/${slug}`,
          })
        .then((response) => {
          this.course = response.data;
          this.category_course = response.data['category'];
          this.id_course = response.data['id'];
          //console.log(this.category_course);
          //console.log(this.course);

          this.get_user()
          this.recomended_course();
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
    async recomended_course() {
      if(this.category_course) {
      let token = localStorage.getItem("token");
      let category = this.category_course;
        await this.$axios.request({
            method: "get",
            headers: { Authorization: `Token ${token}` },
            baseURL: path + `/courses/recomend_course_buy/${category}/${id_course}`,
          })
        .then((response) => {
          this.recomended_courses = response.data;
          //console.log(this.recomended_courses)
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
      }
    },
    select_recomended_course(course) {
      localStorage.setItem("slug_course",course.slug);
    },
    async get_user() {
      if(this.course) {
         let token = localStorage.getItem("token");
         await this.$axios.request({
            method: "get",
            headers: { Authorization: `Token ${token}` },
            baseURL: path + `/account/get_user/${this.course.author}`,
          })
        .then((response) => {
          this.info_user = response.data;
          //console.log(this.info_user);
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
      }
    },
    detail_course(slug) {
      // guardamos el slug del curso
      // mandamos un push a detail course\
      localStorage.setItem("slug_course",slug);

      this.$router.push('detail-course'); 
    },
  },
  computed: {
  },
  mounted() {
    // llamamos el slug del curso
    this.slug_course = localStorage.getItem('slug_course');
    this.getCourse();
  },
};
</script>

<style lang="scss" scoped>
.margin-content {
  width: 80%;
  margin: 0 auto;
  margin-top: 90px;
}



.img-response-dim {
  height: 160px;
  width: 100%;
  object-fit: cover;
  object-position: center;
}



@media (max-width: 575px) {
  .img-response-dim {
      height: 100%;
      width: 100%;
    object-fit: cover;
    object-position: center;
  }
}

.portfolio-card {
  min-width: 260px;
}


.dimension_image {
  width: 400px;
  height: 100%;
  border-radius: 10px;
  object-fit: cover;
}

.desing_info_user {
  color: rgb(64, 113, 219);
}

.dimension_image_user {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
}
.content-user {
  display: flex;
}





// button style

.shadow-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
}

.content-card {
  height: 370px;
  overflow-y: auto;
}

.detail-img-desing {
  height: 200px;
  object-fit: cover;
  object-position: center;
}

/* botones estilos */

.layout-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
  max-width: 390px;
}

.button-content-page {
  width: 100%;
}

.button-content-page button {
  height: 45px !important;
}

.container-element-btn {
  width: 100%;
  display: flex;
  align-items: center;
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
