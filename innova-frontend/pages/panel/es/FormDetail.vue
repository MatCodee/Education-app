<template>
    <div class="container-md">
        <h1>Detalle de la evaluacion </h1>
        <div class="mt-5">
            <h2>{{form.title}}</h2>
            <p>{{form.description}}</p>
        </div>

        <div class="mt-10" v-for="(item,index) in form.questions_relations" :key="index">
            <div v-if="item.question_type == 'short_text'">
                <!--
                <ShortQuestion v-model="answer_form[index].answer_text" :question_short="item" />
                -->
                <div class="card-box mt-4">
                    <h3>{{item.question_text}}</h3>
                    <v-text-field
                        v-model="answer_form[index].answer_text"
                        label="Responder pregunta"
                    ></v-text-field>
                </div>
            </div>
            <div v-if="item.question_type == 'long_text'">
                <!--
                <LongQuestion v-model="answer_form[index].answer_text" :question_long="item"/>
                -->
                <div class="card-box mt-4">
                    <h3>{{item.question_text}}</h3>
                    <v-textarea
                        v-model="answer_form[index].answer_text"
                        label="Responder pregunta"
                    ></v-textarea>
                </div>
            </div>
            <div v-if="item.question_type == 'multiple_text'">
                <!--
                <SelectionQuestion :question_multiple="item"/>
                -->
                <div class="card-box mt-4">
                    <h3>{{item.question_text}}</h3>

                    <p>Seleccione una alternativa</p>
                    <v-radio-group v-model="answer_form[index].answer_text">
                        <div class="d-flex" v-for="(n,index) in item.choices_relations" :key="index">
                            <v-radio
                            class="field_radio_button"
                            :key="index"
                            :label="`${n.choice_text}`"
                            :value="n.choice_text"
                            ></v-radio>
                        </div>
                    </v-radio-group>
                </div>
            </div>
        </div>
          <v-btn
            class="mt-5"
            @click="final_exam_comprobation"
            dark
            color="primary"
          >
            Terminar evaluacion
          </v-btn>

        <v-dialog
        v-model="dialog"
        width="500"
        >

        <v-card>
            <v-card-title class="text-h5 grey lighten-2">
                Evaluacion Finalizada
            </v-card-title>


            <v-divider></v-divider>

            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="primary"
                text
                @click="send_answer_to_exam"
            >
                Ver resultados
            </v-btn>
            <v-spacer></v-spacer>

            </v-card-actions>
        </v-card>
        </v-dialog>


        <v-dialog
        v-model="dialog_result"
        width="500"
        persistent
        >

        <v-card>
            <v-card-title class="text-h5 grey lighten-2">
                Puntaje Obtenido:
            </v-card-title>


            <v-divider></v-divider>

            <v-card-actions>
                <div v-if="accumulate_procent >= max_porcent*0.8 ">
                    <h3 class="mt-5 acummulate-font-gren">{{accumulate_procent}} / {{max_porcent}}</h3>
                    <p>Preguntas correctas {{question_correct}}  de un total de {{question_total}} preguntas.</p>
                </div>
                <div v-if="accumulate_procent < max_porcent*0.8 ">
                    <h3 class="mt-5 acummulate-font-red">{{accumulate_procent}} / {{max_porcent}}</h3>
                    <p>Preguntas {{question_correct}} correctas de {{question_total}}</p>
                </div>
            </v-card-actions>
            <v-card-actions>
                <v-btn
                    class="mt-5"
                    @click="return_to_space"
                    dark
                    color="primary"
                >
                    Volver
                </v-btn>
            </v-card-actions>
        </v-card>
        </v-dialog>
    </div>
</template>


<script>
import { path } from "@/api/conf_api";
import SelectionQuestion from "~/components/form_card_user/SelectionQuestionUser.vue";
import LongQuestion from "~/components/form_card_user/LongQuestion.vue";
import ShortQuestion from "~/components/form_card_user/ShortQuestion.vue";

