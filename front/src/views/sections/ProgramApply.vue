<template>
  <v-container>
    <h3 class="title">프로그램 신청</h3>
    <div class="row">
      <div class="program-img">
        <img :src=program.image_url height="300px">
      </div>
      <div class="program-content">
        <h2>{{program.title}}</h2>
        <p>상품 명 : {{price.title}}</p>
        <p>결제 금액 : {{price.price}}원</p>
        <p>온라인 횟수 : {{price.online_count}}회</p>
        <p>온라인 횟수 : {{price.offline_count}}회</p>
        <h3>결제 방법</h3>
        <hr>
        <button class="btn btn-primary" @click="pay">카카오페이로 결제하기</button>
      </div>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'
import {mapMutations, mapState} from 'vuex'

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
          // console.log(err)
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
        let form = new FormData()
        form.append('item_name', this.program.title + " | " + this.price.title)
        // form.append('partner_order_id', this.program.trainer.id)
        form.append('total_amount', this.price.price)
        form.append('program_id', this.program.id)
        form.append('price_id', this.price.id)
        axios.post(`${this.constants.API_URL}kakaopay/`, form)
        .then((res)=>{
            this.SET_TID(res.data.tid)
            let payUrl = res.data.next_redirect_pc_url
            location.href = payUrl
        })
        .catch((err)=>{
            // console.log(err)
            alert("에러가 발생했습니다. 다시 시도해주세요")
            this.$router.push('/')
        })
    },
      
    ...mapMutations(['SET_TID'])
  },
  computed : {
      ...mapState(['tid'])
  }
}
</script>

<style scoped>
.title {
  margin: 40px 20px 20px;
  font-size: 48px;
  font-weight: 600;
  text-align: center;
}

.row {
  display: flex;
  justify-content: center;
}

.program-img {
  margin-right: 50px;
}

.program-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.program-content h2 {
  width: 200px;
  text-align: center;
  margin-bottom: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid #dddddd;
}

.program-content h3 {
  margin-bottom: 20px;
}

.btn-primary {
  padding: 4px 12px;
  border-radius: 4px;
  background-color: #FFEB33;
  transition: ease-in-out 0.2s;
}

.btn-primary:hover {
  background-color: #f0dc29;
}
</style>