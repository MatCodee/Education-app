<template>
  <div class="container-d">
    <div class="margin-content">
      <v-row>
        <v-col xs="12" sm="12" md="4" lg="3" xl="3" class="filter-desing">
          <p>FILTRAR RESULTADOS</p>

          <v-list class="list-desing">
            <v-list-group sub-group :value="true" no-action>
              <template v-slot:activator>
                <v-list-item-title class="title-list-detail"
                  >Tema</v-list-item-title
                >
              </template>

              <v-radio-group v-model="request_data.categoria">
                <v-radio
                  v-for="(categoria, i) in categorias"
                  :key="i"
                  :label="categoria"
                  :value="categoria"
                  class="radio-desing mb-2"
                ></v-radio>
              </v-radio-group>
            </v-list-group>

            <v-list-group sub-group  :value="true" no-action>
              <template v-slot:activator>
                <v-list-item-title class="title-list-detail"
                  >Nivel</v-list-item-title
                >
              </template>

              <v-checkbox
                v-model="request_data.nivel"
                label="Todos los niveles"
                value="Todos los niveles"
                color="primary"
                hide-details
                class="radio-desing margin-checkbox"
              ></v-checkbox>
              <v-checkbox
                v-model="request_data.nivel"
                label="Basico"
                value="Basico"
                color="primary"
                hide-details
                class="radio-desing margin-checkbox"
              ></v-checkbox>
              <v-checkbox
                v-model="request_data.nivel"
                label="Intermedio"
                value="Intermedio"
                color="primary"
                hide-details
                class="radio-desing margin-checkbox"
              ></v-checkbox>
              <v-checkbox
                v-model="request_data.nivel"
                label="Avanzado"
                value="Avanzado"
                color="primary"
                hide-details
                class="radio-desing mb-5"
              ></v-checkbox>
            </v-list-group>
            <v-list-group sub-group  :value="true" no-action>
              <template v-slot:activator>
                <v-list-item-title class="title-list-detail"
                  >Tipo de Curso</v-list-item-title
                >
              </template>

              <v-radio-group v-model="request_data.tipo_producto">
                <v-radio
                  v-for="(title, i) in tipo_producto"
                  :key="i"
                  :label="title"
                  :value="title"
                  class="radio-desing mb-2"
                ></v-radio>
              </v-radio-group>
            </v-list-group>
            <button
              @click="filter_course()"
              style="width: 100%"
              class="button-font-nav button-m-nav mr-4"
            >
              Filtrar
            </button>
          </v-list>
        </v-col>
        <v-col xs="12" sm="12" md="12" lg="9" xl="9">
          <v-row class="mb-5" v-if="!filter_on">
            <v-col
              sm="12"
              md="4"
              lg="4"
              xl="4"
              v-for="course in courses"
              :key="course.id"
            >
              <v-card class="mx-auto layout-card" rounded="lg">
                <v-img
                  :src="course.get_image"
                  @click="detail_course(course.slug)"
                  class="detail-img-desing"
                ></v-img>
                <div class="padd-content-card">
                  <v-card-title class="title-text-card">
                    {{ course.title.substring(0, 24) }}
                  </v-card-title>

                  <v-card-subtitle class="subtitle-text-card">
                    Por Cecilia Hugony
                  </v-card-subtitle>

                  <v-card-actions class="button-content-page">
                    <v-btn @click="addToCart(course)" class="mr-1" color="primary">
                      <v-icon>mdi-cart-minus</v-icon>
                    </v-btn>
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

          <v-row class="mb-5" v-if="filter_on">
            <v-col
              sm="12"
              md="4"
              lg="4"
              xl="4"
              v-for="course in courses_filter"
              :key="course.id"
            >
              <v-card class="mx-auto layout-card" rounded="lg">
                <v-img
                  :src="course.get_image"
                  @click="detail_course(course.slug)"
                  class="detail-img-desing"
                ></v-img>
                <div class="padd-content-card">
                  <v-card-title class="title-text-card">
                    {{ course.title.substring(0, 24) }}
                  </v-card-title>

                  <v-card-subtitle class="subtitle-text-card">
                    Por Cecilia Hugony
                  </v-card-subtitle>

                  <v-card-actions>
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
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";

