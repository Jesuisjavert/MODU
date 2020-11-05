<template>
  <div>
  <VueSlickCarousel
  ref="c1"
  :asNavFor="focus2"
  :slidesToShow="4"
  :focusOnSelect="true">
    <div><h3>1</h3></div>
    <div><h3>2</h3></div>
    <div><h3>3</h3></div>
    <div><h3>4</h3></div>
    <div><h3>5</h3></div>
    <div><h3>6</h3></div>
  </VueSlickCarousel>
  
  <VueSlickCarousel 
    ref="c2"
    :asNavFor='focus1'
    :slidesToShow="2"
    :focusOnSelect="true"
  >
    <div><h1>1</h1></div>
    <div><h1>2</h1></div>
    <div><h1>3</h1></div>
    <div><h1>4</h1></div>
    <div><h1>5</h1></div>
    <div><h1>6</h1></div>
  </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  

  export default {
    name: 'CamSlider',
    components: { VueSlickCarousel },
    data(){
      return {
        c1 : '',
        c2 : '',
      }
    },
    computed : {
      focus1(){
        return this.c1
      },
      focus2(){
        return this.c2
      }
    },
    mounted(){
      this.c1 = this.$refs.c1
      this.c2 = this.$refs.c2
    }

  }
</script> 