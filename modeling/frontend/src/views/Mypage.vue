<template>
    <div>
        <h1>클라이언트 마이페이지</h1>
        <button @click="get_data()">test</button>
    </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'
import {mapState} from 'vuex'

export default {
    name : 'Mypage',
    data() {
        return{
            constants,
        }
    },
    methods:{
        get_data() {
            const Token = 'Bearer '+this.userToken
            axios.get(`${this.constants.API_URL}client/`,{
                headers: {
                    Authorization: Token,
                },
            })
            .then((res)=>{
                console.log(res.data)
            })
        }
    },
    computed : {
        ...mapState(['userToken'])
    }
}
</script>