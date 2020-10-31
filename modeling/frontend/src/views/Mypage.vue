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
                console.log(res)
            })
        }
    }
}
</script>