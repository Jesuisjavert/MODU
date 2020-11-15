import Vue from 'vue'
import Vuex from 'vuex'
import pathify from 'vuex-pathify'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userToken : sessionStorage.getItem('auth-token'),
    userType : sessionStorage.getItem('userType'),
  },
  getters: {
    isLogined : (state) => !!state.userToken,
    isUserTypeCheck : (state) => !!state.userType,
    isKakaoLogined() { return state.kakaoCheck }
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.userToken = token;
      sessionStorage.setItem("auth-token", token);
    },
    SET_TYPETOKEN(state,token){
      state.userType = token,
      sessionStorage.setItem('userType',token)
    },
    LOGOUT(state){
      sessionStorage.removeItem('auth-token')
      sessionStorage.removeItem('userType')
      state.userToken = ''
      state.userType = ''
    }
  },
  
  actions : {
    
  },
  
  plugins: [pathify.plugin],
})
