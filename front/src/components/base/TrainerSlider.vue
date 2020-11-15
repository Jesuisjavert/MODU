<template>
  <div>
    <VueSlickCarousel v-bind="settings" v-if="trainers!=null">
      <div v-for="trainer in trainers" :key="trainer.id">
        <TrainerCard v-bind="trainer"/>
      </div>
    </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  import constants from "@/api/constants";
  
  import TrainerCard from '@/components/base/TrainerCard'

  import axios from 'axios'

  export default {
    name: 'MyComponent',
    components: { VueSlickCarousel, TrainerCard },
    data() {
      return {
        constants,
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
    created() {
      this.get_trainer()
    },
    methods: {
      get_trainer() {
        axios.get(`${this.constants.API_URL}trainer/`)
          .then((res)=>{
            this.trainers = res.data
          })
          .catch((err)=>{
            // console.log(err)
          })
      }
    }
  }
</script> 