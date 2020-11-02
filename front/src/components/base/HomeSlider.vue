<template>
  <div>
    <VueSlickCarousel v-bind="settings">
      <div><HomeHero /></div>
      <div><HomeHero /></div>
      <div><HomeHero /></div>
    </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  
  import HomeHero from '@/components/base/HomeHero'

  export default {
    name: 'MyComponent',
    components: { VueSlickCarousel, HomeHero },
    data() {
        return {
          settings: {
            "dots": true,
            "infinite": true,
            "slidesToScroll": 1,
            "autoplay": true,
            "autoplaySpeed": 2000,
            "pauseOnDotsHover": true,
            "pauseOnFocus": true,
            "pauseOnHover": true
          }
        }
      },
  }
</script> 