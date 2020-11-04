<template>
  <div>
      <div>여기는 TrainerSubmit 하는 곳입니다.</div>
            <label for="name"> 이름 </label>
      <input v-model="submitData.name" type="text" name="name" id="">
      <label for="age">나이</label>
      <input v-model="submitData.age" type="number" max='99' min='10' name="age">
      <label for="gender">성별</label>
      <select v-model='submitData.gender' name="gender" id="">
          <option value="남">남</option>
          <option value="녀">녀</option>
      </select>
      <label for="address"> 주소 </label>
      <input type="text" name="address" v-model="submitData.address">
      <label for="content"> 자기소개 </label>
      <input type="text" name="content" v-model="submitData.content">
      <button @click="submitTrainer()">제출</button>
  </div>
</template>

<script>
import axios from 'axios'
import {mapState,mapMutations} from 'vuex'
import constants from '@/api/constants'
export default {
    name : 'trainerSubmit',
    data(){
      return {
            submitData : {
                name : '',
                age : '',
                gender : '',
                address : '',
                is_first : '1',
                content : '',
            },
            constants,
      }
    },
    methods : {
      submitTrainer(){
        const Token = 'Bearer '+this.userToken
            axios.post(`${constants.API_URL}rest-auth/user/`,this.submitData,{
                    headers: {
                        Authorization: Token,
                    },
                    })
            .then(()=>{
                this.SET_TYPETOKEN('trainer')
                
            })
            .catch((err)=>{
                console.log(err.response)
            })
      },
      ...mapMutations(['SET_TYPETOKEN'])
    },
    computed : {
        ...mapState(['userToken'])
    }

}
</script>

<style>

</style>