import Vue from 'vue'
import Vuetify, { VRow } from 'vuetify/lib'
// import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify, {
  components: { VRow },
})
export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#ff002b',
        secondary: '#FFFFFF',
        accent: '#e5db09',
        error: '#00b050', 
        info: '#0070c0',
        success: '#eaf9ff',
        warning: '#e0d1ff',
      },
    },
  },
})


// primary : 빨강색
// secondary: 흰색
// accent: 노랑색
// Error : 초록색
// info : 파랑색
// success: 연하늘색
// warning: 연보라