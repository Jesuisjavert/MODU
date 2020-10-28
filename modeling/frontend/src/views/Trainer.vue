<template>
  <div class="about">
    <h1>Trainer</h1>
    <button @click="test">TEST</button>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'
export default {
  data(){
    return {
      constants,
    }
  },
  methods: {
    test() {
      const form = {

      }
      axios.post(`${this.constants.API_URL}trainer/1/comment/`,form)
        .then((res)=>{
          console.log(res.data)
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  }
}
</script>