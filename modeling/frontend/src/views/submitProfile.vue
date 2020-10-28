<template>
  <div>
      <div>최초가입</div>
    <button @click="select('trainer')">트레이너 회원가입!</button>
    <button @click="select('client')">일반회원가입</button>
    <div v-if="!selected">처음화면</div>
    <div v-else-if="selected === 'trainer'">트레이너!!!!</div>
    <div v-else>일반회원!!!!!!!!!!!!!!!!!!!!!</div>
  </div>
</template>

<script>
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
        }
    },

}
</script>

<style>

</style>