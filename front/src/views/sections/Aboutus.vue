<template>
  <v-container
    id="about us"
    class="pa-0"
    fluid
    tag="section"
  >
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      > <br><br>
        <v-img
          src="@/assets/modu.png"
          class="align-self-stretch"
          max-height="400"
          contain
        />
        <br><br>
      </v-col>

      <v-col
        class="d-block d-md-flex align-center grey lighten-3 pa-6"
        cols="12"
        md="6"
      >
        <v-responsive
          class="mx-auto px-3 px-md-12"
          max-width="750"
        >
          <h1
            class="mb-6"
            :class="$vuetify.breakpoint.mdAndUp ? 'display-1' : 'display-1'"
          >
            Hi, We're Health for Everyone<br>
          </h1>

          <p class="mal">
           모두의 헬스는 온/오프라인 헬스 트레이너–개인PT회원 관리 및 
           <br>온라인 홈트레이닝 화상대면 관리 플랫폼 서비스입니다.
           <br>가장 관심있으신 PT 프로그램을 찾아보시고, 가입해보세요.
           <br>KaKao Login 과 KakaoPay 를 이용해서, 간편하게 이용하실 수 있습니다.
           <br>건강한 삶을 위하여, 우리 모두 헬스 합시다!
          </p>
          <h4>
            by 모두의 헬스 개발자팀
          </h4>
        </v-responsive>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
  export default {
    name: 'Aboutus',
    components: {
    }
  }
</script>

<style scoped>
.mal {
 line-height: 150%; 
}
</style>

