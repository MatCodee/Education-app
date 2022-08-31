<template>
  <div>
    <v-navigation-drawer  app temporary  v-model="drawer">
   
    <div class="menu-header">
      <p>Menu</p>
      <v-btn icon @click="drawer = !drawer">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </div>
      <v-list>
   
          <v-list-item class="px-4">
            <v-list-item-avatar size="60" v-if="!user_info.image_user">
              <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
            </v-list-item-avatar>
        
            <v-list-item-avatar  v-if="user_info.image_user">
              <v-img  :src="user_info.image_user"></v-img>
            </v-list-item-avatar>
          </v-list-item>

        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="text-h5" v-if="user_info.fullname">
              {{ user_info.fullname }}
            </v-list-item-title>
            <v-list-item-title class="text-h5" v-if="!user_info.fullname">
              {{ user_info.username }}
            </v-list-item-title>
            <v-list-item-subtitle> {{ user_info.email }} </v-list-item-subtitle>
          </v-list-item-content>

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

        <v-list-group :value="true" no-action sub-group>
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title> Configuracion </v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon, path], i) in settings"
            :key="i"
            link
            :to="path"
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>


    <v-app-bar color="primary" class="app-bar-desing" flat >
      <v-app-bar-nav-icon @click="drawer = !drawer" color="white"></v-app-bar-nav-icon>
      <div class="logo">
          <!--
        <NLink to="/">
          <v-img
            :src="require('@/assets/images/LIXFUX.png')"
            alt="logo"
            width="120"
            class="hide-btn-response-logo"
          />
        </NLink>
        -->
      </div>

     

      <v-spacer></v-spacer>
      <v-form class="form-box mx-1" action="/panel/search" method="get">
          <v-text-field
            class="mt-6  size-text-field"
            outlined
            background-color="white"
            label="Buscar cualquier cosa"
            clearable
            type="text"
            rounded
            :full-width="true"
            dense
            color="white"
            name="query"
          >
            <template v-slot:append>
              <v-icon color="primary2"> mdi mdi-magnify </v-icon>
            </template>
          </v-text-field>
      </v-form>
      
      <v-btn  v-if="is_instructor" icon color="white" to="/panel/instructor/coursesp/" dark>
          <v-icon>mdi-school</v-icon>
      </v-btn>


      <v-badge color="error"  icon="mdi-chat" bottom offset-x="20" offset-y="25">
        <v-btn icon color="white">
          <v-icon>mdi-bell</v-icon>
        </v-btn>
      </v-badge>


      <!--
      <app-bar-user-menu></app-bar-user-menu>
      -->

      <v-spacer></v-spacer>

      <v-btn icon color="white" dark v-on:click="closeSession()">
          <v-icon>mdi-logout</v-icon>
      </v-btn>
      
    </v-app-bar>
    
  </div>
</template>

<script>
import {path} from "@/api/conf_api";
export default {
  name: "AppBarPanel",
  data() {
    return {
      user_info: [],
      drawer: false,
      is_instructor : false,
      op_select_user: -1,

      group: null,
      items: [
        {
          title: "Centro de Actividades",
          icon: "mdi-view-dashboard",
          path: "/panel/activity",
        },
        {
          title: "Cursos Registrados",
          icon: "mdi mdi-application-edit-outline",
          path: "/panel/mycourses",
        },
      ],
      settings: [
        ["Usuario", "mdi-account-multiple-outline", "/panel/settings"],
      ],
    };
  },

  methods: {

    closeSession() {
      console.log("Eliminando todos los campos");
      // Eliminacion de los campos
      this.$axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("isAuthenticate");
      localStorage.removeItem("username");
      localStorage.removeItem("email");
      localStorage.removeItem("fullname");
      localStorage.removeItem("is_instructor");
      localStorage.removeItem("user_id");

      this.$router.push("/");
    },
/*
    async getAccestokentoBackend() {
      let formData = {
        grant_type: 'convert_token',
        client_id: "567845169256-sm737t22ggqc53330surtsm106varirs.apps.googleusercontent.com",
        client_secret: "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",
        backend: 'google-oauth2',
        token: this.$store.state.loginUser.google.auth.access_token,
      }
      await axios.request({
        baseURL: "http://127.0.0.1:8000/auth/convert-token",
        method: 'post',
        data: qs.stringify(formData),
        headers: {
          'content-type': 'application/x-www-form-urlencoded',
        }
      })
      .then(res => {
        //const token = result.data.auth_token;
        //this.$axios.defaults.headers.common["Authorization"] = "Token " + token;
        //localStorage.setItem("token", token);
        //localStorage.setItem("isAuthenticate", true);
        console.log(res.data);
      })
      .catch(err => {
        console.log(err);
      });
    },
*/
    async getUserInfo() {
      let token = localStorage.getItem("token");
      await this.$axios
          .request({
            method: "get",
            headers: { Authorization: `Token ${token}` },
            baseURL: path + `/account/infoUser/`,
          })
        .then((response) => {
            this.user_info = response.data;
            //this.$axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token");
            this.is_instructor = response.data['is_instructor'];
            console.log(this.user_info);

            if(this.op_select_user == 1){
            
              // debemos almacenar la informacion en el local Storage
              localStorage.setItem("fullname", this.user_info.fullname);
              localStorage.setItem("email", this.user_info.email);
              localStorage.setItem("username", this.user_info.username);
              localStorage.setItem("is_instructor",this.user_info.is_instructor);
              localStorage.setItem("user_id",this.user_info.id);
              this.$store.commit('set_user_information',this.user_info)
            }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    existUser() {
      let token = localStorage.getItem("token");
        this.$axios
          .request({
            method: "get",
            headers: { Authorization: `Token ${token}`},
            baseURL: path + `/account/exist_user/`,
          })
        .then((response) => {
            console.log("Existe el usuario de la cuenta: " + response.data.data);
            this.op_select_user = parseInt(response.data.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  components: {
    /*
    AppBarUserMenu: () => import("@/components/ComponentsPanel/AppBarUserMenu"),
    */
  },
  watch: {
    group() {
      this.drawer = false;
    },
  },
  mounted() {
    //this.getAccestokentoBackend();
    //this.is_instructor = localStorage.getItem('is_instructor');
    this.existUser();
    this.getUserInfo();
  },
};
</script>


<style lang="scss">



.edit-link {
  text-decoration: none;
}

@media (max-width: 1068px) {
  .hide-btn-response {
    display: none;
  }
}

.form-box {
  max-width: 700px;
  width: 100%;
}

@media (min-width: 1256px) {
  .hide-btn-response-drawer {
    display: none;
  }
  .form-box {
    width: 100%;
  }
}
@media (max-width: 868px) {
  .hide-btn-response-logo {
    display: none;
  }
  .form-edit {
  width: 100%;
  }
}


.image-edit {
  padding: 10px 10px;
}

.app-bar-desing {
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
}

.menu-header {
  padding: 10px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  p {
    padding-left: 10px;
    margin-top: 10px;
    font-size: 16px;
    font-weight: 700;
    font-weight: 20px;
  }
}

</style>