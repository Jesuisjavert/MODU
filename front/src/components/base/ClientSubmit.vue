<template>
    <div>
        <base-heading class="white--text text-center mb-10 pb-5">손님 가입 페이지입니다</base-heading>
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
            </div>
        </v-card>
        <Btn @click="submitClient">제출하기</Btn>
    </div>
</template>

<script>
import axios from 'axios'
import {mapState,mapMutations} from 'vuex'
import constants from '@/api/constants'

export default {
    name: "ClientSubmit",
    components: {
        Btn: () => import('@/components/base/Btn'),
    },
    methods :{
        submitClient(){
            const Token = 'Bearer '+this.userToken
            axios.post(`${constants.API_URL}rest-auth/user/`, this.submitData, {
                headers: {
                    Authorization: Token,
                },
            })
            .then((res) => {
                console.log(res.data)
                this.SET_TYPETOKEN('client')
                this.$router.push({ name: 'Home' })
            })
            .catch((err) => {
                console.log(err.response)
            })
        },
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
                is_first : '2',
            },
            constants
        }
    },
}
</script>

<style>

</style>