<template>
  <div class="container-md ">
    <h1>Administracion de estudiantes de los cursos</h1>

      <v-row class="mt-2" v-if="courses.data != 'error'">
        <v-col lg="3" md="3" sm="3" cols="12" class="align-self-start">
          <v-list subheader>
            <v-list-item v-for="course in courses" :key="course.id">
              <v-list-item-content>
                <h4>{{course.title}}</h4>
              </v-list-item-content>

              <v-list-item-action>
                <v-btn  
                  class="mx-2"
                  fab
                  dark
                  x-small
                  color="primary"
                  @click="select_couse(course)"
                >
                  <v-icon dark> mdi-pencil </v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </v-col>
        <v-col lg="9" md="9" sm="9" cols="12">
          <v-data-table
            :headers="headers"
            :items="desserts"
            sort-by="calories"
            class="elevation-1"
          >
            <template v-slot:top>
              <v-toolbar flat>
                <v-toolbar-title>Panel de Adinistracion: </v-toolbar-title>
                <v-divider class="mx-4" inset vertical></v-divider>
                <v-spacer></v-spacer>

                
              
                    <v-btn
                      color="primary"
                      dark
                      rounded
                      class="mb-2"
                      @click="dialog = !dialog"
                      v-if="select_option"
                    >
                      Agregar Estudiante
                    </v-btn>
              
                <v-dialog v-model="dialog" max-width="500px">
                  <v-card>
                    <v-card-title>
                      <span class="mt-16 text-h5">
                        Seleccione la busqueda por nombre de usuario o correo del usuario
                      </span>
                    </v-card-title>

                    <v-card-text>
                      <v-container>
  
                            <v-text-field
                              v-model="username_select"
                              label="filtrar usuario"
                            ></v-text-field>

                            <v-btn small color="primary" @click="filterUser">
                                filtrar
                            </v-btn>
                      </v-container>
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="close">
                        Cancelar
                      </v-btn>
                      <v-btn color="blue darken-1" text @click="save">
                        Guardar
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <v-dialog v-model="dialogDelete" max-width="500px">
                  <v-card>
                    <v-card-title class="text-h5">
                      Seguro que deseas eliminar a este estudiante?
                    </v-card-title>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="closeDelete"
                        >Cancelar</v-btn
                      >
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="deleteItemConfirm"
                        >Aceptar</v-btn
                      >
                      <v-spacer></v-spacer>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-toolbar>
            </template>

            <template v-slot:[`item.actions`]="{ item }">
              <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
            </template>

            <template v-slot:[`item.last_connect`]="{ item }">
              {{current_time_compare(item.last_connect) }}
            </template>
    
            <template v-slot:[`item.image_user`]="{ item }">
              <img class="image-user-desing" :src="item.image_user" alt="" />
            </template>
          </v-data-table>
        </v-col>
      </v-row>
    </div>

</template>

<script>
import {path} from "@/api/conf_api";
import moment from 'moment';

