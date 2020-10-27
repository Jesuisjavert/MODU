import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import Intro from '../views/Intro.vue'
import Tabs1 from '../views/Tabs1.vue'
import Tabs2 from '../views/Tabs2.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: Intro,
    // redirect: '/Intro'
  },
  {
    path: '/tabs/',
    component: Tabs1,
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
        component: () => import('@/views/Tab4.vue')
      }
    ]
  },
  {
    path: '/tabs/',
    component: Tabs2,
    children: [
      {
        path: '',
        redirect: 'tab5'
      },
      {
        path: 'tab5',
        component: () => import('@/views/Tab5.vue')
      },
      {
        path: 'tab6',
        component: () => import('@/views/Tab6.vue')
      },
      {
        path: 'tab7',
        component: () => import('@/views/Tab7.vue')
      },
      {
        path: 'tab8',
        component: () => import('@/views/Tab8.vue')
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
