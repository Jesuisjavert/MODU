<template>
    <div class="container" v-if="!!this.userData.length">
        <!-- <ItemColumn>
            <v-btn>프로필사진</v-btn>
            <v-btn>프로필정보</v-btn>
        </ItemColumn> -->
        <v-row>
            <v-col cols="auto">
                <v-img
                    :src="this.userData[0].user.image_url"
                    max-height="150"
                    max-width="150"
                    class="rounded-circle mr-5"
                ></v-img>
            </v-col>
            <v-col cols="auto" class="text-start">
                <p>{{ this.userData[0].name }}</p>
                <p>{{ this.userData[0].address }}</p>
                <v-row v-if="!!this.userData[0].tags">
                    <v-col v-for="(tag, i) in userData1.tags" :key="tag.id">
                        <v-chip
                            class="mr-1"
                            color="red"
                            text-color="white"
                        >
                            {{ userData1.tags[i].name }}
                        </v-chip>
                    </v-col>
                </v-row>
                <!-- <p>그외 정보들 넣을거</p> -->
            </v-col>
            <v-col cols="auto" class="ml-auto">
                <!-- <v-icon @click="updateProfile" style="cursor: pointer">
                    mdi-cog
                </v-icon> -->
                <TrainerInfoModal></TrainerInfoModal>
            </v-col>
        </v-row>
        <h3>여기는 자기소개입니다</h3>
        <pre id="content">{{userData[0].content}}</pre>
    </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants.js'
import { mapState } from 'vuex'
import ItemColumn from './ItemColumn.vue'

export default {
    name: "TrainerProfile",
    components: {
        ItemColumn: () => import('@/components/base/ItemColumn'),
        Btn: () => import('@/components/base/Btn'),
        TrainerInfoModal: () => import('@/components/base/TrainerInfoModal'),
    },
    data () {
        return {
            userData: [],
            userData1: null,
            constants,
        }
    },
    computed: {
        ...mapState(['userToken']),
    },
    created() {
        this.fetchData()
        console.log(this.userData)
    },
    methods: {
        async fetchData() {
            const Token = 'Bearer ' + this.userToken 
            await axios.get(`${constants.API_URL}rest-auth/user`, {
                headers: {
                    Authorization: Token,
                },
            })
            .then((res) => {
                // console.log(res)
                this.userData.push(res.data)
                this.userData[0].content.replaceAll("\n", "<br>");
                // console.log(this.userData)
                this.userData1 = this.userData[0]
                // console.log(this.userData1, 'asdfasdf')
                // console.log(this.userData[0].user.image_url)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        updateProfile() {
            console.log('프록필수정')
            const Token = 'Bearer ' + this.userToken
            axios.put(`${constants.API_URL}trainer/`, {
                headers: {
                    Authorization: Token,
                },
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        }
    },
}
</script>

<style>

</style>