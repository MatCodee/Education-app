<template>
<v-app dark>
  <div class="container-element">
    <nuxt/>
  </div>
 </v-app>
</template>

<script>
export default {
  head() {
    return {
      
    };
  },
  components: {
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
.container-element {
  width: 100%;
  max-width: 1800px;
  margin: 0 auto;
  box-sizing: border-box;
  overflow: hidden;
}
</style>