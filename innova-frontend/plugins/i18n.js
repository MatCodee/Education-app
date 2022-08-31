import Vue from 'vue'
import VueI18n from 'vue-i18n'
import es from 'vuetify/lib/locale/es'

Vue.use(VueI18n)

export default ({ app, $vuetify }) => {
  // inject vue-i18n in the app context
  app.i18n = new VueI18n({
    locale: 'es',
    messages: {
      'es': es,
    },
  })
  
  // change the default method used by Vuetify to apply translation to their built-in components
  $vuetify.lang.t = (key, ...params) => app.i18n.t(key, params)
}