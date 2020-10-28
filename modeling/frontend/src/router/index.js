import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Trainer from '../views/Trainer.vue'
import Mypage from '../views/Mypage.vue'
import SubmitProfile from '../views/submitProfile.vue'
import Login from '../views/Login.vue'
import store from '../store/index.js'
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
router.beforeEach((to,from,next)=>{
  const publicpage = [
    'Home',
    'Login'
  ]
  console.log(to.name)
  const authRequired = !publicpage.includes(to.name)
  const isLogined = store.getters.isLogined
  console.log(!isLogined&&authRequired,'------')
  console.log(isLogined)
  if(!isLogined && authRequired){
    next({name:'Login'})
  } else{
    console.log('여기아니냐?')
    next()
  }

})
export default router
