<template>
  <div class="card-box mt-4">
    <v-text-field label="Ingrese la Pregunta"></v-text-field>
    <div class="d-flex">
      <v-text-field class="field_option" v-on:keyup.enter="add_option"  v-model="$store.state.form_question[index].question_text" label="Opcion"/>
      <v-btn class="mx-2 mt-1" @click="add_option" fab dark x-small color="primary">
        <v-icon dark> mdi-plus </v-icon>
      </v-btn>
    </div>
  
    <div v-if="$store.state.form_question[index].choices_relations">
      <v-radio-group v-on:change="group_selection">
          <div class="d-flex" v-for="(n,index) in $store.state.form_question[index].choices_relations" :key="index">
            <v-radio
              class="field_radio_button"
              :key="index"
              :label="`${n.choice_text}`"
              :value="n.choice_text"
            ></v-radio>
          <v-btn icon @click="delete_option">
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
</template>

<script>
export default {
  data() {
    return {
      group_selection: 0,
      options: [],

      input_text_option: "",
    };
  },
  computed: {
  },
  methods: {
    add_option() {
      if(this.input_text_option) {
        this.$store.commit('asign_question_index_choice',input_text_option,this.index);
        this.input_text_option = "";
        this.options.push(form);
      }
    },
    delete_option(option) {
      let option_index = option.text_title_option;
      console.log(option_index);
      let index = this.options.findIndex(op => op.text_title_option === option_index)
      this.options.splice(index);
    },
    delete_component() {   
      this.$emit("click");
    }
  },
  props: ["index"],
};
</script>

<style lang="scss" scoped>
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