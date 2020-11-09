<template>
  <section id="hero">
    <v-img
      :min-height="minHeight"
      :src="require('@/assets/modu34.jpg')"
      class="white--text"
      gradient="to right, rgba(45, 45, 45, .8), rgba(5, 11, 31, .8)"
      aspect-ratio="12"
    >
      <v-container class="fill-height px-4 py-12 mt-12 pt-12" >
        <v-responsive
          class="d-flex align-center"
          height="100%"
          max-width="850"
          width="100%"
        >
          <base-heading title="당신을 위한, 당신에 의한, 당신의 트레이너를 찾아보세요" />

          <base-body>
            모두의 헬스에서 당신이 원하는 Online / Offline 코스를 검색해보세요. 운동루틴 관리부터 식단조절 프로그램까지. 체계적인 프로그램을 매칭 시켜드립니다.
          </base-body>

          <div
            :class="$vuetify.breakpoint.smAndDown ? 'flex-column align-start' : 'align-center'"
            class="d-flex flex-wrap"
          >
            <base-btn>
              프로그램 찾기
            </base-btn>

            <span class="font-weight-bold ml-6 mr-4 my-4">or</span>

            <base-btn
              :ripple="false"
              class="pa-1"
              height="auto"
              text
            >
              Get Started Now
            </base-btn>
          </div>
        </v-responsive>
      </v-container>
    </v-img>
  </section>
</template>

<script>
  export default {
    name: 'HomeHeadline',
    computed: {
      minHeight () {
        const height = this.$vuetify.breakpoint.mdAndUp ? '100vh' : '50vh'
        return `calc(${height} - ${this.$vuetify.application.top}px)`
      },
    }
  }
</script>