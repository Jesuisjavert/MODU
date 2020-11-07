<template>
  <section id="hero">
    <v-img
      :min-height="minHeight"
      :src="require('@/assets/modu34.jpg')"
      class="white--text"
      height="500"
    >
      <v-container class="fill-height px-4 py-12">
        <v-responsive
          class="d-flex align-center"
          height="100%"
          max-width="700"
          width="100%"
        >
          <base-heading title="당신을 위한, 당신에 의한, 당신의 트레이너를 찾아보세요" />

          <base-body>
            Infographic hypotheses influencer user experience Long madel ture gen-z paradigm shift client partner network product seilans solve management influencer analytics leverage virality.
            incubator seed round massmarket. 
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