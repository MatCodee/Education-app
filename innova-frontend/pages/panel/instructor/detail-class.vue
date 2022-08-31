<template>
  <div class="container-md">
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
                Crear una Clase
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-row>
      <v-col md="4">
        <h2 class="mb-12">Editar el curso y sus clases</h2>
        <v-list subheader two-line>
          <v-list-item
            v-for="class_data in class_total"
            :key="class_data.id"
          >
            <v-list-item-content>
              <v-list-item-title v-text="class_data.title"></v-list-item-title>

              <v-list-item-subtitle
                v-text="class_data.resumen"
              ></v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-btn
                fab
                dark
                @click="edit_class(class_data)"
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
                @click="dialog_delete(class_data)"
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
        <h2 class="mb-2">Detalla de la Clase</h2>

        <div v-if="request_class">
          <p>Titulo</p>
          <v-text-field
            label="Titulo"
            v-model="request_class.title"
            solo
          ></v-text-field>

          <p>Resumen</p>
          <v-textarea
            solo
            v-model="request_class.resumen"
            name="input-7-4"
            label="Solo textarea"
            class="mt-10"
          ></v-textarea>

          <v-card class="mb-16 mt-16 pa-16">
            <div class="mb-16">
              <div class="desing-video" v-if="request_class">
                <p>Video Actual de la clase</p>
                <video width="100%" controls :src="request_class.video"></video>
              </div>
            </div>

            <div style="min-height: 4px">
              <v-progress-linear
                v-model="value"
                :active="show"
                :indeterminate="query"
                :query="true"
              ></v-progress-linear>
            </div>
            <input type="file" @change="videoFile" class="mt-5 mb-13" multiple />
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
            <input type="file" @change="documentFile"  class="mt-5 mb-13" multiple />
          </v-card>
        </div>
        <p>Link del video</p>
          <v-text-field
            label="Titulo"
            v-model="request_class.link"
            solo
          ></v-text-field>
        <v-btn color="primary" @click="updateProffesorClass" dark>
          Actualizar la informacion de la clase
        </v-btn>
      </v-col>
    </v-row>


    <!--Este es el dialog para crear una nueva clase  -->
    <v-dialog v-model="dialog" width="70%">
      <v-card class="pa-16">

            <h2 class="mb-2">Creacion de una Clase</h2>
            <p>Titulo</p>
            <v-text-field
              label="Titulo"
              v-model="form_class.title"
              solo
            ></v-text-field>
            <p>Resumen de la Clase (opcional)</p>
            <v-textarea
              solo
              v-model="form_class.resumen"
              name="input-7-4"
              label="Solo textarea"
              class="mt-10"
            ></v-textarea>


            <div style="min-height: 4px">
              <v-progress-linear
                v-model="value"
                :active="show"
                :indeterminate="query"
                :query="true"
              ></v-progress-linear>
            </div>

    
              <div class="desing-video">
                <p>Video Actual de la clase</p>
                <video width="100%" controls :src="form_class.video"></video>
              </div>
            <S3FileUpload :dirName="'media_cdn/' + $store.state.week_path"/>
            <v-text-field
              class="mt-2"
              label="path del video"
              v-model="form_class.video"
              solo
            ></v-text-field>
      

            <div class="mb-16">
              <p>Agregar enlaces (opcional)</p>
              <UrlComponent/>
            </div>


            <p>Agregar Documentos: </p>
            <input type="file" ref="file" multiple class="mt-5 mb-13">



              <p>Link del video de clase (opcional)</p>
              <v-text-field
                label="Titulo"
                v-model="form_class.link"
                solo
              ></v-text-field>
            <v-btn block color="primary" @click="create_class" dark>
              Crear la Clase
            </v-btn>

      </v-card>
    </v-dialog>

    <v-dialog v-model="delete_bol" max-width="400">
      <v-card class="mx-auto pa-12">
        <v-card-subtitle class=""> Eliminar la clase </v-card-subtitle>

        <v-card-text class="text--primary">
          <div>Estas seguro que quieres elminar la clase?</div>
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" text @click="delete_class"> Eliminar </v-btn>

          <v-btn color="primary" text @click="delete_bol = !delete_bol">
            Cancelar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
import { path } from "@/api/conf_api";
// componentes:
import S3FileUpload from "@/components/utils/S3FileUpload.vue";
import UrlComponent from "@/components/panel-utils/UrlComponent.vue";
import UploadFileMultiple from "@/components/utils/UploadFileMultiple.vue";

