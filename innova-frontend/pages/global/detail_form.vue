<template>
    <div class="container-md">
        <h1>Formulario: </h1>
        <div v-if="form.type_form == 'Prueba' ">
            <h2>Esta es una prueba</h2>

            <div v-for="question,index in form.questions_relations" :key="index">
                
                <div v-if="question.question_type == 'short_text'">
                    <p>Pregunta corta</p>
                    <ShortQuestion
                        @click="delete_component(item)"
                        :text_title="question.answer_text"
                    />
                </div>
                
                <div v-if="question.question_type == 'long_text'">
                    <p>Pregunta larga</p>
                    <LongQuestion
                        @click="delete_component(item)"
                        :text_title="question.answer_text"
                    />
                </div>

                <div v-if="question.question_type== 'multiple_text'">
                    <p>Pregunta de seleccion</p>
                    <SelectionQuestion
                        @click="delete_component(item)"
                        :text_title="question.answer_text"
                        :choice="question.choices_relations"
                    />
                </div>
            </div>

        </div>
        <div v-if="form.type_form == 'Encuesta' ">
            <h2>Este es un formulario: </h2>
        </div>



    </div>
</template>


<script>
import { path } from "@/api/conf_api";

import ShortQuestion from "~/components/form_card_panel/ShortQuestion.vue";
import LongQuestion from "~/components/form_card_panel/LongQuestion.vue";
import SelectionQuestion from "~/components/form_card_panel/SelectionQuestion.vue";

export default {
    layout: "LayoutPanelProffesor",
    data() {
        return {
            form: {},
        }
    },
    components: {
        ShortQuestion,
        LongQuestion,
        SelectionQuestion
    },
    methods: {
        async get_detail_form() {
            let params_url = this.$store.state.form.id;
            console.log(params_url);

            let token = localStorage.getItem("token");
            await this.$axios
            .request({
                method: "get",
                headers: { Authorization: "Token " + token },
                baseURL: path + `/exam/form/${params_url}`,
            })
            .then((response) => {
                this.form = response.data;
                console.log(this.form);
            })
            .catch(function (error) {
                console.log("error encontrado: " + error);
            });
        }
    },
    mounted() {
        this.get_detail_form();
    }
} 
</script>

<style lang="scss" scoped>
.container-md {
  margin: 0 auto;
  width: 60%;
  margin-top: 150px;
}

</style>