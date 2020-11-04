<template>
<div>
    <router-link to="/">메인 화면</router-link> |
    <router-link  v-if="!isLogined" to="/login">로그인</router-link>
    <router-link  :to="trainer.url" v-for="trainer in trainerlist" :key="trainer.url" v-if="userType === 'trainer'" >{{trainer.name}} |</router-link>
</div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
export default {
    name : 'Header',
    data(){
        return {
            trainerlist : [{'url' : 'Trainer',
            'name' : '트레이너'},
            {'url': 'Program',
            'name' : '프로그램'}]
        }
    },
    methods : {

    },
    computed : {
        ...mapGetters(['isLogined']),
        ...mapState(['userType'])
    }

}
</script>

<style>

</style>