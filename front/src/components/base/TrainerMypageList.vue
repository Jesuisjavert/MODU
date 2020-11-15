<template>
    <v-expansion-panels focusable>
        <v-expansion-panel
        v-for="(item,i) in items"
        :key="i"
        >
            <v-expansion-panel-header disable-icon-rotate>
                <p class="text-center mb-0" v-if="item.title == '프로그램 추가'" @click="goProgramCreate">{{ item.title }}</p>
                <p class="text-center mb-0" v-else>{{ item.title }}</p>
                <template v-slot:actions>
                    <v-icon></v-icon>
                </template>
            </v-expansion-panel-header>
            <v-expansion-panel-content v-if="item.title == '고객관리'">
                <p v-for="client in item.content" :key="client.name">
                    {{ client }}
                </p>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-else-if="item.title == '나의 프로그램'">
                <TrainerMyProgram></TrainerMyProgram>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-else-if="item.title == '이번달 수입'">
                <RevenueGraph></RevenueGraph>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-else-if="item.title == '채팅 참가하기'">
                <v-col v-if="chatRooms.length > 0">
                    <v-col v-for="(room, index) in chatRooms" :key="index">
                        <v-row>
                            <v-col cols="auto" class="mr-auto">
                                <p>{{room.client_name}}</p>
                            </v-col>
                            <v-col cols="auto">
                                <button @click="pushChat(index)">참가하기</button>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-col>
                <v-col v-else>
                    <p>진행중인 채팅이 없습니다</p>
                </v-col>
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
</template>

<script>
import axios from "axios";
import constants from "@/api/constants";
import { mapState } from 'vuex';
export default {
    name: "TrainerMypage",
    components: {
        TrainerMyProgram: () => import('@/components/base/TrainerMyProgram'),
        RevenueGraph: () => import('@/components/base/RevenueGraph'),
    },
    data() {
        return {
            chatRooms :[],
            items: [
                {
                    title: '나의 프로그램',
                },
                
                {
                    title: '프로그램 추가',
                },
                {
                    title: '이번달 수입',
                },
                {
                  title: '채팅 참가하기',
                },
                
                {
                    title: '고객관리',
                    content: [
                        '이창완',
                        '강동훈',
                        '강병국',
                        '배용균',
                    ]
                },
            ],
        }
    },
    computed : {
        ...mapState(['userToken','username'])
    },
    created(){
      this.getChattingRoom()
    },
    methods: {
        goProgramCreate() {
            this.$router.push({ name: 'ProgramCreate' })
        },
        pushChat(index) {
            let roomid = this.chatRooms[index].roomid.slice(2, -1);
            sessionStorage.setItem("chatroomId", roomid);
            this.$socket.emit("join", roomid, this.username);
            this.$router.push({ name: "Chat" });
            },
        getChattingRoom() {
            const Token = `Bearer ${this.userToken}`;
            axios
                .get(`${constants.API_URL}chat/`, {
                headers: {
                    Authorization: Token,
                },
                })
                .then((res) => {
                res.data.forEach((item) => {
                    this.chatRooms.push(item);
                });
                // console.log(res);
                });
            },
    },
}
</script>

<style>

</style>