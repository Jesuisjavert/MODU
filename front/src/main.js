import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import vuetify from './plugins/vuetify'
import VueCookies from 'vue-cookies'
// import VueAwesomeSwiper from 'vue-awesome-swiper'


Vue.use(VueCookies)
Vue.config.productionTip = false

 
// import style
 
// Vue.use(VueAwesomeSwiper, /* { default options with global component } */)



new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app')
