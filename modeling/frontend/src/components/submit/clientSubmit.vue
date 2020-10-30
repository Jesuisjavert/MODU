<template>
  <div>
      <div>여기는 클라이언트 가입 페이지입니다.</div>
      <label for="name"> 이름 </label>
      <input v-model="submitData.name" type="text" name="name" id="">
      <label for="age">나이</label>
      <input v-model="submitData.age" type="number" max='99' min='10' name="age">
      <label for="gender">성별</label>
      <select v-model='submitData.gender' name="gender" id="">
          <option value="남">남</option>
          <option value="녀">녀</option>
      </select>
      <button @click="submitClient()">제출</button>
  </div>
</template>

<script>
import axios from 'axios'
import {mapState} from 'vuex'
import constants from '@/api/constants'
export default {
    name : 'clientSubmit',
    data(){
        return {
            submitData : {
                name : '',
                age : '',
                gender : '',
                is_first : '2',
            },
            constants
        }
    },
    methods :{
        submitClient(){
            const Token = 'Bearer '+this.userToken
            axios.post(`${constants.API_URL}rest-auth/user/`,this.submitData,{
                    headers: {
                        Authorization: Token,
                    },
                    })
            .then((res)=>{
                console.log(res.data)
            })
            .catch((err)=>{
                console.log(err.response)
            })
        },
    },
    computed : {
        ...mapState(['userToken'])
    }

}
</script>

<style>

</style>