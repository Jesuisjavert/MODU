<template>
  <base-section
    id="affiliates"
    class="grey lighten-4"
    space="36"
  >
    <v-container>
      <base-section-heading title="이번 주 최고의 트레이너" />
      
      <trainer-slider />
      
    </v-container>
  </base-section>
</template>

<script>
  export default {
    name: 'TopTrainer',
    components: {
      TrainerSlider: () => import('@/components/base/TrainerSlider'),
    },
  }
</script>
