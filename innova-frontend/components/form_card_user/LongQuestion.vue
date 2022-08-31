<template>
  <div class="card-box mt-4">
    <h3>{{question_long.question_text}}</h3>
    <v-textarea
        @input="$emit('input', $event.target.value)"
        label="Responder pregunta"
    ></v-textarea>
  </div>    
</template>

<script>
export default {
    data() {
        return  {

        }
    },
    props: ['question_long']
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