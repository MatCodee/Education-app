<template>
<div>
    <div class="mt-10 container-md">
      <h1> Cursos del profesor </h1>

      <p class="mt-5">Crea un curso atractivo
        No importa si llevas años dando clase o es la primera vez que lo haces, todo el mundo es capaz de crear un curso atractivo. Hemos recopilado recursos y las mejores prácticas para ayudarte a subir el listón con tu curso, sea cual sea tu base.</p>
 
    

    <v-card
      class="max-auto pa-10"
    >
      <v-card-text>
        <v-row>
          <v-col>
            <div class="d-flex justify-star">
              <p>Cursos del profesor</p>
            </div>
          </v-col>
          <v-col>
            <div class="d-flex justify-end">
                <button class="layout-btn button-font button-m btn-w"  @click="create_course">Crear un nuevo curso</button>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

       </div>

      <div class="container-md">
        <h1> Cursos Creados </h1>
        <v-row class="mb-5 mt-3">
          <v-col sm="12" md="4" lg="4" xl="3" v-for="course in courses" :key="course.id" >
          <v-card
            class="mx-auto layout-card"
            
            rounded="lg"
          >
            <v-img
              :src="course.get_image"
              @click="edit_course(course.slug)"
              class="detail-img-desing"

            ></v-img>
            <div class="padd-content-card">
              <v-card-title class="title-text-card" v-if="course.title">
                {{course.title.substring(0, 24)}}
              </v-card-title>

              <v-card-subtitle class="subtitle-text-card">
                Por Cecilia Hugony
              </v-card-subtitle>

              <v-card-actions>
                <div class="container-element-btn">
                  <button @click="edit_course(course.slug)" class="layout-btn button-font button-m btn-w100">Editar</button>
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
import {path} from "@/api/conf_api";
export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {
      courses: [],
    }
  },
  methods: {
    edit_course(slug) {
      //this.$store.commit('removeSlugProffesor');
      this.$store.commit('setSlugProffesor',slug);      
      this.$router.push('/panel/instructor/detailCourse/'); 
    },
    create_course() {
      this.$router.push('/panel/instructor/createCourse/'); 
    },


    async getCourseProffesor() {
        let token = localStorage.getItem("token");
        await this.$axios
          .request({
            method: "get",
            headers: { Authorization: "Token " + token },
            baseURL: path + `/courses/proffesor-course/`,
          })
        .then((response) => {
          if(response.data != 'error') {
            this.courses = response.data;
          }
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },

    permisos_user(){
      let per = localStorage.getItem('is_instructor');
      if(!per) {
        this.$router.push('panel/activity'); 
      }
    }
  },
  computed: {
  },
  mounted() {
    this.permisos_user();

    this.getCourseProffesor();
  },
};
</script>

<style lang="scss" scoped>

.container-md {
  width: 80%;
  padding-top: 50px;
  margin: auto;
}

.margin-content {
  margin-top: 90px;
}

.img-response-dim {
  min-width: 260px;
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


//btn
.container-element-btn {
  width: 100%;
}


.detail-img-desing {
  height: 200px;
  object-fit: cover;
  object-position: center;
}

.button-m:hover {
    background-color: #0f52b8;
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

//card



</style>