export default {
    layout: "LayoutPanel",
    data() {
        return {
            form: {},
            dialog: false,
            dialog_result: false,
            answer_form: [],


            points: 0,
            accumulate_procent: 0,
            question_total: 0,
            question_correct: 0,
            max_porcent: 4,
            porcent: 2,
        }
    },
    components: {
        SelectionQuestion,
        LongQuestion,
        ShortQuestion
    },
    // creacion de un watch para agregar la informacion en el store y en el local storage
    watch: {

    },
    methods: {
        return_to_space() {
            this.$router.push("/panel/es/Evaluations");
        },
        create_template_answer() {
            console.log(this.form.questions_relations);
            for(let i=0;i<this.form.questions_relations.length;i++) {
                if(this.form.questions_relations[i].question_type == 'short_text') {
                    let answer = { answer_text: ""};
                    this.answer_form.push(answer);
                }else if(this.form.questions_relations[i].question_type == 'long_text') {
                    let answer = { answer_text: ""};
                    this.answer_form.push(answer);
                }else {
                    let answer = { answer_text: ""};
                    this.answer_form.push(answer);
                }
            }
        },
        calculete_porcent_evaluation() {
            this.question_total = this.form.questions_relations.length;
            for(let i=0;i<this.form.questions_relations.length;i++) {
                if(this.form.questions_relations[i].question_type == 'short_text') {
                    console.log("Pregunta Corta");
                }else if(this.form.questions_relations[i].question_type == 'long_text') {
                    console.log("Pregunta larga");
                }else if(this.form.questions_relations[i].question_type == 'multiple_text'){
                    let correct = "";
                    for(let j=0;j<this.form.questions_relations[i].choices_relations.length;j++) {
                        if(this.form.questions_relations[i].choices_relations[j].is_correct){
                            correct = this.form.questions_relations[i].choices_relations[j].choice_text;
                        }
                    }
                    if(this.answer_form[i].answer_text === correct) {
                        this.question_correct++;
                        this.accumulate_procent += this.porcent;
                    }
                }
            }
        },
        async final_exam_comprobation() {
            /*
                aqui vamos a recibir la informacion del usuario y vamos a terminar
                para hacer una sumatoria y calcular el puntaje de la nota.
                de igual forma podemos usar un sistema de puntaje ene l proceso de la informacion
            */
            let token = localStorage.getItem("token");
            let answer_data = []
            for(let i=0;i<this.form.questions_relations.length;i++) {
                if(this.form.questions_relations[i].question_type == 'short_text') {
                    let answer = {
                        question: this.form.questions_relations[i].id,
                        user: this.$store.state.user_information.id,
                        answer_short_text: this.answer_form[i],
                        answer_long_text: null,
                        answer_selection_text: null
                    }
                    answer_data.push(answer);
                }else if(this.form.questions_relations[i].question_type == 'long_text') {
                   let answer = {
                        question: this.form.questions_relations[i].id,
                        user: this.$store.state.user_information.id,
                        answer_short_text: null,
                        answer_long_text: this.answer_form[i],
                        answer_selection_text: null
                    }
                    answer_data.push(answer);
                }else {
                   let answer = {
                        question: this.form.questions_relations[i].id,
                        user: this.$store.state.user_information.id,
                        answer_short_text: null,
                        answer_long_text: null,
                        answer_selection_text: this.answer_form[i]
                    }
                    answer_data.push(answer);
                }
            }
            await this.$axios.request({
                method: "post",
                headers: { Authorization: "Token " + token },
                baseURL: path + `/exam/add_many_answer/`,
                data:answer_data
                })
                .then((response) => {
                })
                .catch((err) => {
                    console.log("error encontrado: ", err);
                }); 
            this.dialog = true;

        },  
        // Esta es la funcion que va a retornar la informacion dle certamen
        async get_form_exam() {
            let token = localStorage.getItem("token");
            let id_form = this.$store.state.form.id;
            await this.$axios.request({
                method: "get",
                headers: { Authorization: "Token " + token },
                baseURL: path + `/exam/form/${id_form}`,
                })
                .then((response) => {
                    this.form = response.data;
                    console.log(this.form);
                    this.create_template_answer();
                    console.log(this.answer_form);
                })
                .catch((err) => {
                    console.log("error encontrado: ", err);
                }); 
        },
        // Esta es la funcion que va a enviar las repouestas del usuario
        send_answer_to_exam() {
            this.dialog = false;
            this.calculete_porcent_evaluation();
            this.dialog_result = true;
        },  
        is_activate_exam() {
            return true;
        }
    },
    mounted() {
        if(this.is_activate_exam()){
            // accedemos a la informacion del examen y poder contestar
            this.get_form_exam();
        }else {
            // volveos al panel de inicio
        }
    }
}
</script>


<style lang="scss" scoped>
.container-md {
  margin: 40px auto;
  width: 80%;
}

.card-box {
  width: 100%;
  padding: 20px 40px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
}

.acummulate-font-gren {
    font-size: 2.5rem;
    color: green;
}


.acummulate-font-red {
    font-size: 2.5rem;
    color: red;
}
</style>