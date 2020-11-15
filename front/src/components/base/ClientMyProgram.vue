<template>
    <div>
        <div v-for="(data,idx) in onlineLecturelist">
            <div>
            <v-row>
                <v-col cols="5" class="mr-auto">
                    <v-img 
                        :src="data.image_url" 
                        max-width="100"
                        max-height="100"
                    ></v-img>
                </v-col>
                <v-col cols="7" class="text-start">
                    <p class="pt-2 ma-0">프로그램 명 : {{ data.program_title }}</p>
                    <span class="font-weight-bold mr-2">{{ data.trainer_name }}</span>
                    <span>트레이너</span>
                    <p>{{data.program_price_title}}</p>
                    <!-- <button @click="">정보보기</button> -->
                </v-col>
            </v-row>
            <br />
            <!-- <div style="boarder : solid"></div> -->
            </div>
        </div>
    </div>
</template>

<script>
import constants from '@/api/constants.js'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
    name: "ClientMyProgram",
    components: {
    },
    created() {
        this.get_programs()
    },
    computed: {
        ...mapState(['userToken'])
    },
    data() {
        return{
            onlineLecturelist: [],
            constants,
        }
    },
    methods: {
        get_programs() {
            const Token = "Bearer " + this.userToken;
            axios.get(`${this.constants.API_URL}client/program/`, {
                headers: {
                    Authorization: Token,
                },
            })
            .then((res) => {
                res.data.forEach((item)=>{
                    this.onlineLecturelist.push(item)
                })
                // const a = res.data.filter((item) => {
                //     console.log(item,'item입니다.')
                //     if (item._type == "온라인") {
                //     return item;
                //     }
            })
            // a.forEach((item)=>{
            //     this.onlineLecturelist.push(item)
            // })
            // console.log(this.onlineLecturelist,'-0---')
            // })
            .catch((err) => {
                console.log(err)
            })
        },
    }
}
</script>

<style>

</style>