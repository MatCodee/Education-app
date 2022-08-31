<template>
  <v-app>
    <v-app-bar color="white"  app flat>  
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <div class="btn-desktop-display">
        <button class="layout-btn button-font button-m btn-w" @click="go_back_menu" dark >Volver al menu Principal</button>
      </div>
      <div class="btn-mobile-display">
        <v-btn icon color="primary" dark  @click="go_back_menu">
          <v-icon>mdi-logout</v-icon>
        </v-btn>
      </div>
    </v-app-bar>



    <v-navigation-drawer app temporary  v-model="drawer">
      <v-list>

          <v-list-item class="px-4">
            <!--
            <v-list-item-avatar>
              <v-img :src="require('@/assets/images/avatars/1.png')"></v-img>
            </v-list-item-avatar>
            -->
          </v-list-item>

      </v-list>



      <v-list>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            :to="item.path"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-app dark>
            <nuxt/>
        
    </v-app>

  </v-app>
</template>

<script>
import {path} from "@/api/conf_api";
export default {
  data() {
    return {
      checkbox: true,
      notDrawer: true,
      
      course: [],
      ite: 0,
      settings: [],
      course_select: null,

      proffesor_info: [],

      interval: {},
      value: 0,

      drawer: false,
      notDrawer: false,
      group: null,
      items: [
        { title: "Cursos", icon: "mdi-view-dashboard", path: "/panel/instructor/coursesp" },
        {
          title: "Administracion de Usuarios",
          icon: "mdi mdi-application-edit-outline",
          path: "/panel/instructor/comunicationp",
        },
        {
          title: "Lista de tareas",
          icon: "mdi-format-list-checkbox",
          path: "/panel/instructor/list-homework",
        },
        {
          title: "Foro de cursos",
          icon: "mdi-forum",
          path: "/panel/instructor/foro_detail",
        },
        {
          title: "Crear Evaluaciones",
          icon: "mdi-file",
          path: "/panel/instructor/create_exam",
        },
        {
          title: "Configuracion del Profesor",
          icon: "mdi-account-cog",
          path: "/panel/instructor/confp",
        },
      ],
    };
  },
  components: {
  },
  methods: {
  go_back_menu() {
      this.$router.push('/panel/mycourses'); 
  },

   async getProffesorInfo() {
      let token = localStorage.getItem("token");
      await this.$axios
          .request({
            method: "get",
            headers: { Authorization: `Token ${token}` },
            baseURL: path + `/account/infoProffesor/`,
          })
        .then((response) => {
          this.proffesor_info = response.data;
          //console.log(this.proffesor_info);

          // debemos almacenar la informacion en el local Storage
          localStorage.setItem("id_proffesor", this.proffesor_info.id);
          //localStorage.setItem("email", this.user_info.email);

        })
        .catch((error) => {
          console.log(error);
        });
    },    
  },
  mounted() {
    this.getProffesorInfo();
  },
};
</script>

<style lang="scss" scoped>

//btn
.container-element-btn {
  width: 100%;
}


.detail-img-desing {
  height: 200px;
  object-fit: cover;
  object-position: center;
}

.button-m:hover {
    background-color: #0f52b5;
}

.btn-w {
    max-width: 250px;
}

.btn-w100 {
  width: 100%;
}

.button-m {
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    background-color: #0D47A1;
    transition: background-color .35s ease-in-out,color .15s ease-in-out,border .15s ease-in-out;
    height: 48px;
    padding-left: 40px;
    padding-right: 40px;
    border-radius: 5px;
    color: #ffff;
}

.button-font {
  text-decoration: none;
  font-family: Gilroy,SF Pro Display,-apple-system,BlinkMacSystemFont,Roboto,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;
  font-weight: 700;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: .4px;
}

.btn-mobile-display {
  display: none;
}

@media screen and (max-width: 600px) {
  .btn-desktop-display {
    display: none;
  }
  .btn-mobile-display {
    display: block;
  }
}
</style>