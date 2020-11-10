import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/base'
import vuetify from './plugins/vuetify'
import store from './store'

Vue.config.productionTip = false
window.Kakao.init('abde304aa1e26779e03c975a6d6035de');
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
