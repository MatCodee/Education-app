<template>
    <div class="card-box mt-4">
      <p>Pregunta larga</p>

        <textarea class="textarea-element" placeholder="Ingrese la pregunta" @input="$emit('input', $event.target.value)"></textarea>
        <v-btn class="mx-2 mt-1" fab dark x-small color="primary">
          <v-icon dark> mdi-update </v-icon>
        </v-btn>
        <v-btn class="mx-2 mt-1" @click="delete_component"  fab dark x-small color="primary">
          <v-icon dark> mdi-delete </v-icon>
        </v-btn>
    </div>
</template>

<script>
export default {
    methods: {
      delete_component() {   
        this.$emit("click");
      }
    },
}
</script>

<style lang="scss" scoped>
.card-box {
  width: 100%;
  padding: 20px 40px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
}

.textarea-element {
  margin: 10px 0; 
  width: 100%;
  height: 200px;
  border: solid 1px #ccc;  
  outline: none;
  border-radius: 10px;
  padding: 15px 10px;
}

</style>