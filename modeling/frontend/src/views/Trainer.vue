<template>
  <div class="about">
    <h1>Trainer</h1>
    <button @click="test">TEST</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  methods: {
    test() {
      const form = {

      }
      axios.post('http://127.0.0.1:8000/api/trainer/1/comment/',form)
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