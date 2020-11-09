import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userToken : sessionStorage.getItem('auth-token'),
    userType : sessionStorage.getItem('userType')
  },
  getters : {
    isLogined : (state) => !!state.userToken
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.userToken = token;
      sessionStorage.setItem("auth-token", token);
    },
    SET_TYPETOKEN(state,token){
      state.userType = token,
      sessionStorage.setItem('userType',token)
    }
  },
  actions: {
  },
  modules: {
  }
})
