<template>
  <div>
    <h1>프로그램 신청</h1>

    <hr>
    
		<img :src=program.image_url height="300px">
    <h3>프로그램명 : {{program.title}}</h3>
    <p>결제 명 : {{price.title}}</p>
    <p>결제 금액 : {{price.price}}</p>
    <p>온라인 횟수 : {{price.online_count}}</p>
    <p>온라인 횟수 : {{price.offline_count}}</p>

    <hr>

    <h3>결제 방법</h3>
    <button @click="pay">카카오페이로 결제하기</button>

  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'

export default {
    name: "ProgramApply",
    data(){
      return {
        constants,
        program: {
					"image": null,
					"title": null,
					"content": null,
        },
        price: {
          "title" : null,
          "price" : null,
          "online_count": null,
          "offline_count": null,
        }
      }
    },

    created() {
			this.get_program()
    },

    methods: {
      get_program() {
				const pk = this.$route.query.program
        axios.get(`${this.constants.API_URL}program/`+pk)
          .then((res)=>{
            this.program = res.data
            this.get_price()
          })
          .catch((err)=>{
            console.log(err)
          })
      },
      get_price() {
        const pk = this.$route.query.price
        this.program.programprice.forEach(element => {
          if (pk==element.id){
            this.price = element
          }
        });
      },
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