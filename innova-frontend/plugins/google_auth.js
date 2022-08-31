import Vue from 'vue'
import GoogleAuth from '@/config/google_oAuth.js';

const gauthOption = {
  clientId: '567845169256-d5kofok2ui8elnk4rufqb4ijgamagimv.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}

Vue.use(GoogleAuth, gauthOption)
//Vue.config.productionTip = false