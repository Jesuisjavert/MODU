<template>
  <div class="home">
      <div>
          메인화면
      </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
    export default {
        name: 'Home',
        computed : {
            ...mapGetters(['isLogined'])
        },
        methods : {
            loginCheck(){
                if(!this.isLogined){
                    this.$router.push({name:'Login'})

                }
                
            }
        },
        mounted(){
            this.loginCheck()
        }
    }
</script>
