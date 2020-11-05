import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import vuetify from './plugins/vuetify'
import VueCookies from 'vue-cookies'
import WebRTC from 'vue-webrtc'
import UUID from 'vue-uuid'

Vue.use(VueCookies)
Vue.config.productionTip = false

Vue.use(WebRTC)
Vue.use(UUID)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app')
