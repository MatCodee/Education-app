<template>
  <div class="container-md">
    <v-row>
      <v-col sm="12" md="12" lg="5" xl="6">
        <div class="content-element">
          <span class="title-span"> Aula Virtual </span>
          <p class="subtitle-content">Cursos en Modalidad E-learning</p>
          <div class="container-btn">
            <button class="button-font button-m button-primary btn-w" @click="btn_action"
              >Iniciar Sesión </button
            >
          </div>
        </div>
      </v-col>
      <v-col sm="12" md="12" lg="7" xl="6">
        <v-img class="img-desing" src="fondo_recortado.jpg" />
      </v-col>
    </v-row>
    <div class="d-flex justify-center">
    <div class="information-element-as">
      <p class="text-center">Instituciones Educaciones Asociada</p>
      <v-row class="d-flex align-center justify-center">
        <v-col sm="3">
          <v-img class="img-desing-card" src="logoKimun.jpg" />
        </v-col>
        <v-col sm="3">
          <v-img class="img-desing-card" src="logoAltamira.jpg" />
        </v-col>
      </v-row>
    </div>
    </div>

    <div class="my-10">
      <p class="subtitle-content mb-5">Nuevos Cursos Agregados</p>
      <v-row>
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
                  <a href="#" class="layout-btn button-font button-m"
                    >Inscribite ahora</a
                  >
                </div>
              </v-card-actions>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </div>

    <div class="content-element-md">
      <div class="information-element">
        <h2>LixFux</h2>
        <p>Comienza la Ruta de Cambio de tu Vida!</p>
        <a href="#" class="button-font button-m">Iniciar Sesion</a>
      </div>
    </div>




  </div>
  
</template>

<script>
import { path } from "@/api/conf_api";
export default {
  data() {
    return {
      courses: [],
    };
  },
  methods: {
    btn_action() {
      this.$store.commit('set_btn',!this.$store.state.btnobe);
    },
    async getCoursey() {
      await this.$axios
        .request({
          method: "get",
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
  mounted() {
    this.getCoursey();
  },
};
</script>

<style lang="scss" scoped>
:root {
  --color-primary-light: #6f4ef6;
  --color-primary-main: #4b22f4;
}

.container-md {
  width: 80%;
  margin: 0 auto;
  margin-top: 40px;
  max-width: 1854px;
}

.element-s {
  display: flex;
  height: 100vh;
}

.content-element {
  margin-top: 100px;
  width: 700px;
}

.title-span {
  font-size: 72px;
  line-height: 76px;
  font-weight: 700;
  color: rgb(0, 0, 0);
}
.subtitle-content {
  margin-top: 30px;
  font-size: 28px;
  line-height: 24px;
  font-weight: 400;
  color: rgb(0, 0, 0);
}

.container-btn {
  margin-top: 20px;
  display: flex;
  align-items: center;
}

.container-btn a {
  color: #ffff;
  margin-right: 30px;
}

.button-m:hover {
  background-color: #7a60f0;
}

.btn-w {
  max-width: 183px;
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

// section
.content-element-md {
  display: flex;
  align-items: center;
  justify-content: center;
}

.information-element {
  margin: 20px 0;
  width: 800px;
  text-align: center;
  h2 {
    font-size: 42px;
    line-height: 76px;
    font-weight: 700;
    color: #5631eb;
  }
  p {
    font-size: 33px;
    font-weight: 700;
    margin-bottom: 10px;
  }
  a {
    color: #ffff;
  }
}

.container-element-btn a {
  color: #fff;
}

.container-element-btn {
  width: 100%;
}
.layout-btn {
  width: 100%;
}

.layout-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
}

@media (max-width: 1400px) {
  .title-span {
    font-size: 48px;
    line-height: 56px;
    font-weight: 700;
    color: rgb(0, 0, 0);
  }
  .content-element {
    margin-top: 100px;
    width: 500px;
  }
  .subtitle-content {
    margin-top: 30px;
    font-size: 16px;
    line-height: 24px;
    font-weight: 400;
    color: rgb(0, 0, 0);
  }
}

@media (max-width: 800px) {
  .title-span {
    font-size: 42px;
    line-height: 56px;
    font-weight: 700;
    color: rgb(0, 0, 0);
  }
  .content-element {
    text-align: center;
    margin-top: 100px;
    width: 100%;
  }
  .container-btn {
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
.detail-img-desing {
  height: 200px;
  object-fit: cover;
  object-position: center;
}

.img-desing {
  width: 100%;
  height: 100%;
  border-radius: 25%;
}

.information-element-as {
  margin-top: 100px;
  margin-bottom: 100px;
  width: 800px;
  text-align: start;
  p {
    font-size: 33px;
    font-weight: 700;
    margin-bottom: 10px;
  }
}

.title-text-card {
  font-size: 16.5px;
}

.img-desing-card {
  object-fit: cover;
}
</style>