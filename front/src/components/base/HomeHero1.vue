<template>
  <section id="hero">
    <video-bg
    :sources="['https://static.videezy.com/system/resources/previews/000/020/188/original/hanteln1.mp4']" 
    img="https://static.videezy.com/system/resources/previews/000/020/188/original/hanteln1.mp4"
    class="background-video white--text"
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
            <base-btn @click="gomembership">
              Find your Program
            </base-btn>

            <span class="font-weight-bold ml-6 mr-4 my-4">or</span>
            
            <base-btn
              :ripple="false"
              class="pa-1"
              height="auto"
              color="accent"
              text
              @click="gomembership"
            >
              Get Started Now
            </base-btn>

          </div>
        </v-responsive>
      </v-container>
    </video-bg>
  </section>
</template>

<script>
  export default {
    name: 'HomeHeadline',
    methods: {
      gomembership() {
        this.$router.push('/membership')
      }
    },
    computed: {
      minHeight () {
        const height = this.$vuetify.breakpoint.mdAndUp ? '100vh' : '50vh'
        return `calc(${height} - ${this.$vuetify.application.top}px)`
      },
    }
  }
</script>
<style scoped>
    .background-video {
        opacity: 0.81;
    }
</style>