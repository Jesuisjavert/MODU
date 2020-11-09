<template>
  <base-section
    id="affiliates"
    class="grey lighten-4"
    space="36"
  >
    <v-container>
      <base-section-heading title="이번 주 최고의 프로그램" />
      
      <program-slider />
      
    </v-container>
  </base-section>
</template>

<script>
  export default {
    name: 'TopProgram',
    components: {
      ProgramSlider: () => import('@/components/base/ProgramSlider'),
    },
  }
</script>
