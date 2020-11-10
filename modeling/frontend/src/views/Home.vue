<template>
  <div class="home">
      <div>
          메인화면
      </div>

      <v-container>
        <base-section-heading title="이번 주 최고의 트레이너" />
        
        <trainer-slider />
    </v-container>
  </div>
</template>

<script>
    export default {
        name: 'Home',
        components: {
          TrainerSlider: () => import('@/components/base/TrainerSlider'),
        },
        computed : {
        },
        methods : {

        },
        mounted(){
        }
    }
</script>
