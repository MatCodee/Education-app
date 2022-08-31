<template>
  <div class="container-md">
    <h2 class="ml-5">Hola, Matías. ¡Te damos la bienvenida a LixFux!</h2>


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
                <v-list-item @click="select_homework(item)">
                  <v-list-item-avatar>
                       <v-img :src="item.get_UserImage"></v-img>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title
                      v-html="item.get_UserInfo"
                    ></v-list-item-title>
                    <v-list-item-subtitle
                      v-html="item.get_course_info"
                    ></v-list-item-subtitle>

                    <v-list-item-subtitle
                      class="text--primary"
                      v-text="item.title"
                    ></v-list-item-subtitle>
                  </v-list-item-content>

                  <v-list-item-action v-if="item.created_at">
                    <v-list-item-action-text
                      class="time-detail-desing"
                      v-text="
                        'tiempo de envio: ' + date_homework(item.created_at)
                      "
                    ></v-list-item-action-text>
                    <v-list-item-action-text
                     class="desing-font-send"
                      v-text="complete_homework(item.completed)"
                    ></v-list-item-action-text>
                  </v-list-item-action>
                </v-list-item>

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
    selectedItem: "",
    };
  },
  methods: {
    select_homework(item) {
      this.$store.commit("set_id_homework",item.homework);
      this.$store.commit("set_id_homework_send",item.id);
      this.$router.push(`/panel/instructor/list-homework-detail/`)
    },
    complete_homework(completed) {
      if(completed) {
        return "Enviado";
      }else {
        return "Sin enviar";
      }
    },
    date_homework(date) {
      let d = new Date(date);
      let formtat = d.getFullYear() + "/" + (d.getMonth() + 1) + "/" + d.getDate() + "  hora: " + d.getHours() + "-" + d.getMinutes() + "-" +  d.getSeconds();
      return formtat;
    },

    async get_homework_list() {
      let token = localStorage.getItem("token");
      let id_homework = this.$store.state.current_id_homework_course;
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/list_homework_student/${id_homework}`,
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
    this.get_homework_list();
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
.time-detail-desing {
  font-size: 16px;
  font-weight: 600;
}

.desing-font-send {
  font-size: 16px;
  font-weight: 900;
}
</style>