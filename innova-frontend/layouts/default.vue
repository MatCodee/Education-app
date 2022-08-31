<template>
  <v-app dark>

    <NavigationHeader />
    <v-main>
        <Nuxt />
    </v-main>

  </v-app>
</template>

<script>
import NavigationHeader from "@/components/Nav/NavigationHeader";
export default {
  data() {
    return {

    };
  },
  components: {
    NavigationHeader
  }
}
</script>

<style lang="scss" scope>

.fondo:before {
	content:'';
	position: absolute;
  top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	background-color: rgba(0,0,0,0.1);
}

.fondo {
  background: url("../static/fondo_recortado.jpg") no-repeat center center/cover;
  width: 100%;
  height: 100vh;
  position: relative;
}
</style>
