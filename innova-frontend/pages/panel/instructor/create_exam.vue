<template>
  <div>
    <v-toolbar class="gg">
      <v-tabs dark background-color="primary" grow>
        <v-tab @click="change_tab(1)">
          <v-badge color="pink" dot> Crear un formulario </v-badge>
        </v-tab>

        <v-tab @click="change_tab(2)">
          <v-badge color="green" content="6"> Ver formularios </v-badge>
        </v-tab>

      </v-tabs>
    </v-toolbar>

    <!-- Esta es la vista numero 1 ----------------------------------------------------- -->
    <div class="container-md" v-if="vista_select == 1">
      <h2>Creacion de una evaluacion:</h2>
      <div class="d-flex">
        <div class="content-box">
          <div class="principal-box">
            <p>Seleccionar el tipo de formulario</p>
            <v-select
              :items="type_form"
              label="Tipo de formulario"
              v-model="form.type_form"
              solo
            ></v-select>
            <p>
              Definir el rango de fecha en que va a estar disponible la encuwsta
              o evaluacion
            </p>
            <TimeCardConfigure />
            <div class="mt-3">
              <v-text-field v-model="form.title" label="Formulario sin titulo"></v-text-field>
              <v-text-field v-model="form.description" label="Description del formulario"></v-text-field>
            </div>
          </div>
          <div v-for="(item, index) in form_question" :key="index">
            <div v-if="item.question_type == 'short_text'">
              <ShortQuestion
                @click="delete_component(item)"
                :index="index"
                v-model="item.question_text"
              />
            </div>
            <div v-if="item.question_type == 'long_text'">
              <LongQuestion
                @click="delete_component(item)"
                v-model="item.question_text"
              />
            </div>
            <div v-if="item.question_type == 'multiple_text'">
              <!--
              <SelectionQuestion
                @click="delete_component(item)"
                :index="index"
              />
              -->

              <div class="card-box mt-4">
                <v-text-field v-model="item.question_text" label="Ingrese la Pregunta"></v-text-field>
                <div class="d-flex">
                  <v-text-field class="field_option" v-on:keyup.enter="add_option(item)"  v-model="option_text" label="Opcion"/>
                  <v-btn class="mx-2 mt-1" @click="add_option(item)" fab dark x-small color="primary">
                    <v-icon dark> mdi-plus </v-icon>
                  </v-btn>
                </div>
              
                <div v-if="item.choices_relations && options_select">
                  <v-radio-group :change="options_select[index]">
                      <div class="d-flex" v-for="(n,index) in item.choices_relations" :key="index">
                        <v-radio
                          class="field_radio_button"
                          :key="index"
                          :label="`${n.choice_text}`"
                          :value="n.choice_text"
                        ></v-radio>
                      <v-btn icon @click="delete_option_select(index,item.choices_relations)">
                        <v-icon>mdi-close</v-icon>
                      </v-btn>
                    </div>
                  </v-radio-group>
                </div>

                <div>
                  <v-btn class="mx-2 mt-1" fab dark x-small color="primary">
                    <v-icon dark> mdi-update </v-icon>
                  </v-btn>
                  <v-btn class="mx-2 mt-1" @click="delete_component" fab dark x-small color="primary">
                    <v-icon dark> mdi-delete </v-icon>
                  </v-btn>
                </div>
              </div>


            </div>
          </div>
          <v-btn depressed color="primary" @click="add_form" class="mt-3">
            Terminar
          </v-btn>
        </div>
        <div class="secundary-box-vertical">
          <v-btn
            class="mx-2 mt-1"
            @click="create_short_question"
            fab
            dark
            small
            color="primary"
          >
            <v-icon dark> mdi-plus </v-icon>
          </v-btn>
          <v-btn
            class="mx-2 mt-1"
            @click="create_long_question"
            fab
            dark
            small
            color="primary"
          >
            <v-icon dark> mdi-ab-testing </v-icon>
          </v-btn>
          <v-btn
            class="mx-2 mt-1"
            @click="create_multiple_selection_question"
            fab
            dark
            small
            color="primary"
          >
            <v-icon dark> mdi-checkbox-blank-circle-outline </v-icon>
          </v-btn>
        </div>
      </div>
    </div>
    <!-- Esta es la vista numero 1 ----------------------------------------------------- -->

    <!---  Listar los formularios de encuestas o evaluaciones --------------------------  ---->
    <div class="container-md" v-if="vista_select == 2">
      <ListForm />
    </div>
    <!---  Listar los formularios de encuestas o evaluaciones --------------------------  ---->

    <!---  Configuracion de los formularios                   --------------------------  ---->

    <!---  Listar los formularios de encuestas o evaluaciones --------------------------  ---->
  </div>
