import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Trainer from '../views/Trainer.vue'
import Mypage from '../views/Mypage.vue'
import SubmitProfile from '../views/submitProfile.vue'
import Login from '../views/Login.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path : '/login',
    name : 'Login',
    component : Login
  },
  {
    path: '/trainer',
    name: 'Trainer',
    component: Trainer
  },
  {
    path : '/submitProfile',
    name : 'SubmitProfile',
    component : SubmitProfile
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