const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {

      username_select: '',
      user_filter_result: {},

      select_option: false,
      courses: [],
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: "Imagen", value: "image_user", sortable: false },
        {
          text: "Nombre de Usuario",
          align: "start",
          sortable: false,
          value: "username",
        },
        { text: "Nombre completo", value: "fullname" },
        { text: "Correo", value: "email" },
        { text: "Ultima conectado", value: "last_connect" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      desserts: [],
      slug_principal: "",
      editedIndex: -1,
      filter_op: "",
      editedItem: {
        image_user: "",
        username: "",
        fullname: "",
        email: "",
      },
      defaultItem: {
        image_user: "",
        username: "",
        fullname: "",
        email: "",
      },
    };
  },
  methods: {
    difference(date1, date2) {  
      //const date1utc = Date.UTC(date1.getFullYear(), date1.getMonth(), date1.getDate());
      //const date2utc = Date.UTC(date2.getFullYear(), date2.getMonth(), date2.getDate());
      const total_fecha = Math.abs(date1 - date2);
      let res_minutes = parseInt(total_fecha/(1000*60));
      
      let resto_hour = 0;
      let resto_days = 0;

      if(res_minutes >= 60) {
        resto_hour = parseInt(res_minutes / 60);
        res_minutes = res_minutes % 60;
      }
      if(resto_hour >= 24) {
        console.log("Entro aqui");
        resto_days = parseInt(resto_hour / 24);
        resto_hour = resto_hour % 24;
      }

      if(resto_days != 0) {
        return `${resto_days} Dias ${resto_hour} horas ${res_minutes} minutos`;
      }else {
        return `${resto_hour} horas ${res_minutes} minutos`;
      }

    },
    current_time_compare(last_date) {
        moment.locale();
        console.log(last_date);
        console.log(`${moment().toISOString(true).substring(0, 19)}Z`);

        //let current_date = new Date(moment().format());
        //let lastDate = new Date(last_date);

        let current_date = new Date(`${moment().toISOString(true).substring(0, 19)}Z`).getTime();
        let lastDate = new Date(last_date).getTime();
        
        //let data = this.difference(current_date,lastDate);
        //console.log(data);
        
        //console.log("Actual fecha");
        //console.log(current_date);
        //console.log("Fecha del Usuario");
        //console.log(lastDate);

        //let total_hora =  new Date(Math.abs(current_date - lastDate));
        //console.log(total_hora);
        //return `${total_hora.getDay()} Dias ${total_hora.getHours()} horas ${total_hora.getMinutes()} minutos`
        return this.difference(current_date,lastDate);
    },
    edit_course(slug) {
      this.$store.commit("removeSlugProffesor");
      this.$store.commit("setSlugProffesor", slug);
      this.$router.push("/proffesor-pages/detailCourse/");
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
          this.courses = response.data;
        })
        .catch(function (error) {
          console.log("error encontrado: " + error);
        });
    },
    genRandomIndex(length) {
      return Math.ceil(Math.random() * (length - 1));
    },

    initialize() {
      console.log(this.desserts);
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.desserts.splice(this.editedIndex, 1);


      console.log(this.editedItem);
      this.deleteUser(this.editedItem);
      //Eliminamos la persona del curso
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;

      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.addUser(this.editedItem);
        this.desserts.push(this.editedItem);

        // Agregamos el cambio del usuario
      }
      this.close();
    },
    select_couse(course) {
      this.slug_principal = course.slug;
      this.select_option = true;
      this.getUsers();
    },
    async filterUser() {
      if(this.username_select) {
        let token = localStorage.getItem("token");
        await this.$axios
          .request({
            method: "get",
            headers: { Authorization: "Token " + token },
            baseURL: path + `/courses/filter_user_course/${this.username_select}`,
          })
          .then((response) => {
            console.log(response.data);
            this.user_filter_result = response.data;
          })
          .catch(function (error) {
            console.log("error encontrado: " + error);
          });
      }
    },
    async addUser(item) {
      if(this.slug_principal != "") {
        let token = localStorage.getItem("token");
        let formData = {
          course_slug: this.slug_principal,
          user: this.user_filter_result.username,
        }
        console.log(formData);
        await this.$axios
          .request({
            method: "post",
            headers: { Authorization: "Token " + token },
            baseURL: path + `/courses/add_user_couse/`,
            data:formData,
          })
          .then((response) => {
            console.log(response.data);
          })
          .catch(function (error) {
            console.log("error encontrado: " + error);
          });
      }
    },
    async deleteUser(item) {
      if (this.slug_principal != "") {
        let token = localStorage.getItem("token");
        let formData = {
          username: item.username,
        }
        await this.$axios
          .request({
            method: "post",
            headers: { Authorization: "Token " + token },
            baseURL: path + `/courses/delete_user_course/${this.slug_principal}`,
            data:formData,
          })
          .then((response) => {
            console.log(response.data);
          })
          .catch(function (error) {
            console.log("error encontrado: " + error);
          });
      }
    },
    async getUsers() {
      if (this.slug_principal != "") {
        let token = localStorage.getItem("token");
        await this.$axios
          .request({
            method: "get",
            headers: { Authorization: "Token " + token },
            baseURL: path + `/courses/get_user_course/${this.slug_principal}`,
          })
          .then((response) => {
            this.desserts = response.data;
            console.log(this.desserts);
          })
          .catch(function (error) {
            console.log("error encontrado: " + error);
          });
      }
    },
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  created() {
    this.initialize();
  },
  mounted() {
    this.getCourseProffesor();
  },
};
</script>

<style lang="scss" scoped>

.container-md {
  width: 80%;
  margin: 100px auto;
}


.image-user-desing {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  object-fit: cover;
}
</style>
