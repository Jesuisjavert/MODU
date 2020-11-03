<template>
    <div>
        <button @click="pay">카카오페이로 결제하기</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name : 'Mypage',
    data: () => ({
      dialog: false,
      items: [5000, 10000, 20000],
      value:'뭐지이건'
    }),
    methods:{
        pay(){
            let baseUrl = "http://127.0.0.1:8000/"
            let form = new FormData()
            form.append('amount', this.value)
            axios.post(baseUrl+"api/kakaopay/", form)
            .then((res)=>{
                // let payUrl = res.data.next_redirect_pc_url
                console.log(res)
                // location.href = payUrl
                // console.log(payUrl)
            })
            .catch((err)=>{
                console.log(err)
                alert("에러가 발생했습니다. 다시 시도해주세요")
                this.$router.push('/')
            })
        },
        approve(){
            let baseUrl = "http://127.0.0.1:8000/"
            let form = new FormData()
            // let pg_token = this.$route.query.pg_token
            form.append('amount', this.value)
            axios.post(baseUrl+"api/kakaopay/approve", form)
            .then((res)=>{
                let payUrl = res.data.next_redirect_pc_url
                console.log(res)
                location.href = payUrl
                console.log(payUrl)
            })
            .catch((err)=>{
                console.log(err)
                alert("에러가 발생했습니다. 다시 시도해주세요")
                this.$router.push('/')
            })
        },
    }
}
</script>