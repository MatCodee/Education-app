<template>
    <div>
        <h2>Lista de los formularios: </h2>
        <p class="mt-5">Seleccione el curso: </p>
        <v-select
          :items="course_names"
          label="Selecciona el curso"
          v-model="select_item"
          solo
        ></v-select>
        <button
          class="button-font button-m btn-w"
          @click="get_form_course(select_item)"
        >
          filtrar
        </button>
        <v-card class="shadow-card content-card mt-5" rounded="xl">
          <v-list three-line>
            <v-list-item-group color="primary">
                <v-subheader
                  v-text="'Pruebas Creadas:'" 
                ></v-subheader>
              <div v-for="item,index in list_form" :key="index">
                <v-list-item @click="detail_form_click(item)">
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
                    <v-list-item-title v-html="item.title"></v-list-item-title>

                    <v-list-item-subtitle
                      class="text--primary"
                      v-text="item.description"
                    ></v-list-item-subtitle>


                  </v-list-item-content>
                </v-list-item>
                

              </div>
            </v-list-item-group>
          </v-list>
        </v-card>
    </div>
</template>


<script>
import { path } from "@/api/conf_api";

export default {
    data() {
        return {
          course_names: [],
          select_item: "",
          items: [],
          list_form: [],
        }
    },
    methods: {
      async detail_form_click(form) {
        console.log(form);
        this.$store.commit("change_form",form);
        this.$router.push(`/global/detail_form`)
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
      async get_form_course(selected_item_query) {
        if(selected_item_query) {
          console.log(selected_item_query);
          let token = localStorage.getItem("token");

          await this.$axios
            .request({
              method: "get",
              headers: { Authorization: "Token " + token },
              baseURL: path + `/exam/get_all_evaluation/${selected_item_query}`,
            })
            .then((response) => {
              console.log(response.data)
              this.list_form= response.data;
            })
            .catch(function (error) {
              console.log("error encontrado: " + error);
            });
        }
      },
    },
    mounted() {
      this.get_course_name();
    },
}
</script>


<style lang="scss" scoped>
.shadow-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
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