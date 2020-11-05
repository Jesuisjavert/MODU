<template>
  <div>
      <div>프로그램 디테일</div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'

export default {
    name : 'ProgramDetail',
  
    data(){
      return {
        constants,
        programs: null,
      }
    },

    created() {
      this.get_program()
    },

    methods: {
      get_program() {
				const pk = this.$route.params.pk
        axios.get(`${this.constants.API_URL}program/`+pk)
          .then((res)=>{
						console.log(res.data)
            this.program = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
      },
    },
    
    computed : {
    }

}
</script>

<style>

</style>