<template>
  <div>
    <VueSlickCarousel v-bind="settings" v-for="trainer in trainers" :key="trainer.id">
      <div><TrainerCard v-bind="trainer"/></div>
    </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  
  import TrainerCard from '@/components/base/TrainerCard'

  import axios from 'axios'

  export default {
    name: 'MyComponent',
    components: { VueSlickCarousel, TrainerCard },
    data() {
        return {
          settings: {
          "centerMode": true,
          "centerPadding": "30px",
          "focusOnSelect": true,
          "infinite": true,
          "slidesToShow": 3,
          "speed": 500
          },
          trainers: null,
        }
      },
    methods: {
      get_trainer() {
        axios.get(`http://127.0.0.1:8000/api/trainer/`)
          .then((res)=>{
            this.trainers = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
      }
    }
  }
</script> 