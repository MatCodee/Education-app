<template>
  <div class="box">
    <p>Titulo del enlace:</p>
    <v-text-field   
      label="titulo del enlace"
      v-model="title"
      placeholder="titulo del enlace"
      solo
    ></v-text-field>
    <p>Url del formulario:</p>
    <v-text-field
      label="Url del documento"
      v-model="url_document"
      placeholder="Url del documento"
      solo
    ></v-text-field>
    <v-btn class="mx-2 mt-1" @click="add_url" fab dark x-small color="primary">
      <v-icon dark> mdi-plus </v-icon>
    </v-btn>

    <div class="mt-6" v-for="(item, index) in url_documents" :key="index">
      <div class="box d-flex align-center">
        <div class="box-component mr-3">
            <p>Titulo del enlace:</p>
            <v-text-field
            label="vacio"
            v-model="item.title"
            placeholder="vacio"
            solo
            ></v-text-field>
        </div>
        <div class="box-component">
            <p>Url del formulario:</p>
            <v-text-field
            label="vacio"
            v-model="item.url_document"
            placeholder="vacio"
            solo
            ></v-text-field>
        </div>

        <v-btn
          class="mx-2 mt-1"
          @click="delete_url(item)"
          fab
          dark
          x-small
          color="primary"
        >
          <v-icon dark> mdi-delete </v-icon>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

    title: "",
    url_document: "",
    url_documents: [],
    
    };
  },
  methods: {
    add_url() {
        if(this.title || this.url_document) {
            let input_form = {
                title: this.title,
                url_document: this.url_document
            }
            this.url_documents.push(input_form);
            this.title = "";
            this.url_document = "";
        }
    },
    delete_url(index) {
        let index_data = this.url_documents.indexOf(index);
        this.url_documents.splice(index_data,1);
    },
  },
};
</script>


<style lang="scss" scoped>
.box {
  width: 100%;
  padding: 40px 40px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
}

.box-component {
    width: 100%;
}
</style>