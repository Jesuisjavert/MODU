<template>
  <div>
    <VueSlickCarousel v-bind="settings" v-if="programs!=null">
      <div v-for="program in programs" :key="program.id"><ProgramCard v-bind="program"/></div>
    </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  
  import ProgramCard from '@/components/base/ProgramCard'
  
  import axios from 'axios'

  export default {
    name: 'MyComponent',
    components: { VueSlickCarousel, ProgramCard},
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
        programs: null,
      }
    },
    created() {
      this.get_program()
    },
    methods: {
      get_program() {
        axios.get(`http://127.0.0.1:8000/api/program/`)
          .then((res)=>{
            this.programs = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
      }
    }
  }
</script> 