export default {
  layout: "LayoutPanel",
  props: {},

  data() {
    return {
      isCardDetailsVisible: false,

      // Esta es la informacion de la consulta al menu
      nivel: ["Todos los niveles", "Basico", "Intermedio", "Avanzado"],
      categorias: [
        "Tegnologia",
        "Administracion",
        "Negocios",
        "Contabilidad",
        "Comunicacion",
      ],
      tipo_producto: ["Curso", "Programa Especializados"],

      // resultados de los cursos en general
      courses: [],
      //resultados del filter
      courses_filter: [],

      request_data: {
        categoria: "",
        nivel: [],
        tipo_producto: "",
      },

      filter_on: false,
    };
  },
  methods: {
    // Esta es la fncion que va a hacer el filtrado
    filter_course() {
      if (this.request_data) {
        let token = localStorage.getItem("token");
        this.$axios
          .request({
            method: "post",
            headers: { Authorization: `Token ${token}` },
            baseURL: path + `/courses/filter/`,
            data: this.request_data,
          })
          .then((response) => {
            this.courses_filter = response.data;
            console.log(this.courses_filter);
            this.filter_on = true;
          })
          .catch(function (error) {
            console.log("error encontrado: " + error);
          });
      }
    },
    async getCategory() {
      let token = localStorage.getItem("token");
      console.log("Bearer " + token);
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
    onScroll() {
      this.scrollInvoked++;
    },
    detail_course(slug) {
      // guardamos el slug del curso
      // mandamos un push a detail course\
      console.log(slug);
      localStorage.setItem("slug_course", slug);

      this.$router.push("/panel/detail-course");
    },


    addToCart(course) {
      if(course){
         this.$store.commit("addToCart", course);
      }
    },

  },

  components: {
    /*
    CardComponent: () => import("@/components/ComponentsPanel/Basic/CardComponent"),
    */
  },
  mounted() {
    this.getCategory();
  },
};
</script>

<style lang="scss">
.margin-content {
  margin-top: 30px;
}

.container-d {
  width: 90%;
  margin: 0 auto;
}

.container-filter {
  position: fixed;
}

.detail-img-desing {
  height: 200px;
  object-fit: cover;
  object-position: center;
}

.list-desing {
  width: 100%;
  height: 80vh;
  overflow-y: auto;
  overflow-x: hidden;
}

@media (max-width: 575px) {
  .list-desing {
    width: 100%;
  }
  .img-response-dim {
    height: 100%;
    width: 100%;
  }
}

.radio-desing {
  margin-left: 20px;
}

.portfolio-card {
  min-width: 260px;
}

.title-list-detail {
  font-size: 20px;
  font-weight: 900;
}

/* Componentes */

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
  background-color: white;
  border: solid 3px #0D47A1;
  transition: background-color 0.35s ease-in-out, color 0.15s ease-in-out,
    border 0.15s ease-in-out;
  height: 48px;
  width: 100%;
  padding-left: 40px;
  padding-right: 40px;
  border-radius: 5px;
  color: #0D47A1;
}
.button-m :hover {
  background-color: rgb(231, 231, 231);
}

.button-m-nav {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  background-color: #0D47A1;
  transition: background-color 0.35s ease-in-out, color 0.15s ease-in-out,
    border 0.15s ease-in-out;
  height: 38px;
  padding-left: 40px;
  padding-right: 40px;
  border-radius: 5px;
  color: #ffff;
}

.button-font-nav {
  text-decoration: none;
  font-family: Gilroy, SF Pro Display, -apple-system, BlinkMacSystemFont, Roboto,
    Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji,
    Segoe UI Symbol;
  font-weight: 700;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.4px;
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

.layout-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
  max-width: 390px;
}

.title-text-card {
}

.subtitle-text-card {
}

.button-content-page {
  width: 100%;
}

.button-content-page button {
  height: 45px !important;
}

.padd-content-card {
  padding: 5px;
}

@media (max-width: 1400px) {
  .title-text-card {
    font-size: 14px;
    line-height: 24px;
  }

  .subtitle-text-card {
    font-size: 12px;
    font-weight: 600;
  }
  .padd-content-card {
    padding: 1px;
  }
  .button-m {
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    background-color: white;
    border: solid 3px #0D47A1;
    transition: background-color 0.35s ease-in-out, color 0.15s ease-in-out,
      border 0.15s ease-in-out;
    height: 38px;
    padding-left: 30px;
    padding-right: 30px;
    border-radius: 5px;
    color: #0D47A1;
  }

  .button-content-page button {
    height: 35px !important;
  }
}

@media (max-width: 1263px) {
  .filter-desing {
    display: none;
  }
  .button-font {
    text-decoration: none;
    font-family: Gilroy, SF Pro Display, -apple-system, BlinkMacSystemFont,
      Roboto, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji,
      Segoe UI Emoji, Segoe UI Symbol;
    font-weight: 700;
    font-size: 13px;
    line-height: 13px;
    letter-spacing: 0.4px;
  }
  .button-m {
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    background-color: white;
    border: solid 3px #5631eb;
    transition: background-color 0.35s ease-in-out, color 0.15s ease-in-out,
      border 0.15s ease-in-out;
    height: 38px;
    width: 100%;
    padding-left: 40px;
    padding-right: 40px;
    border-radius: 5px;
    color: #5631eb;
  }

  .title-text-card {
    font-size: 14px;
    line-height: 24px;
  }

  .subtitle-text-card {
    font-size: 12px;
    font-weight: 600;
  }
  .padd-content-card {
    padding: 1px;
  }
}

@media (max-width: 950px) {
  .title-text-card {
    font-size: 20px;
    line-height: 28px;
  }

  .subtitle-text-card {
    font-size: 16px;
  }
  .padd-content-card {
    padding: 5px;
  }
  .button-content-page button {
    height: 45px !important;
  }
}


.margin-checkbox {
  margin-bottom: -10px;
}
</style>
