<template>
<div>
    <router-link to="/">메인 화면</router-link> |
    <router-link  v-if="!isLogined" to="/login">로그인</router-link>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name : 'Header',
    data(){
        return {

        }
    },
    methods : {

    },
    computed : {
        ...mapGetters(['isLogined'])
    }

}
</script>

<style>

</style>