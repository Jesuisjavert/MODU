import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import vuetify from './plugins/vuetify'
import VueCookies from 'vue-cookies'
import WebRTC from 'vue-webrtc'
import UUID from 'vue-uuid'
import VideoBg from 'vue-videobg'
// import VueApexCharts from 'vue-apexcharts'

import io from 'socket.io-client';
const socket = io('https://k3c202.p.ssafy.io:3000');
Vue.prototype.$socket = socket;
import VueMoment from 'vue-moment'

Vue.use(VueMoment);
Vue.use(VueCookies)
Vue.config.productionTip = false

window.Kakao.init('abde304aa1e26779e03c975a6d6035de');

Vue.use(WebRTC)
Vue.use(UUID)
Vue.component('video-bg', VideoBg)
// Vue.component('apexchart', VueApexCharts)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app')