export default {
  layout: "LayoutPanelProffesor",
  data() {
    return {
      show: true,
      value: 0,
      delete_bol: false,
      dialog: false,
      query: false,

      class_total: [],
      request_class: {},
      form_class: {
        id: "",
        title: "",
        resumen: "",
        week: "",
        video: null,
        document: null,
      },
    };
  },
  watch: {
    '$store.state.file_class_upload': function() {
        this.form_class['video'] = this.$store.state.file_class_upload;
        console.log("cambio!!!!")
    }
  },
  components: {
    S3FileUpload,
    UrlComponent,
    UploadFileMultiple,
  },
  methods: {
    documentFile(event) {
      console.log(event.target.files[0]);
      this.form_class.document = event.target.files[0];
    },
    videoFile(event) {
      console.log(event.target.files[0]);
      this.form_class.video = event.target.files[0];
    },
    async get_Class() {
      let week = this.$store.state.current_id_week;
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/detail-class/${week}`,
        })
        .then((result) => {
          this.class_total = result.data;
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    async create_class() {
      let df = new FormData();
      console.log(this.form_class.video);
      console.log(this.form_class.document);
      //df.append("url_documents",null);
      //df.append("documents",null);

      /*
      let documents = []
      for( var i = 0; i < this.$refs.file.files.length; i++ ){
          let file = this.$refs.file.files[i];
          let form = { document: file };
          documents.push(form);
      }
      console.log(documents);
      if(documents.length > 0) {
        df.append("documents",documents);
      }
      */


      df.append("title", this.form_class.title);
      df.append("resumen", this.form_class.resumen);
      df.append("week", this.$store.state.current_id_week);
    
    
      if(this.form_class.link) {
        df.append("link",this.form_class.link)
      }
    

      if (this.form_class.video && !this.form_class.document) {
        df.append("video", this.form_class.video);
      } else if (this.form_class.document && !this.form_class.video) {
        df.append("document", this.form_class.document);
      } else {
        df.append("video", this.form_class.video);
        df.append("document", this.form_class.document);
      }

      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "post",
          headers: { 
            'Content-Type': 'multipart/form-data',
            Authorization: "Token " + token, 
          },
          baseURL: path + `/courses/create-class/`,
          data: df,
        })
        .then((result) => {
          console.log(result.data);
          this.dialog = !this.dialog;
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },

    // funciones de actualizacion de clase de profesor
    async updateProffesorClass() {
      let pk = this.request_class.id;
      // comprobacion de los campos directamente en la funcion

      let df = new FormData();
      if (this.request_class.video == null && this.request_class.document == null) {
        df.append("title", this.request_class.title);
        df.append("resumen", this.request_class.resumen);
        df.append("week", this.$store.state.current_id_week);
      } else if (this.request_class.video == null) {
        df.append("title", this.request_class.title);
        df.append("resumen", this.request_class.resumen);
        df.append("week", this.$store.state.current_id_week);
        df.append("document", this.request_class.document);
      } else if (this.request_class.document == null) {
        df.append("title", this.request_class.title);
        df.append("resumen", this.request_class.resumen);
        df.append("week", this.$store.state.current_id_week);
        df.append("video", this.request_class.video);
      } else {
        df.append("video", this.request_class.video);
        df.append("document", this.request_class.document);
      }
      if(this.request_class.link) {
        df.append('link',this.request_class.link);
      }
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "put",
          headers: { Authorization: "Token " + token },
          baseURL: path + `/courses/update_class/${pk}`,
          data: df,
        })
        .then((result) => {
          console.log("Actualizando la clase");
          console.log(result.data)
        })
        .catch((err) => {
          console.log("error encontrado: ", err);
        });
    },
    async delete_class(class_data) {
      if (class_data) {
        let pk = this.request_class.id;
        let token = localStorage.getItem("token");
        await this.$axios
          .request({
            method: "delete",
            headers: { Authorization: "Token " + token },
            baseURL: path + `/courses/delete-class/${pk}`,
          })
          .then((result) => {
            this.delete_bol = !this.delete_bol;
            //this.getCourseProffesor();
          })
          .catch((err) => {
            console.log("error encontrado: ", err);
          });
      }
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
  },
  mounted() {
    this.get_Class();
  }
};
</script>

<style lang="scss">

.container-md {
  margin:  0 auto;
  width: 80%;
  margin-top: 100px;
}


</style>