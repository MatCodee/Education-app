<template>
  <div class="margin-content">
    <v-toolbar class="gg">
      <v-tabs dark background-color="primary" grow>
        <v-tab @click="change_tab(1)">
          <v-badge color="pink" dot> Editar el Curso </v-badge>
        </v-tab>

        <v-tab @click="change_tab(2)">
          <v-badge color="green" content="6"> Editar las Clases </v-badge>
        </v-tab>

        <v-tab @click="change_tab(3)">
          <v-badge color="green" content="6"> Editar las Tareas </v-badge>
        </v-tab>
      </v-tabs>
    </v-toolbar>

    <!-- Esta es la opcion 1-->
    <div class="container-md" v-if="vista_select == 1">
      <v-row>
        <v-col md="7">
          <h2 class="mb-2">Informacion del Curso</h2>
          <p>Titulo</p>
          <v-text-field
            label="Titulo"
            v-model="request_data.title"
            solo
          ></v-text-field>
          <p>Subtitulo</p>
          <v-text-field
            label="Subtitulo"
            v-model="request_data.subtitle"
            solo
          ></v-text-field>

          <p>Descripcion</p>
          <v-textarea
            solo
            name="input-7-4"
            v-model="request_data.description"
            label="Descripcion del curso"
          ></v-textarea>

          <v-row>
            <v-col class="d-flex" cols="6" sm="4">
              <v-select
                :items="nivel"
                label="Nivel"
                v-model="request_data.level"
                solo
              ></v-select>
            </v-col>

            <v-col class="d-flex" cols="6" sm="4">
              <v-select
                :items="categoria"
                label="Categoria"
                solo
                v-model="request_data.category"
              ></v-select>
            </v-col>

            <v-col class="d-flex" cols="6" sm="4">
              <v-select
                :items="tipo_producto"
                label="Tipo de producto"
                solo
                v-model="request_data.tipo_producto"
              ></v-select>
            </v-col>
          </v-row>

          <v-btn rounded color="primary" @click="updateProffesorCourse" dark>
            Actualizar
          </v-btn>
        </v-col>
        <v-col md="5">
          <v-card class="mb-16 mt-16 full-padding-a">
            <p class="mb-5">Imagen del Curso</p>
            <div class="mb-16">
              <img
                :src="img_course_get"
                width="100%"
                alt="portfolio"
                class="portfolio-img"
              />
            </div>

            <div style="min-height: 4px">
              <v-progress-linear
                v-model="value"
                :active="show"
                :indeterminate="query"
                :query="true"
              ></v-progress-linear>
            </div>
            <input
              type="file"
              class="mt-5 mb-13"
              @change="previewFiles"
              multiple
            />
            <v-btn block color="primary" @click="updateImage" dark>
              Actualizar Imagen
            </v-btn>
          </v-card>
        </v-col>
      </v-row>
    </div>

    <!--Esta es la opcion 2-->
    <!-- -------------------------------------------------------------------------------------------------------------------------------------------------->

    <div class="container-md" v-if="vista_select == 2">
      <div class="margin-xl">

         <v-card class="max-auto pa-10 mb-16">
          <v-card-text>
            <v-row>
              <v-col>
                <div class="d-flex justify-star">
                  <p>Clases del Curso</p>
                </div>
              </v-col>
              <v-col>
                <div class="d-flex justify-end">
                  <v-btn color="primary" rounded @click="dialog = !dialog">
                    Crear una Semana de preparacion
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      <v-dialog v-model="dialog" width="70%">
          <v-card class="pa-16">
                <h2 class="mb-2">Crear una organizacion para la semana</h2>
                <p>Resumen de lo que se va a a ver</p>
                <v-textarea
                  solo
                  v-model="request_week.resumen"
                  name="input-7-4"
                  label="Solo textarea"
                  class="mt-10"
                ></v-textarea>
                <v-btn block color="primary" @click="create_week" dark>
                  Crear una semana de organizacion
                </v-btn>
          </v-card>
        </v-dialog>
    <v-row class="mt-3">
      <v-col sm="12">
        <v-card class="shadow-card content-card mt-2" rounded="xl">
          <v-list three-line>
            <v-list-item-group
              color="primary"
            >
              <v-subheader v-text="'Semanas definidas de estrategias:'"></v-subheader>
              <div v-for="(item, index) in request_data.course_data" :key="index">
                <v-list-item @click="select_week_class(item)">
                  <v-list-item-avatar>
                    <v-icon class="blue" dark color="white">
                      mdi-clipboard-text
                    </v-icon>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title
                      v-html="'Semana ' + item.id"
                    ></v-list-item-title>
                    <v-list-item-subtitle
                      v-html="'Profesor: ' + item.get_profesor"
                    ></v-list-item-subtitle>

                    <v-list-item-subtitle
                      class="text--primary"
                      v-text="item.resumen"
                    ></v-list-item-subtitle>
                  </v-list-item-content>
           

                </v-list-item>


              </div>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
    </v-row>



      </div>
    </div>


    <!-- -------------------------------------------------------------------------------------------------------------------------------------------------->

    <div class="container-md" v-if="vista_select == 3">
      <v-card class="max-auto pa-10 mb-16">
        <v-card-text>
          <v-row>
            <v-col>
              <div class="d-flex justify-star">
                <p>Tarea del curso</p>
              </div>
            </v-col>
            <v-col>
              <div class="d-flex justify-end">
                <v-btn
                  color="primary"
                  rounded
                  @click="dialog_homework = !dialog_homework"
                >
                  Crear una Tarea
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>

      <v-dialog v-model="dialog_homework" width="70%">
        <v-card class="pa-16">
          <v-row>
            <v-col md="7">
              <h2 class="mb-2">Creacion de una tarea</h2>
              <p>Titulo</p>
              <v-text-field
                label="Titulo"
                v-model="form_homework.title"
                solo
              ></v-text-field>
              <p>Descripcion de la tarea (opcional)</p>
              <v-textarea
                solo
                v-model="form_homework.description"
                name="input-7-4"
                label="Solo textarea"
                class="mt-10"
              ></v-textarea>

              <v-row>
                <v-col cols="12" lg="5">
                  <v-menu
                    ref="menu1"
                    v-model="menu1"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="form_homework.start_date"
                        label="Date"
                        hint="MM/DD/YYYY format"
                        persistent-hint
                        :rules="dateRules_start"
                        prepend-icon="mdi-calendar"
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="form_homework.start_date"
                      no-title
                      @input="menu1 = false"
                    ></v-date-picker>
                  </v-menu>
                  <p>
                    Date in ISO format: <strong>{{ date }}</strong>
                  </p>
                </v-col>

                <v-col cols="12" lg="5">
                  <v-menu
                    v-model="menu2"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="form_homework.end_date"
                        label="Date (read only text field)"
                        hint="MM/DD/YYYY format"
                        persistent-hint
                        :rules="dateRules_end"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="form_homework.end_date"
                      no-title
                      @input="menu2 = false"
                    ></v-date-picker>
                  </v-menu>
                  <p>
                    Date in ISO format: <strong>{{ date }}</strong>
                  </p>
                </v-col>
              </v-row>
            </v-col>
            <v-col md="5">
              <p>Agregar un link para complementar (opcional)</p>

              <div class="mb-2">
                <p>Agregar documento para complementar (opcional)</p>
              </div>

              <div style="min-height: 4px">
                <v-progress-linear
                  v-model="value"
                  :active="show"
                  :indeterminate="query"
                  :query="true"
                ></v-progress-linear>
              </div>
              <input
                type="file"
                @change="documentFile"
                class="mt-5 mb-13"
                multiple
              />
              <v-btn block color="primary" @click="add_homework" dark>
                Crear la tarea
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-dialog>



      <v-row>
        <v-col md="4">
          <h2 class="mb-12">Editar las tareas</h2>
          <v-list subheader two-line v-if="request_homework">
            <v-list-item
              v-for="homework,index in homeworks"
              :key="index"
            >
              <v-list-item-content>
                <v-list-item-title
                  v-text="homework.title"
                ></v-list-item-title>

                <v-list-item-subtitle
                  v-text="homework.description"
                ></v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-action>
                <v-btn
                  fab
                  dark
                  @click="edit_homework(homework)"
                  x-small
                  color="primary"
                >
                  <v-icon dark> mdi-pencil </v-icon>
                </v-btn>
              </v-list-item-action>
              <v-list-item-action>
                <v-btn
                  fab
                  dark
                  @click="dialog_delete(homework)"
                  x-small
                  color="primary"
                >
                  <v-icon dark> mdi-delete </v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </v-col>
        <v-col md="8">
          <h2 class="mb-2">Detalle de la tarea</h2>

          <div v-if="request_homework">
            <p>Titulo</p>
            <v-text-field
              label="Titulo"
              v-model="request_homework.title"
              solo
            ></v-text-field>

            <p>Resumen</p>
            <v-textarea
              solo
              v-model="request_homework.description"
              name="input-7-4"
              label="Solo textarea"
              class="mt-10"
            ></v-textarea>

            <v-card class="mb-16 mt-16 pa-16">

              <div style="min-height: 4px">
                <v-progress-linear
                  v-model="value"
                  :active="show"
                  :indeterminate="query"
                  :query="true"
                ></v-progress-linear>
              </div>
              <input type="file" class="mt-5 mb-13" multiple />
            </v-card>

            <v-card class="mb-16 mt-16 pa-16">
              <div class="mb-16">
                <p>Seleccione un Documento</p>
                <p>{{ request_class.document }}</p>
              </div>

              <div style="min-height: 4px">
                <v-progress-linear
                  v-model="value"
                  :active="show"
                  :indeterminate="query"
                  :query="true"
                ></v-progress-linear>
              </div>
              <input type="file" class="mt-5 mb-13" multiple />
            </v-card>
          </div>
          
          <v-row>

                <v-col cols="12" lg="6">
                  <v-menu
                    ref="menu1"
                    v-model="menu_homework_deatil1"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="request_homework.start_date"
                        label="Date"
                        hint="MM/DD/YYYY format"
                        persistent-hint
                        :rules="dateRules_start"
                        prepend-icon="mdi-calendar"
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="request_homework.start_date"
                      no-title
                      @input="menu_homework_deatil1 = false"
                    ></v-date-picker>
                  </v-menu>
                </v-col>

                <v-col cols="12" lg="6">
                  <v-menu
                    v-model="menu_homework_deatil2"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="request_homework.end_date"
                        label="Date (read only text field)"
                        hint="MM/DD/YYYY format"
                        persistent-hint
                        :rules="dateRules_end"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="request_homework.end_date"
                      no-title
                      @input="menu_homework_deatil2 = false"
                    ></v-date-picker>
                  </v-menu>
                </v-col>
        

          </v-row>
          <v-btn color="primary mt-6" @click="update_homework" dark>
            Actualizar
          </v-btn>

          <v-dialog v-model="delete_bol" max-width="400">
            <v-card class="mx-auto pa-12">
              <v-card-subtitle class=""> Eliminar la clase </v-card-subtitle>

              <v-card-text class="text--primary">
                <div>Estas seguro que quieres elminar la clase?</div>
              </v-card-text>

              <v-card-actions>
                <v-btn color="primary" text @click="delete_homework"> Eliminar </v-btn>

                <v-btn color="primary" text @click="delete_bol = !delete_bol">
                  Cancelar
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";
export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {
      // detail class
      detail_class: {},
      class_names: [],




      vista_select: 1,
      // propiedades del progress
      value: 0,
      query: false,
      show: true,
      interval: 0,


      request_week: {
        course_week: "",
        resumen: "",
      },

      img_course_get: null,

      nivel: ["Todos los niveles", "Basico", "Intermedio", "Avanzado"],
      categoria: [
        "Tegnologia",
        "Administracion",
        "Negocios",
        "Contabilidad",
        "Comunicacion",
      ],
      tipo_producto: ["Curso", "Programa Especializados"],

      id_author: "",
      id_course: "",

      request_data: {
        author: "",
        title: "",
        subtitle: "",
        description: "",
        level: "",
        category: "",
        tipo_producto: "",
        img_course: null,
        get_image: null,
      },
      request_data_img: {
        author: -1,
        img_course: null,
      },

      dialog: false,
      dialog_homework: false,
      delete_bol: false,
      // consulta de la aplicacion actualizacion de la clase
      request_class: [],





      // formularios de las tareas
      homeworks: [],
      request_homework: {
        id: "",
        profesor: "",
        course: "",
        title: "",
        description: "",
        start_date: null,
        end_date: null,
      },

      form_homework: {
        title: "",
        description: "",
        start_date: null,
        end_date: null,
      },
      // controles de los input del calendario

      // reglas de la fecha
      current_time: this.parse_picke_time(new Date()),
      rules_control_start_date: false,
      rules_control_end_date: false,
      dateRules_start: [
        (v) => !!v || "Name is required",
        (v) => this.rules_control_start_date || "Fecha es anterior a la actual",
      ],
      dateRules_end: [
        (v) => !!v || "Name is required",
        (v) => this.rules_control_end_date || "Fecha es anterior a la actual",
      ],

      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      //dateFormatted: vm.formatDate((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)),
      menu1: false,
      menu2: false,
      menu_homework_deatil1: false,
      menu_homework_deatil2: false,
    };
  },

  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },
  watch: {
    date(val) {
      this.dateFormatted = this.formatDate(this.date);
    },
    'request_homework.title': function (new_title) {
      console.log(this.request_homework.title);
    },
    'form_homework.start_date': function(new_picker){
      if(this.form_homework.start_date >= this.date){
        this.rules_control_start_date = true;
      }else {
        this.rules_control_start_date = false;   
      }
    },
    'form_homework.end_date': function (new_picker) {
      if(this.form_homework.end_date > this.date){
        this.rules_control_end_date = true;
      }else {
        this.rules_control_end_date = false;   
      }
    },
    'request_homework.start_date': function(new_picker){
      if(this.request_homework.start_date >= this.date){
        this.rules_control_start_date = true;
      }else {
        this.rules_control_start_date = false;   
      }
    },
    'request_homework.end_date': function (new_picker) {
      if(this.request_homework.end_date > this.date){
        this.rules_control_end_date = true;
      }else {
        this.rules_control_end_date = false;   
      }
    }
  },
  methods: {
    // funciones de la fecha
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${month}/${day}/${year}`;
    },

    change_tab(number) {
      this.vista_select = number;
    },
    previewFiles(event) {
      this.request_data_img.img_course = event.target.files[0];
    },

    // Funcines establecidas del homework
    parse_picke_time(date) {
      let d = new Date(date);
      let format_pickle = d.getFullYear() + "-" + (d.getMonth()+1) + "-" + (d.getDate()+1);
      return format_pickle
    },
    compare_picker_time_start(date_start) {
      let current = this.parse_picke_time(new Date())
      if(current  >= date_start){
        this.rules_control_start_date = true;
      }
    },
    compare_picker_time_end(date_end) {
      let current = this.parse_picke_time(new Date())
      if(current  >= date_end){
        this.rules_control_end_date = true;
      }
    },

    edit_homework(homework) {
      this.request_homework = homework;
      this.request_homework['start_date'] = this.parse_picke_time(homework['start_date']);
      this.request_homework['end_date'] = this.parse_picke_time(homework['end_date']);
      console.log(this.request_class);
    },

    async add_homework() {
      let token = localStorage.getItem("token");
      let form = new FormData();
      form.append("title", this.form_homework.title);
      form.append("description", this.form_homework.description);
      form.append("start_date", this.form_homework.start_date);
      form.append("end_date", this.form_homework.end_date);
      form.append("profesor", this.id_author);
      form.append("course", this.request_data.id);
      await this.$axios
        .request({
          method: "post",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/add_homework/`,
          data: form,
        })
        .then((result) => {
          console.log(result.data);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },

    async get_homework() {
      // list_homework_profesor/<course_id>
      let token = localStorage.getItem("token");
      let course_slug = this.$store.state.slug_course_proffesor;
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/list_homework_profesor_slug/${course_slug}`,
        })
        .then((result) => {
          this.homeworks = result.data;
          console.log(result.data);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    async update_homework() {
      let token = localStorage.getItem("token");
      let form = new FormData();
      form.append("title", this.request_homework.title);
      form.append("description", this.request_homework.description);
      form.append("start_date", this.request_homework.start_date);
      form.append("end_date", this.request_homework.end_date);
      form.append("profesor", this.id_author);
      form.append("course", this.request_homework.course);
      await this.$axios
        .request({
          method: "put",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/update_list_homework_profesor/${this.request_homework.id}`,
          data: form,
        })
        .then((result) => {
          console.log(result.data);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    async delete_homework() {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "delete",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/update_list_homework_profesor/${this.request_homework.id}`,
        })
        .then((result) => {
          console.log(result.data);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    
    
    async create_week() {
      let token = localStorage.getItem("token");
      this.request_week.course_week = this.request_data.id;
      await this.$axios
        .request({
          method: "post",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/create_week/`,
          data: this.request_week,
        })
        .then((result) => {
          console.log(result.data);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },

    //--------------------------------------------------------------------------------------------
    select_week_class(week) {
      this.$store.commit("set_id_week",week.id);
      this.$store.commit("week_delected",week.get_fullpath_link);
      console.log(week.get_fullpath_link);
      console.log(week);
      // podemos guardar ne el localhost
      this.$router.push(`/panel/instructor/detail-class`)
    },
    //funciones de actualizacion del cursod de profesor
    async updateImage() {
      let slug = this.$store.state.slug_course_proffesor;
      // comprobacion de los campos directamente en la funcion

      let token = localStorage.getItem("token");
      let df = new FormData();
      df.append("img_course", this.request_data_img.img_course);
      df.append("author", this.request_data_img.author);

      await this.$axios
        .request({
          method: "put",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/update_proffesor_course_img/${slug}`,
          data: df,
        })
        .then((result) => {
          this.id_course = result.data.id;
          console.log(result.data);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    async updateProffesorCourse() {
      let slug = this.$store.state.slug_course_proffesor;
      // comprobacion de los campos directamente en la funcion

      let token = localStorage.getItem("token");
      let df = new FormData();

      df.append("title", this.request_data.title);

      df.append("subtitle", this.request_data.subtitle);
      df.append("description", this.request_data.description);
      df.append("level", this.request_data.level);

      df.append("category", this.request_data.category);
      df.append("tipo_producto", this.request_data.tipo_producto);
      df.append("author", this.id_author);

      if (this.request_data.img_course) {
        df.append("img_course", this.request_data.img_course);
      }

      await this.$axios
        .request({
          method: "put",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/update_proffesor_course/${slug}`,
          data: df,
        })
        .then((result) => {
          //console.log("Mostrando la informaicon de los cursos: ")
          //console.log(result.data);
          console.log(result.data);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },



    async getCourseProffesor() {
      // comprobacion de los campos directamente en la funcion
      let slug = this.$store.state.slug_course_proffesor;
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/detail-course/${slug}`,
        })
        .then((result) => {
          this.img_course_get = result.data["get_image"];
            this.items = result.data;

          // obteniendo la ifnormacion del usuario
          this.request_data = result.data;
          console.log(this.request_data)
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    queryAndIndeterminate() {
      this.query = true;
      this.show = true;
      this.value = 0;

      setTimeout(() => {
        this.query = false;

        this.interval = setInterval(() => {
          if (this.value === 100) {
            clearInterval(this.interval);
            this.show = false;
            return setTimeout(this.queryAndIndeterminate, 2000);
          }
          this.value += 25;
        }, 1000);
      }, 2500);
    },

    dialog_delete(class_data) {
      this.delete_bol = !this.delete_bol;
      this.request_class = class_data;
    },
    // funciones de botones de clases
    edit_class(class_data) {
      this.request_class = class_data;
      console.log(this.request_class);
    },
    documentFile(event) {
      this.form_class.document = event.target.files[0];
    },

  },
  computed: {},
  mounted() {
    //TODO: en esta funcion estamos llamando a todos los metodos esto puede causar retraso optimizar cuando se tenga que optimizar
    this.queryAndIndeterminate();
    this.request_data.author = parseInt(localStorage.getItem("id_proffesor"));
    this.id_author = parseInt(localStorage.getItem("id_proffesor"));

    this.get_homework();
    //console.log(typeof(this.request_data.author));
    console.log("id del author: ", this.request_data.author);
    this.request_data_img.author = parseInt(
      localStorage.getItem("id_proffesor")
    );
    this.getCourseProffesor();
  },
  beforeDestroy() {
    clearInterval(this.interval);
  },
};
</script>

<style lang="scss" scoped>
.margin-content {
}

.container-md {
  margin: 0 auto;
  width: 80%;
  padding-top: 150px;
}

.portfolio-img {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
.gg {
  top: 60px;
  width: 100%;
  position: fixed;
  z-index: 1;
}

.full-padding-a {
  padding: 20px;
}
</style>
