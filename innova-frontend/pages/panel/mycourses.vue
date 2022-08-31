<template>
  <div class="margin-content container-md">
    <h2 class="text-h4 my-4 black--text">Mis Cursos</h2>
    <p> Cursos Registrados del Usuario</p>
    
    <v-row class="my-5">
          <v-col sm="12" md="6" lg="4" xl="3" v-for="course in courses" :key="course.id">
          <v-card
            class="layout-card"
            rounded="lg"
          >
            <v-img
              class="img-response-dim"
              height="200px"
              :src="course.get_image"
               @click="entryCourse(course)"
            ></v-img>
       

            <div class="padd-content-card">
              <v-card-title class="title-text-card" v-if="course.title">
                {{ course.title.substring(0, 50)  }}
              </v-card-title>
              <!--
              <v-card-subtitle class="subtitle-text-card">
                Por Cecilia Hugony
              </v-card-subtitle>
              -->
              <v-card-actions>
                <div class="container-element-btn">
                  <button  @click="entryCourse(course)" class="layout-btn button-font button-m ">Empezar Curso</button>
                </div>
              </v-card-actions>
            </div>
          </v-card>
          </v-col>
      </v-row>

  </div>
</template>

<script>
//import axios from "axios";
import {path} from "@/api/conf_api";
export default {
  layout: "LayoutPanel",
  data() {
    return {
        courses: [],
    }
  },
  methods: {
    entryCourse(course) {
      this.$store.commit('removeSlug');
      localStorage.setItem('setSlug',course.slug);
      this.$store.commit('setSlug',course.slug);

      this.$store.commit('remove_current_course');
      console.log(course)
      this.$store.commit('set_current_course',course);
      
      this.$router.push('/panel/es/menu_course'); 
    },
    async getCursos() {
      let token = localStorage.getItem("token");
      await this.$axios.request({
            method: "get",
            headers: { Authorization: `Token ${token}`,'Content-Type': 'application/json', },
            baseURL: path + `/courses/user-course/`,
          })
        .then((response) => {
          if(response.data != 'error') {
            this.courses = response.data;
            console.log(this.courses)
          }
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
  },
  computed: {
  },
  mounted() {
    this.getCursos();
  },
};
</script>

<style lang="scss" scoped>
.margin-content {
  margin-top: 90px;
}
.container-md {
    width: 80%;
    margin: 0 auto;
}
.portfolio-card {
  min-width: 260px;
}

.container-img {
  height: 200px;
}
.img-response-dim {
  width: 100%;
  height: 100%;
  overflow: hidden;
  object-fit: cover;
  object-position: center center;

}


.layout-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
  max-width: 390px;
}


.container-element-btn {
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
    width: 100%;
    padding-left: 40px;
    padding-right: 40px;
    border-radius: 5px;
    color: #fff;
}


.button-font {
  text-decoration: none;
  font-family: Gilroy,SF Pro Display,-apple-system,BlinkMacSystemFont,Roboto,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;
  font-weight: 700;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: .4px;
}

.layout-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
  max-width: 390px;
}


.title-text-card {
  font-size: 16.5px;
}

</style>