</template>

<script>
import { path } from "@/api/conf_api";
import ShortQuestion from "~/components/form_card_panel/ShortQuestion.vue";
import LongQuestion from "~/components/form_card_panel/LongQuestion.vue";
import SelectionQuestion from "~/components/form_card_panel/SelectionQuestion.vue";
import TimeCardConfigure from "~/components/form_card_panel/TimeCardConfigureStart.vue";

import ListForm from "~/components/Form/ListForm.vue";
import ConfForm from "~/components/Form/ConfForm.vue";



export default {
  components: { ShortQuestion },
  layout: "LayoutPanelProffesor",
  data() {
    return {
      vista_select: 1,
      options_select: [],
      form_question: [],
      form :{
        title: "",
        description: "",
        type_form: "",
        is_active: true,
        evaluation: 5
      },
      type_form: ["Prueba", "Encuesta"],
      option_text: "",
      // este es para mostrar todos los formularios creados
      list_form: [],
    };
  },
  components: {
    ShortQuestion,
    LongQuestion,
    SelectionQuestion,
    TimeCardConfigure,
    ListForm,
    ConfForm,
  },
  computed: {
  },
  methods: {
    change_tab(number) {
      this.vista_select = number;
    },
    delete_component(index) {
      this.form_question.splice(index,1);
      //this.$store.commit('delete_question',index);
    },
    create_short_question() {
      let form = {
        question_text: "",
        question_type: "short_text",
      };
      //this.$store.commit('add_question',form);
      this.form_question.push(form);
      this.options_select.push(0);
    },
    create_long_question() {
      let form = {
        question_text: "",
        question_type: "long_text",
      };
      //this.$store.commit('add_question',form);
      this.form_question.push(form);
      this.options_select.push(0);
    },
    create_multiple_selection_question() {
      let form = {
        question_text: "",
        choices_relations: [],
        question_type: "multiple_text",
      };
      console.log(form);
      //this.$store.commit('add_question',form);
      this.form_question.push(form);
      this.options_select.push(0);
    },
    add_option(item) {
      if(this.option_text) {
        item.choices_relations.push({
          choice_text:this.option_text,
          is_correct: false,
        });
        this.option_text = "";
      }
    },
    delete_option_select(index,options) {
      options.splice(index,1);
    },
    // funciones  para acceder a la base de datos:
    async add_questions(id_form) {
      console.log("Entro aqui");
      let token = localStorage.getItem("token");

      for(let i=0;i<this.form_question.length;i++) {
        this.form_question[i]['form'] = id_form;
      }
      console.log(this.form_question);
      await this.$axios
        .request({
          method: "post",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/exam/question/`,
          data: this.form_question
        })
        .then((response) => {
          console.log(response.data)
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });  
    },
    // selecciona la opcion correcta y la agrega al formulario que se le va a enviar al servidor
    detect_answer_option() {
      for(let i=0;i<this.form_question.length;i++) {
        if(this.form_question[i].question_type == "multiple_text") {
          for(let j=0;j<this.form_question[i].choices_relations.length;j++) {
            if(this.options_select[i] == j) {
              this.form_question[i].choices_relations[j].is_correct = true;
              break;
            }
          } 
        }
      }
    },
    async add_form() {
      this.detect_answer_option();
      let token = localStorage.getItem("token");
      console.log(this.form);
      await this.$axios
        .request({
          method: "post",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/exam/form/`,
          data: this.form
        })
        .then((response) => {
          console.log("Devolver una respuesta: ");
          console.log(response.data)
          this.add_questions(response.data['id']);
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });  
    },


    // Esta es la segunda pestaña
    async get_forms() {
      // traemos todos los formularios
      let token = localStorage.getItem("token");

      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/exam/form/`,
        })
        .then((response) => {
            this.list_form = response.data;
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });  
    }
  },
  created() {
    this.get_forms();
  }
};
</script>


<style lang="scss" scoped>
.container-md {
  margin: 0 auto;
  width: 60%;
  margin-top: 150px;
}
.content-box {
  width: 100%;
  margin-top: 10px;
  margin-right: 10px;
}

.principal-box {
  width: 100%;
  padding: 20px 40px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
}
.secundary-box-vertical {
  margin-top: 10px;
  max-width: 60px;
  max-height: 170px;
  padding: 20px 2px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
}
.gg {
  top: 60px;
  width: 100%;
  position: fixed;
  z-index: 1;
}



/* Campos de los input */
.card-box {
  width: 100%;
  padding: 20px 40px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
}

.field_option {
  max-width: 400px;
}

.field_radio_button {
  width: 95%;
}

</style>