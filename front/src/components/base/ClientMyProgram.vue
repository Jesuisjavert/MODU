<template>
    <div>
        <div v-for="(data,idx) in onlineLecturelist">
            <div>
            <v-row>
                <v-col cols="5" class="mr-auto">
                    <v-img 
                        :src="data.image_url" 
                        max-width="150"
                        max-height="150"
                        aria-inh
                    ></v-img>
                </v-col>
                <v-col cols="7" class="text-start">
                    <p class="mt-2">프로그램 명 : {{ data.program_title }}</p>
                    <p>{{ data.trainer_name }}</p>
                    <p>{{data.program_price_title}}</p>
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
                console.log(res, '여기는 반응입니다.')
                res.data.forEach((item)=>{
                    this.onlineLecturelist.push(item)
                })
                console.log(this.onlineLecturelist)
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