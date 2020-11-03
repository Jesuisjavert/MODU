<template>
    <div>
        <h2>결제가 완료되었습니다!</h2>
        <div>
          <h3>주문자 정보</h3>
          <!-- <div>
            <div><div>주문번호</div><div>{{ res.partner_order_id }}</div></div>
            <div><div>상품명</div><div>{{ res.item_name }}</div></div>
            <div><div>결제금액</div><div>{{ amount }}원</div></div>
            <div><div>결제승인시각</div><div>{{ res.approved_at }}</div></div>
          </div> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name : 'KakaoPayApprove',
    data: () => ({
    }),
    mounted(){
        console.log(this.$route.query.pg_token)
    },
    methods:{
      approve(){
            let baseUrl = "http://127.0.0.1:8000/"
            let form = new FormData()
            // let pg_token = this.$router.params
            form.append('amount', this.value)
            axios.post(baseUrl+"api/kakaopay/", form)
            .then((res)=>{
                let payUrl = res.data.next_redirect_pc_url
                console.log(res)
                location.href = payUrl
                // console.log(payUrl)
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