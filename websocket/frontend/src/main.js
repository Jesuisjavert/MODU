import Vue from 'vue'
import App from './App.vue'
import io from 'socket.io-client';
import router from './router'
const socket = io('http://localhost:3000');
Vue.prototype.$socket = socket;

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
