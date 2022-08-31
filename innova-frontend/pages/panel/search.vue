<template>
    <div class="margin-content container-md">
        <h2> Resultados de la Busqueda: {{query}}</h2>
  
        <v-row class="mt-4 mb-5">
          <v-col sm="12" md="4" lg="4" xl="3"  v-for="course in courses_search" :key="course.id">
          <v-card
            class="layout-card"
            
            rounded="lg"
          >
            <v-img
              :src="course.get_image"
              @click="detail_course(course.slug)"
              class="detail-img-desing"

            ></v-img>
            <div class="padd-content-card">
              <v-card-title class="title-text-card">
                {{course.title.substring(0, 24)}}
              </v-card-title>

              <v-card-subtitle class="subtitle-text-card">
                Por Cecilia Hugony
              </v-card-subtitle>

              <v-card-actions>
                <div class="container-element-btn">
                  <button @click="detail_course(course.slug)" class="layout-btn button-font button-m ">Inscribite ahora</button>
                </div>
              </v-card-actions>
            </div>
          </v-card>
          </v-col>
        </v-row>
          
    </div>
</template>


<script>
import {path} from "@/api/conf_api";
export default {
    layout: "LayoutPanel",
    data() {
        return {
            courses_search: [],
            query: '',
        }
    },
    mounted() {
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)
        if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods: {
    detail_course(slug) {
      // guardamos el slug del curso
      // mandamos un push a detail course\
      console.log(slug)
      localStorage.setItem("slug_course",slug);

      this.$router.push('detail-course'); 
    },
        async performSearch() {
            let token = localStorage.getItem("token");
            await this.$axios.request({
                    method: "post",
                    headers: { Authorization: `Token ${token}`},
                    baseURL: path + `/courses/search`,
                    data: {'query': this.query},
                })
                .then(response => {
                    this.courses_search= response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
    }
}
</script>


<style lang="scss" scoped>
.container-md {
  width: 80%;
  margin: 0 auto;
}
.margin-content {
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

.detail-img-desing {
  height: 200px;
  object-fit: cover;
  object-position: center;
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
.container-element-btn {
  width: 100%;
}

.button-m {
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    background-color: white; 
    border: solid 3px #5631eb;
    transition: background-color .35s ease-in-out,color .15s ease-in-out,border .15s ease-in-out;
    height: 48px;
    width: 100%;
    padding-left: 40px;
    padding-right: 40px;
    border-radius: 5px;
    color: #5631eb;
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

</style>
