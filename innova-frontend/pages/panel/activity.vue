<template>
  <div class="container-md pt-10">
    <h2 class="ml-5">Hola,  ¡Te damos la bienvenida a LixFux!</h2>

    <v-row class="mt-3">
      <v-col sm="12" md="7" lg="8" xl="9">
        <v-card class="shadow-card content-card mt-2" rounded="xl">
          <v-list three-line>
            <v-list-item-group v-model="selectedItem" color="primary" v-if="homeworks">
                <v-subheader
                  v-text="'Recordatorios de los Cursos:'" 
                ></v-subheader>
              <div v-for="(item, index) in homeworks" :key="index">
                <v-list-item @click="select_homework(item.id)">
                  <v-list-item-avatar>
                    <v-icon
                        class="blue"
                        dark
                        color="white"
                      >
                        mdi-clipboard-text
                      </v-icon>
                  </v-list-item-avatar>


                  <v-list-item-content>
                    <v-list-item-title v-html="item.get_course_info"></v-list-item-title>
                    <v-list-item-subtitle v-html="'Profesor: ' + item.get_proffesorInfo"></v-list-item-subtitle>

                    <v-list-item-subtitle
                      class="text--primary"
                      v-text="item.title"
                    ></v-list-item-subtitle>


                  </v-list-item-content>


                  <v-list-item-action v-if="item.start_date && item.end_date">
                    <v-list-item-action-text class="time-detail-desing" v-text="'tiempo faltante: '  + date_homework(item.start_date,item.end_date)"></v-list-item-action-text>
                  </v-list-item-action>

                </v-list-item>
                

              </div>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
      <v-col sm="12" md="5" lg="4" xl="3">
        <div class="container-picker">
          <v-date-picker
            class="shadow-card"
            v-model="date"
            readonly
          ></v-date-picker>          
        </div>

      </v-col>
    </v-row>


    <h2 class="ml-5 my-5">Nuevos Cursos</h2>
    <v-row class="mb-5">
      <v-col
        sm="12"
        md="6"
        lg="4"
        xl="3"
        v-for="course in courses"
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
              {{ course.title }}
            </v-card-title>
            <!--
            <v-card-subtitle class="subtitle-text-card">
              Por Cecilia Hugony
            </v-card-subtitle>
            -->
            <v-card-actions class="button-content-page">
              <div class="container-element-btn">
                <button
                  @click="detail_course(course.slug)"
                  class="layout-btn button-font button-m"
                >
                  Detalle del curso
                </button>
              </div>
            </v-card-actions>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>


<script>
import { path } from "@/api/conf_api";
import { formatDistance } from "date-fns";

export default {
  layout: "LayoutPanel",
  data() {
    return {
      courses: [],
      homeworks : [],
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      selectedItem: 0,

    };
  },
  mounted() {
    this.getCategory();
    this.get_homework();
  },
  methods: { 
    detail_course(slug) {
      // guardamos el slug del curso
      // mandamos un push a detail course\
      console.log(slug);
      localStorage.setItem("slug_course", slug);

      this.$router.push("/panel/detail-course");
    },

    date_homework(start_date,end_date) {
      return formatDistance(new Date(start_date), new Date(end_date));
    },

    select_homework(id) {
      this.$store.commit("set_id_homework",id);
      this.$router.push(`/panel/detail-homework/`)
    },

    async get_homework() {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { 
            Authorization: `Token ${token}` ,
            'Content-Type': 'application/json',
          },
          baseURL: path + `/courses/list_homework/`,
        })
        .then((response) => {
          console.log(response.data['data'])
          if(response.data['data'] != "error") {
            this.homeworks = response.data;
            console.log(this.homeworks);
          }
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
    async getCategory() {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/courses-list/`,
        })
        .then((response) => {
          this.courses = response.data;
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.container-md {
  width: 80%;
  margin: 0 auto;
}


@media screen and (max-width: 956px) {
  .container-picker {
    display: flex;
    align-items: center;
    justify-content: center;
  }
}

@media screen and (max-width: 800px) {
  .container-md {
    width: 98%;
    margin: 0 auto;
  }

}

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

/* estilos del link del foro*/
.card-foro {
  width: 100%;
  height: 200px;
}

.content-foro-element {
  padding: 20px 50px;
  width: 100%;
}
.container-element-button {
  display: flex;
  justify-content: center;
  margin: 5px 0;
}
.content-foro-element h3 {
  text-align: center;
}

.time-detail-desing {
  font-size: 16px;
  font-weight: 600;
}


.title-text-card {
  font-size: .8rem;
}

</style>