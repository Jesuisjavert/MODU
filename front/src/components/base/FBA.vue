<template>
    <v-menu
        v-model="menu"
        :close-on-content-click="false"
        top
        left
        max-width="90%"
        min-width="275"
        offset-x
        offset-y
        origin="bottom right"
        transition="scale-transition"
    >
        <template v-slot:activator="{ attrs, on }">
        <v-card
            id="settings"
            class="py-2 px-4 icon-card"
            color="rgb(255, 0, 0, 0)"
            black
            flat
            style="position: fixed; bottom: 10%; right: 6%;"
            v-bind="attrs"
            v-on="on"
        >
            <v-icon large>
            mdi-bell
            </v-icon>
        </v-card>
        </template>

        <v-card class="">
        <base-title
            align="center"
            title="알림창"
            space="0"
        />

        <v-card-text>
            <div v-for="notification in notificationlist" :key="notification.id">
                <v-alert color="green" type="success" class="mb-1" v-if="notification.is_view">
                    <v-row>
                        <v-col cols="auto" class="mr-auto">
                            <p>망할 {{ notification.program_title }} 의 강의가 시작되었습니다.</p>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn
                                @click="joinWeb(notification.id)"
                            >
                            입장하기
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-alert>
                <v-alert color="blue" type="info" class="mb-1" v-else>
                    <v-row>
                        <v-col cols="auto" class="mr-auto">
                            <p>{{ notification.program_title }} 의 강의가 시작되었습니다.</p>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn
                                @click="joinWeb(notification.id)"
                            >
                            입장하기
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-alert>
            </div>
        </v-card-text>
        </v-card>
    </v-menu>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants.js'
import { mapState } from 'vuex'
export default {
    name: "FBA",
    data() {
        return {
            menu: false,
            constants,
            notificationlist : []
        }
    },
    methods : {
        clicktest(event){
            console.log(event)
        },
        joinWeb(pk){
            const Token = 'Bearer ' + this.userToken
            axios.put(`${constants.API_URL}client/notification/${pk}/`, null,{
                headers: {
                    Authorization: Token,
                },
            })
            .then((res)=>{
                if(res.data.data == false){
                    alert(res.data.notication)
                } else {

                    $cookies.set('roomID', res.data.data)
                    this.$router.push({ name: 'WebCam' })
                }
            })

        },
        getNotification () {
            const Token = 'Bearer ' + this.userToken
            axios.get(`${constants.API_URL}client/notification/`,{
                headers: {
                    Authorization: Token,
                },
            })
            .then((res) => {
                if(res.data != false){
                    res.data.forEach((item)=>{
                        this.notificationlist.push(item)
                    })

                }
            })
            .catch((err)=>{
                console.log(err.response)
            })
        },
    },
    computed : {
        ...mapState(['userToken'])
    },
    components: {
        WebJoinBtn: () => import('@/components/base/WebJoinBtn'),
    },
    mounted(){
        this.getNotification()
    }
}
</script>

<style>
    
</style>