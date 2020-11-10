<template>
  <div>
    <VueSlickCarousel v-bind="settings">
      <div><TrainerCard1 /></div>
      <div><TrainerCard2 /></div>
      <div><TrainerCard3 /></div>
      <div><TrainerCard1 /></div>
      <div><TrainerCard2 /></div>
      <div><TrainerCard3 /></div>
      <div><TrainerCard1 /></div>
      <div><TrainerCard2 /></div>
      <div><TrainerCard3 /></div>
    </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  
  import TrainerCard1 from '@/components/base/TrainerCard1'
  import TrainerCard2 from '@/components/base/TrainerCard2'
  import TrainerCard3 from '@/components/base/TrainerCard3'

  export default {
    name: 'MyComponent',
    components: { VueSlickCarousel, TrainerCard1, TrainerCard2, TrainerCard3},
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