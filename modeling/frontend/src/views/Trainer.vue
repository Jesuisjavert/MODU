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
      axios.get(`${this.constants.API_URL}trainer/1/comment/`)
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