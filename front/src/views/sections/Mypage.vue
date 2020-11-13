<template>
    <!-- expansion panels 랑 treeview 사용 -->
    <!-- 트레이너일때 이번달 총수입 sparklines 사용 -->
    <div>
        <v-col cols="6" offset="3">
          <ItemRow>
              <!-- <p>마이페이지</p> -->
              <TrainerProfile></TrainerProfile>
              <RevenueGraph></RevenueGraph>
          </ItemRow>
        </v-col>
    </div>
</template>

<script>
export default {
  name: "Mypage",
  components: {
    ItemRow: () => import('@/components/base/ItemRow'),
    TrainerProfile: () => import('@/components/base/TrainerProfile'),
    RevenueGraph: () => import('@/components/base/RevenueGraph'),
  },
}
</script>

<style>

</style>