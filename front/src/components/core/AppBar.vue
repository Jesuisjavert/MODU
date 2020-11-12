<template>
  <div>
    <v-app-bar
      id="home-app-bar"
      app
      color="white"
      elevation="1"
      height="80"
    >
      <base-img
        :src="require('@/assets/modu.png')"
        contain
        max-width="60"
        width="100%"
        @click="gohome"
        style="cursor: pointer"
      />

      <v-spacer />

      <div>
        <v-tabs
          class="hidden-sm-and-down"
          optional
        >
          <v-tab
            v-for="(name, i) in items"
            :key="i"
            :to="{ name }"
            :exact="name === 'Home'"
            :ripple="false"
            active-class="text--primary"
            class="font-weight-bold"
            min-width="96"
            text
          >
            {{ name }}
          </v-tab>
        </v-tabs>
      </div>

      <v-app-bar-nav-icon
        class="hidden-md-and-up"
        @click="drawer = !drawer"
      />
    </v-app-bar>

    <drawer
      v-model="drawer"
      :items="items"
    />
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
  export default {
    name: 'CoreAppBar',

    components: {
      Drawer: () => import('./Drawer'),
    },

    data: () => ({
      drawer: null,
      ansitems: [
        'Home',
        'About us',
        'Contact',
        'Membership',
      ],
      loginitems : [
        'Home',
        'About us',
        'Contact',
        'Mypage',
        // 'Logout'
      ]
    }),
    methods: {
      gohome() {
        this.$router.push('/')
      }
    },
    computed : {
      ...mapGetters(['isUserTypeCheck']),
      items(){
        if (this.isUserTypeCheck){
          return this.loginitems
        } else{
          return this.ansitems
        }
      }
    }
  }
</script>

<style lang="sass">
  #home-app-bar
    .v-tabs-slider
      max-width: 24px
      margin: 0 auto

    .v-tab
      &::before
        display: none
</style>
