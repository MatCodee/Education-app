<template>
  <div class="container-md">
    <h2 class="mb-3">Evaluaciones del curso:</h2>
    <v-simple-table class="table-course my-10">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Evaluaciones</th>
            <th class="text-left">Porcentaje</th>
            <th class="text-left">Note</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in notas" :key="index">
            <td>{{ item.get_title_evaluation }}</td>
            <td>{{ item.get_porcent + "%" }}</td>
            <td>{{ item.nota }}</td>
          </tr>
        </tbody>
        <tfoot v-if="$store.state.current_course.end_course">
          <tr>
            <td> Promedio </td>
            <td>Total </td>
            <td>{{ prom }}</td>
          </tr>
        </tfoot>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import { path } from "@/api/conf_api";

export default {
  layout: "LayoutPanel",
  data() {
    return {
      notas: [],
      prom: null,
    };
  },
  computed: {},
  methods: {
    calc_prom() {
      let prom = 0;
      for (let i = 0; i < this.notas.length; i++) {
        prom += this.notas[i].porcentaje * this.notas[i].nota;
      }
      this.prom = parseFloat(prom/100).toFixed(1);
    },
    async get_calification_user() {
      let token = localStorage.getItem("token");
      let slug = this.$store.state.current_course.slug;
      let user = this.$store.state.user_information;
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL:
            path + `/courses/get_calification_user/${slug}/${user.username}`,
        })
        .then((response) => {
          this.notas = response.data;
          console.log(response.data);
          if(this.$store.state.current_course.end_course) {
             this.calc_prom();
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.get_calification_user();
  },
};
</script>


<style lang="scss">
.container-md {
  width: 80%;
  margin: 60px auto;
}

.table-course {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px !important;
}
</style>