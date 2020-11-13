import Vue from 'vue'
import Router from 'vue-router'
import webCam from '@/views/sections/WebCam.vue'
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/components/core/Index.vue'),
      children: [
        {
          path: '',
          name: 'Home',
          component: () => import('@/views/home/Index.vue'),
        },
        {
          path: '/about',
          name: 'About us',
          component: () => import('@/views/aboutus/Index.vue'),
        },
        {
          path: '/contact',
          name: 'Contact',
          component: () => import('@/views/contact/Index.vue'),
        },
        {
          path: '/membership',
          name: 'Membership',
          component: () => import('@/views/membership/Index.vue'),
        },
        {
          path: '/Mypage',
          name: 'Mypage',
          component: () => import('@/views/sections/Mypage.vue'),
        },
        {
          path: '/oauth2/redirect',
          name: 'Oauth',
          component: () => import('@/views/oauth/Index.vue'),
        },
        {
          path: '/webrtc',
          name: 'webrtc',
          component: () => import('@/components/base/WebCam.vue')
        },
        {
          path: '/webcam',
          name: 'WebCam',
          component: webCam,
        },
        {
          path : 'watingroom/',
          name : 'WatnigRoom',
          component : () => import('@/views/chat/watingroom.vue')
        },
        {
          path : 'chatroom/',
          name : 'chatroom',
          component : ()=> import('@/views/chat/chat.vue')
        }
      ],
    },
  ],
})

// const routes = [
//     {
//     path: '/',
//     component: () => import('@/components/core/Index.vue'),
//     children: [
//       {
//         path: '',
//         name: 'Home',
//         component: () => import('@/views/home/Index.vue'),
//       },
//       {
//         path: '/about',
//         name: 'About us',
//         component: () => import('@/views/aboutus/Index.vue'),
//       },
//       {
//         path: '/contact',
//         name: 'Contact',
//         component: () => import('@/views/contact/Index.vue'),
//       },
//       {
//         path: '/membership',
//         name: 'Membership',
//         component: () => import('@/views/membership/Index.vue'),
//       },
//       {
//         path: '/Mypage',
//         name: 'Mypage',
//         component: () => import('@/views/mypage/Index.vue'),
//       },
//       {
//         path: '/oauth2/redirect',
//         name: 'Oauth',
//         component: () => import('@/views/oauth/Index.vue'),
//       },
//       {
//         path: '/webrtc',
//         name: 'webrtc',
//         component: () => import('@/components/base/WebCam.vue')
//       },
//       {
//         path: '/webcam',
//         name: 'WebCam',
//         component: webCam,
//       },
//     ],
//   },
// ]

// const router = new Router({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes
// })

// router.beforeEach((to,from,next)=>{
//   const publicpage = [
//     'Home',
//     'Login'
//   ]
//   const authRequired = !publicpage.includes(to.name)
//   const isLogined = store.getters.isLogined
//   if(!isLogined && authRequired){
//     next({name:'Login'})
//   } else{
//     next()
//   }
// })