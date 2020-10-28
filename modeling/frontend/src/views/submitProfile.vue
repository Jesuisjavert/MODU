<template>
  <div>
      <div>최초가입</div>
    
    <div v-if="!selected"><button @click="select('trainer')">트레이너 회원가입!</button>
    <button @click="select('client')">일반회원가입</button></div>
    <div v-else-if="selected === 'trainer'"><trainerSubmit/> </div>
    <div v-else> <clientSubmit/> </div>
    <button v-if="selected" @click="clear()">초기화버튼</button>
  </div>
</template>

<script>
import clientSubmit from '@/components/submit/clientSubmit.vue'
import trainerSubmit from '@/components/submit/trainerSubmit.vue'
export default {
    name : 'submitProfile',
    data(){
        return {
            selected : false
        }
    },
    methods : {
        select(input){
            this.selected = input
        },
        clear(){
            this.selected = false
        }
    },
    components : {
        clientSubmit,
        trainerSubmit

    }

}
</script>

<style>

</style>