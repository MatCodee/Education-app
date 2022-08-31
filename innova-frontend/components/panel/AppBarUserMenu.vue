<template>
  <v-menu
    offset-y
    left
    nudge-bottom="14"
    min-width="230"
    content-class="user-profile-menu-content"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-badge
        bottom
        color="success"
        overlap
        offset-x="12"
        offset-y="12"
        class="ms-4"
        dot
      >
        <v-avatar
          size="40px"
          v-bind="attrs"
          v-on="on"
        >
        <!--
          <v-img :src="require('@/assets/images/avatars/1.png')"></v-img>
          -->
        </v-avatar>
      </v-badge>
    </template>
    <v-list>
      <div class="pb-3 pt-2">
        <!--
        <v-badge
          bottom
          color="success"
          overlap
          offset-x="12"
          offset-y="12"
          class="ms-4"
          dot
        >
        
          <v-avatar size="40px">
            <v-img :src="require('@/assets/images/avatars/1.png')"></v-img>
          </v-avatar>
        </v-badge>
        -->
        <div
          class="d-inline-flex flex-column justify-center ms-3"
          style="vertical-align:middle"
        >
          <span class="text--primary font-weight-semibold mb-n1">
            Matias Altamirano
          </span>
          <small class="text--disabled text-capitalize"> Profesor </small>
        </div>
      </div>

      <v-divider></v-divider>

      <!-- Profile -->
      <v-list-item link>
        <v-list-item-icon class="me-2">
            <i class="mdi mdi-account icon-size"></i>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Perfil </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- Chat -->
      <v-list-item link>
        <v-list-item-icon class="me-2">
            <i class="mdi mdi-chat icon-size"></i>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Chat</v-list-item-title>
        </v-list-item-content>

        <v-list-item-action>
          <v-badge
            inline
            color="error"
            content="2"
          >
          </v-badge>
        </v-list-item-action>
      </v-list-item>

      <v-divider class="my-2"></v-divider>
        <v-list-item link>
        <v-list-item-icon class="me-2">
            <i class="mdi mdi-account icon-size"></i>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Instructor </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- Settings -->
      <v-list-item link>
        <v-list-item-icon class="me-2">
            <i class="mdi mdi-cog icon-size"></i>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Configuracion </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link>
        <v-list-item-icon class="me-2">
            <i class="mdi mdi-account icon-size"></i>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Cerrar Sesion </v-list-item-title>
        </v-list-item-content>
      </v-list-item>


    </v-list>
  </v-menu>
</template>

<script>


export default {
  setup() {
    return {

    }
  },
  methods: {}
}
</script>

<style lang="scss">
.user-profile-menu-content {
  .v-list-item {
    min-height: 2.5rem !important;
  }
}

.icon-size {
    color: rgb(141, 141, 141);
    font-size: 24px;
}
</style>

