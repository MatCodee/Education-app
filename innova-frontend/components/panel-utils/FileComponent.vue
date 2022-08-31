<template>
  <div class="box">
    <p>Agregar un documento:</p>
    <div class="box-component">
        <input type="file" @change="upload_file">
    </div>
    <div class="mt-6" v-for="(item, index) in documents" :key="index">
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

      </div>
    </div>
  </div>
</template>

<script>
import S3FileUpload from "@/components/utils/S3FileUpload.vue";

export default {
  data() {
    return {
      title: "",
      document: "",
      documents: [],
    };
  },
  component: {
    S3FileUpload,
  },

  methods: {
    upload_file() {
      this.item.document = event.target.files[0];
    },
    add_url() {
      let input_form = {
        title: "",
        document: null,
      };
      this.documents.push(input_form);
    },
    delete_url(index) {
      let index_data = this.documents.indexOf(index);
      this.documents.splice(index_data, 1);
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