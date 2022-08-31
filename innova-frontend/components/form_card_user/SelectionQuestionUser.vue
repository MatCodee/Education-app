<template>
  <div class="card-box mt-4">
    <h3>{{question_multiple.question_text}}</h3>

      <p>Seleccione una alternativa</p>
      <v-radio-group v-model="radioGroup">
          <div class="d-flex" v-for="(n,index) in question_multiple.choices_relations" :key="index">
            <v-radio
              class="field_radio_button"
              :key="index"
              :label="`${n.choice_text}`"
              :value="n.choice_text"
            ></v-radio>
          </div>
      </v-radio-group>
  </div>
</template>



<script>
export default {
    data() {
        return {
          radioGroup: 0,
        }
    },
    props: ['question_multiple']
}
</script>

<style lang="scss" scoped>
.card-box {
  width: 100%;
  padding: 20px 40px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
}
</style>