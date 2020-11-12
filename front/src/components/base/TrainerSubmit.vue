<template>
    <div>
        <base-heading class="white--text text-center mb-10 pb-5">트레이너 가입 페이지입니다</base-heading>
        <v-card color="rgb(255, 255, 255, 0.7)" class="container mb-10">
            <div class="mx-5 my-5 font-weight-black">
                <v-text-field
                label="이름"
                :rules="rules"
                hide-details="auto"
                type="text"
                v-model="submitData.name"
                ></v-text-field>
                <v-row class="mt-5">
                    <v-col cols="5">
                        <v-text-field
                        label="나이"
                        :rules="rules"
                        hide-details="auto"
                        type="number"
                        v-model="submitData.age"
                        ></v-text-field>
                    </v-col>
                    <v-col cols="5" offset="2">
                        <v-select
                        :items="genders"
                        label="성별"
                        v-model="submitData.gender"
                        ></v-select>
                    </v-col>
                </v-row>
                <v-text-field
                label="주소"
                :rules="rules"
                hide-details="auto"
                type="text"
                v-model="submitData.address"
                ></v-text-field>
                <v-text-field
                class="my-10"
                label="자기소개"
                hide-details="auto"
                type="text"
                v-model="submitData.content"
                ></v-text-field>
            </div>
        </v-card>
        <Btn @click="submitTrainer">제출하기</Btn>
    </div>
</template>

<script>
import axios from 'axios'
import {mapState,mapMutations} from 'vuex'
import constants from '@/api/constants'

export default {
    name: "TrainerSubmit",
    components: {
        Btn: () => import('@/components/base/Btn'),
    },
    methods: {
        submitTrainer(){
        const Token = 'Bearer '+this.userToken
            axios.post(`${constants.API_URL}rest-auth/user/`,this.submitData,{
                headers: {
                    Authorization: Token,
                },  
            })
            .then(()=>{
                this.SET_TYPETOKEN('trainer')
                this.$router.push({ name: 'Home' })
            })
            .catch((err)=>{
                console.log(err.response)
            })
        },
        ...mapMutations(['SET_TYPETOKEN'])
    },
    computed : {
        ...mapState(['userToken'])
    },
    data() {
        return {
            rules: [
                value => !!value || '필수 입력사항입니다.',
                // value => (value && value.length >= 3) || 'Min 3 characters',
            ],
            genders: [
                '남',
                '여',
            ],
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
}
</script>

<style>

</style>