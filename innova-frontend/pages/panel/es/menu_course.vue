<template>
  <div class="container-md">
    <v-row>
      <v-col md="3">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 mb-1">
                Aprendizaje
              </v-list-item-title>
              <v-list-item-subtitle
                > Clases y recursos</v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
            >
            <v-img src="https://cdn-icons-png.flaticon.com/128/3845/3845824.png"/>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn outlined rounded text to="/panel/es/detail"> Acceder </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col md="3">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 mb-1">
                Notas
              </v-list-item-title>
              <v-list-item-subtitle
                >Calificaciones del curso</v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
            >
            <v-img src="https://cdn-icons-png.flaticon.com/128/3845/3845869.png"/>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn outlined rounded text to="/panel/es/Exam"> Acceder</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col md="3">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 mb-1">
                Foro del curso
              </v-list-item-title>
              <v-list-item-subtitle
                >Las preguntas mas comunes estan aqui</v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
              
            >
            <v-img src="https://cdn-icons-png.flaticon.com/128/3845/3845696.png"/></v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn outlined rounded text to="/panel/es/Foro"> Acceder </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

    <v-col md="3">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 mb-1">
                Evaluaciones
              </v-list-item-title>
              <v-list-item-subtitle
                >Evaluaciones del curso </v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
            >
            <v-img src="https://cdn-icons-png.flaticon.com/512/3845/3845853.png"/>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn outlined rounded text to="/panel/es/Evaluations"> Acceder</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

    <v-col md="3">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 mb-1">
                Encuestas
              </v-list-item-title>
              <v-list-item-subtitle
                >Encuestas del curso</v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
            >
            <v-img src="https://cdn-icons-png.flaticon.com/512/3845/3845866.png"/>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn outlined rounded text to="/panel/es/utils"> Acceder</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  layout: "LayoutPanel",
};
</script>


<style lang="scss">
.container-md {
    margin: 0 auto;
    width: 80%;
    margin-top: 50px;
}
</style>