import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import vuetify from './plugins/vuetify'
import VueCookies from 'vue-cookies'

import io from 'socket.io-client';
const socket = io('http://localhost:3000');
Vue.prototype.$socket = socket;

Vue.use(VueCookies)
Vue.config.productionTip = false

 
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app')
