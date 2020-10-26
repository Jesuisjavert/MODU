import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userToken : sessionStorage.getItem('auth-Token')
  },
  getters : {
    isLogined : (state) => !!state.userToken
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token;
      sessionStorage.setItem("auth-token", token);
    }
  },
  actions: {
  },
  modules: {
  }
})
