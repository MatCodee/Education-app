<template>
  <div class="d-flex">
    <v-menu
      ref="menu1"
      v-model="menu1"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="auto"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-text-field
          v-model="form_time.start_date"
          label="Date"
          hint="MM/DD/YYYY format"
          persistent-hint
          :rules="dateRules_start"
          prepend-icon="mdi-calendar"
          v-bind="attrs"
          v-on="on"
        ></v-text-field>
      </template>
      <v-date-picker
        v-model="form_time.start_date"
        no-title
        @input="menu1 = false"
      ></v-date-picker>
    </v-menu>

    <v-menu
      v-model="menu2"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="auto"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-text-field
          v-model="form_time.end_date"
          label="Date"
          hint="MM/DD/YYYY format"
          persistent-hint
          :rules="dateRules_end"
          prepend-icon="mdi-calendar"
          readonly
          v-bind="attrs"
          v-on="on"
        ></v-text-field>
      </template>
      <v-date-picker
        v-model="form_time.end_date"
        no-title
        @input="menu2 = false"
      ></v-date-picker>
    </v-menu>
  </div>
</template>


<script>
export default {
  data() {
    return {
      form_time: {
        start_date: "",
        end_date: "",
      },
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      menu1: false,
      menu2: false,
      dateRules_start: [
        (v) => !!v || "Name is required",
        (v) => this.rules_control_start_date || "Fecha es anterior a la actual",
      ],
      dateRules_end: [
        (v) => !!v || "Name is required",
        (v) => this.rules_control_end_date || "Fecha es anterior a la actual",
      ],
      rules_control_start_date: false,
    };
  },
  methods: {},
  watch: {
    "form_time.start_date": function (new_picker) {
      if (this.form_time.start_date >= this.date) {
        this.rules_control_start_date = true;
      } else {
        this.rules_control_start_date = false;
      }
    },
    'form_time.end_date': function (new_picker) {
      if(this.form_time.end_date > this.form_time.start_date){
        this.rules_control_end_date = true;
      }else {
        this.rules_control_end_date = false;   
      }
    },
  },
};
</script>


<style lang="scss" scoped>
</style>