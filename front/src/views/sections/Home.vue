<template>
  <v-container
    id="home"
    class="pb-0 px-0"
    fluid
    tag="section"
  >
   
    <home-slider />

  </v-container>
</template>

<script>
  export default {
    name: 'Home',

    components: {
      HomeSlider: () => import('@/components/base/HomeSlider')
    },
  }
</script>
