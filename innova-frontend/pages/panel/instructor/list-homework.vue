<template>
  <div class="container-md">
    <h2 class="my-3">Seleccione el Curso: </h2>

    <v-select
      :items="course_names"
      label="Selecciona el curso"
      v-model="select_item"
      solo
    ></v-select>
    <button
      class="button-font button-m btn-w"
      @click="filter_homework(select_item)"
    >
      filtrar
    </button>

    <v-row class="mt-3">
      <v-col sm="12">
        <v-card class="shadow-card content-card mt-2" rounded="xl">
          <v-list three-line>
            <v-list-item-group
              v-model="selectedItem"
              color="primary"
              v-if="homeworks_list"
            >
              <v-subheader v-text="'Tareas pendientes:'"></v-subheader>
              <div v-for="(item, index) in homeworks_list" :key="index">
                <v-list-item @click="select_homework(item.id)">
                  <v-list-item-avatar>
                    <v-icon class="blue" dark color="white">
                      mdi-clipboard-text
                    </v-icon>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title
                      v-html="item.get_course_info"
                    ></v-list-item-title>
                    <v-list-item-subtitle
                      v-html="'Profesor: ' + item.get_proffesorInfo"
                    ></v-list-item-subtitle>

                    <v-list-item-subtitle
                      class="text--primary"
                      v-text="item.title"
                    ></v-list-item-subtitle>
                  </v-list-item-content>

                  <v-list-item-action v-if="item.start_date && item.end_date">
                    <v-list-item-action-text
                      class="time-detail-desing"
                      v-text="
                        'tiempo faltante: ' +
                        date_homework(item.start_date, item.end_date)
                      "
                    ></v-list-item-action-text>
                  </v-list-item-action>

                </v-list-item>

                <v-divider
                  v-if="index < items.length - 1"
                  :key="index"
                ></v-divider>
              </div>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";
import { formatDistance } from "date-fns";

export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {
      homeworks_list: [],
      selectedItem: 0,
      course_names: [],
      items: [],
      select_item: "",
      current_id_course: "",
    };
  },
  methods: {
    select_homework(id) {
      this.$store.commit("set_id_homework_course",id);
      this.$router.push(`/panel/instructor/list`)
    },
    date_homework(start_date,end_date) {
      return formatDistance(new Date(start_date), new Date(end_date));
    },
    async filter_homework(selected_item) {
        if(selected_item){
        for (let it = 0; it < this.items.length; it++) {
            if (this.items[it].title === selected_item) {
            this.current_id_course = this.items[it].id;
            }
        }
        // realizar la busqueda de las tareas
        await this.get_homework_list(this.current_id_course);
      }
    },
    // devuelve los nombre se la busqueda (optimizar)
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


    async get_homework_list(course_id) {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/list_homework_profesor/${course_id}`,
        })
        .then((response) => {
          if (response.data != "error encontrado: ") {
            this.homeworks_list = response.data;
            console.log(this.homeworks_list);
          }
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },

  },
  mounted() {
    this.get_course_name();
  },
};
</script>

<style lang="scss" scoped>
.container-md {
  margin: 0 auto;
  width: 80%;
  max-width: 1300px;
  margin-top: 60px;
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