# Build a PWA With Vue & Ionic 4 (youtube)



## Vue + Ionic

### vue 설치

```bash
$ vue-cli install
npm i -g @vue/cli-init

$ project create
vue init webpack my-project

$ project start
cd my-project
npm run dev

# 현재 진행중 방법
$ project create
vue create zip-info-pwa
cd zip-info-pwa

$ vue-router install
vue add router
```



### ionic4 설치

```bash
$ ionic4 install
npm i @ionic/vue

$ if error
npm i @ionic/vue@0.0.4
```



#### main.js

> main.js에 라이브러리를 import 해서 사용

```javascript
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Ionic from '@ionic/vue'
import '@ionic/core/css/ionic.bundle.css'

Vue.use(Ionic)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```














#### 참고링크

- ionic + vue
  - https://ui.toast.com/weekly-pick/ko_20181206/
- 