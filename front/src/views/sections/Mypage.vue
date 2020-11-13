<template>
    <!-- expansion panels 랑 treeview 사용 -->
    <!-- 트레이너일때 이번달 총수입 sparklines 사용 -->
    <MypageBg>
        <v-col cols="6" offset="3" class="py-0">
          <v-card color="rgb(255, 255, 255, 0.9)">
            <ItemRow class="px-10 py-10">
                <!-- <p>마이페이지</p> -->
                <TrainerProfile></TrainerProfile>
                <RevenueGraph></RevenueGraph>
                <TrainerMypageList></TrainerMypageList>
            </ItemRow>
          </v-card>
        </v-col>
    </MypageBg>
</template>

<script>
export default {
  name: "Mypage",
  components: {
    MypageBg: () => import('@/components/base/MypageBg'),
    ItemRow: () => import('@/components/base/ItemRow'),
    TrainerProfile: () => import('@/components/base/TrainerProfile'),
    RevenueGraph: () => import('@/components/base/RevenueGraph'),
    TrainerMypageList: () => import('@/components/base/TrainerMypageList'),
  },
}
</script>

<style>

</style>