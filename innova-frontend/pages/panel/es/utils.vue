<template>
  <div class="container-md">
    <h3>Encuestas:</h3>
    <div class="my-5" v-for="e,index in polls" :key="index">
      <v-card class="max-auto pa-10 layout-card">
        <h3>{{e.title}}</h3>
        <p>{{e.description}}</p>
        <a :href="e.link" target="_blank">{{e.link}}</a>
      </v-card>
    </div>

  </div>
</template>

<script>
import { path } from "@/api/conf_api";
export default {
  layout: "LayoutPanel",
  data() {
    return {
        polls: [],
    }
  },
  methods: {
    async get_evaluation() {
      let token = localStorage.getItem("token");
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/get_polls`,
        })
        .then((response) => {
          this.polls = response.data;
          console.log(this.polls)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.get_evaluation();
  },
}
</script>

<style lang="scss" scoped>
.container-md {
    margin: 40px auto;
    width: 80%;
}

.layout-card {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
}
</style>