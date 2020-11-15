import Vue from 'vue'
import Vuex from 'vuex'
import pathify from 'vuex-pathify'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userToken : sessionStorage.getItem('auth-token'),
    userType : sessionStorage.getItem('userType'),
    username : sessionStorage.getItem('username'),
    tid : sessionStorage.getItem('tid'),
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
    REMOVE_TID(){
      sessionStorage.removeItem('tid')
    },
    LOGOUT(state){
      sessionStorage.removeItem('auth-token')
      sessionStorage.removeItem('userType')
      state.userToken = ''
      state.userType = ''
    },
    SET_USERNAME(state,token){
      state.username = token
      sessionStorage.setItem('username',token)

    }
  },
  
  actions : {
    
  },
  
  plugins: [pathify.plugin],
})
