<template>
  <div>
    <VueSlickCarousel v-bind="settings">
      <div><ProgramCard1 /></div>
      <div><ProgramCard2 /></div>
      <div><ProgramCard3 /></div>
      <div><ProgramCard1 /></div>
      <div><ProgramCard2 /></div>
      <div><ProgramCard3 /></div>
      <div><ProgramCard1 /></div>
      <div><ProgramCard2 /></div>
      <div><ProgramCard3 /></div>
    </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  
  import ProgramCard1 from '@/components/base/ProgramCard1'
  import ProgramCard2 from '@/components/base/ProgramCard2'
  import ProgramCard3 from '@/components/base/ProgramCard3'

  export default {
    name: 'MyComponent',
    components: { VueSlickCarousel, ProgramCard1, ProgramCard2, ProgramCard3},
    data() {
        return {
          settings: {
          "centerMode": true,
          "centerPadding": "30px",
          "focusOnSelect": true,
          "infinite": true,
          "slidesToShow": 3,
          "speed": 500
          }
        }
      },
  }
</script> 