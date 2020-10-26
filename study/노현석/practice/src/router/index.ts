// import { createRouter, createWebHistory } from '@ionic/vue-router';
// import { RouteRecordRaw } from 'vue-router';
// // import Home from '../views/Home.vue'

// import Tabs from '../views/Tabs.vue'
// import Home from '../views/Home.vue'
// import Calendar from '../views/Calendar.vue'
// import Chat from '../views/Chat.vue'
// import Mypage from '../views/Mypage.vue'

// const routes: Array<RouteRecordRaw> = [
//   {
//     path: '/',
//     redirect: '/home'
//   },
//   {
//     path: '/home',
//     name: 'Home',
//     component: Home
//   },
//   {
//     path: '/',
//     name: 'Tabs',
//     component: Tabs,
//     children: [
//       // {
//       //   path: '/home',
//       //   name: 'Home',
//         // component: () => import('@/views/Home.vue')
//       //   component: Home
//       // },
//       {
//         path: '',
//         redirect: 'home'
//       },
//       {
//         path: 'calendar',
//         name: 'Calendar',
//         // component: () => import('@/views/Calendar.vue')
//         component: Calendar
//       },
//       {
//         path: 'chat',
//         name: 'Chat',
//         // component: () => import('@/views/Chat.vue')
//         component: Chat
//       },
//       {
//         path: 'mypage',
//         name: 'Mypage',
//         // component: () => import('@/views/Mypage.vue')
//         component: Mypage
//       }
//     ]
//   },
// ]

// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes
// })

// export default router

import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import Tabs from '../views/Tabs.vue'
import ClientManage from '../views/ClientManage.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/tabs/tab1'
  },
  {
    path: '/tabs/',
    component: Tabs,
    children: [
      {
        path: '',
        redirect: 'tab1'
      },
      {
        path: 'tab1',
        component: () => import('@/views/Tab1.vue')
      },
      {
        path: 'tab2',
        component: () => import('@/views/Tab2.vue')
      },
      {
        path: 'tab3',
        component: () => import('@/views/Tab3.vue')
      },
      {
        path: 'tab4',
        component: () => import('@/views/Tab4.vue'),
        children: [
          {
            path: 'clientmanage',
            name: 'ClientMange',
            component: () => import('@/views/ClientManage.vue')
          }
        ]
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
