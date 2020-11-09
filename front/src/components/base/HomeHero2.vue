<template>
  <section id="hero">
    <v-img
      :min-height="minHeight"
      :src="require('@/assets/modu35.jpg')"
      class="white--text"
      gradient="to right, rgba(45, 45, 45, .8), rgba(5, 11, 31, .8)"
      aspect-ratio="12"
    >
      <v-container class="fill-height px-4 py-12 mt-12 pt-12">
        <v-responsive
          class="d-flex align-center"
          height="100%"
          max-width="800"
          width="100%"
        >
          <base-heading title="운동루틴, 일정관리, 식단까지." />

          <base-body>
            캘린더 기능을 통해, 운동루틴과 트레이너와의 세션 및 식단까지 간편하게 관리 받아보세요.
          </base-body>

          <div
            :class="$vuetify.breakpoint.smAndDown ? 'flex-column align-start' : 'align-center'"
            class="d-flex flex-wrap"
          >
            <base-btn>
              Discover More
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