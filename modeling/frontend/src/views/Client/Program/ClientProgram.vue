<template>
  <div>
    <h1>프로그램 들!</h1>
    <div v-for="program in programs" :key="program.id" @click="detail(program.id)">
      <h3>{{program.title}}</h3>
      <img :src = program.image_url height="100px">
      <p>{{program.content}}</p>
      <hr>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'

export default {
    name : 'ClientProgram',
  
    data(){
      return {
        constants,
        programs: null,
      }
    },

    created() {
      this.get_programs()
    },

    methods: {
      get_programs() {
        axios.get(`${this.constants.API_URL}program/`)
          .then((res)=>{
            this.programs = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
      },
      detail(pk) {
        this.$router.push('/program/'+pk)
      }
    },
    
    computed : {
    }

}
</script>