import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userToken : sessionStorage.getItem('auth-token'),
    userType : sessionStorage.getItem('userType'),
    tid : sessionStorage.getItem('tid'),
    pg_token : sessionStorage.getItem('pg_token'),
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
    },
    SET_TID(state,token){
      state.tid = token,
      sessionStorage.setItem('tid',token)
    },
    SET_PGTOKEN(state,token){
      state.pg_token = token,
      sessionStorage.setItem('pg_token',token)
    },
  },
  actions: {
  },
  modules: {
  }
})
