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

export default {
    name : 'KakaoPayApprove',
    data: () => ({
    }),
    mounted(){
    },
    methods:{
      
    }
}
</script>