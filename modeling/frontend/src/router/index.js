import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Trainer from '../views/Trainer/Trainer.vue'
import TrainerDetail from '../views/Trainer/TrainerDetail.vue'
import Program from '../views/Program/Program.vue'
import ProgramCreate from '../views/Program/ProgramCreate.vue'
import Mypage from '../views/Mypage.vue'
import SubmitProfile from '../views/submitProfile.vue'
import Login from '../views/Login.vue'
import store from '../store/index.js'
import KakaoPayApprove from '../views/KakaoPayApprove.vue'
import ProgramDetail from '../views/Program/ProgramDetail.vue'

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
    path: '/trainer/:pk',
    name: 'TrainerDetail',
    component: TrainerDetail
  },
  {
    path : '/program',
    name : 'Program',
    component : Program
  },
  {
    path : '/program/:pk',
    name : 'ProgramDetail',
    component : ProgramDetail
  },
  {
    path : '/program/create',
    name : 'ProgramCreate',
    component : ProgramCreate
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
  {
    path: '/kakaopay/approve',
    name: 'KakaoPayApprove',
    component: KakaoPayApprove
  }
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
  const authRequired = !publicpage.includes(to.name)
  const isLogined = store.getters.isLogined
  if(!isLogined && authRequired){
    next({name:'Login'})
  } else{
    next()
  }

})
export default router
