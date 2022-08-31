<template>
  <div class="container-md" v-if="evaluations">
    <h3>Evaluaiones:</h3>
    <div class="mt-5" v-for="(e, index) in evaluations" :key="index">
      <v-card class="max-auto pa-10 layout-card">
        <h3>{{ e.title }}</h3>
        <p>{{ e.description }}</p>

        <p>Fecha de la evaluacion:</p>
        <div>
          <p> Inicio: {{ process_date_complete(e.start_date) }}</p>
          <p> Termino: {{ process_date_complete(e.end_date) }}</p>
        </div>
        <div v-if="current_time_compare(e.start_date, e.end_date)">
          <!--
          <a :href="e.link" target="_blank">{{ e.link }}</a>
          -->
          <v-btn color="primary" @click="form_detail_click(e)"> Acceder a la Evaluacion </v-btn>
        </div>
        <div v-else>
          <p>Evaluacion no disponible</p>
        </div>
      </v-card>
    </div>
  </div>
</template>


<script>
import moment from "moment";
import { path } from "@/api/conf_api";
import { date_element, relativeDate } from "@/helpers/time_function";

export default {
  layout: "LayoutPanel",
  data() {
    return {
      evaluations: [],
    };
  },
  methods: {
    date_element: date_element,
    relativeDate: relativeDate,

    async form_detail_click(form) {
      this.$store.commit('change_form',form);
      this.$router.push("/panel/es/FormDetail");
    },

    process_date_complete(current_date) {
      return new Date(current_date);
    },
    current_time_compare(start_date, end_date) {
      //let current_date = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substr(0, 10);
      moment.locale();
      let current_date = moment().format();
      console.log(current_date);
      console.log("Fecha de inicio: ", start_date);
      console.log("Fecha final: ", end_date);
      if (start_date <= current_date && current_date <= end_date) {
        console.log("Entro en la aplicacion");
        return true;
      } else {
        return false;
      }
    },
    process_date(date) {
      let mont_calc = parseInt((date.getMonth() + 1) / 10);
      let day_calc = parseInt(date.getDate() / 10);
      console.log(mont_calc);
      console.log(day_calc);
      if (mont_calc === 0) {
        mont_calc = `0${parseInt(date.getMonth() + 1)}`;
      } else {
        mont_calc = date.getMonth() + 1;
      }
      if (day_calc === 0) {
        day_calc = `0${parseInt(date.getDate())}`;
      } else {
        day_calc = date.getDate();
      }
      return date.getFullYear() + "-" + mont_calc + "-" + day_calc;
    },
    async get_evaluation() {
      let token = localStorage.getItem("token");
      let slug = this.$store.state.current_course.slug;
      await this.$axios
        .request({
          method: "get",
          headers: { Authorization: `Token ${token}` },
          baseURL: path + `/courses/get_califications/${slug}`,
        })
        .then((response) => {
          this.evaluations = response.data;
          console.log(this.evaluations);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.get_evaluation();
  },
};
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