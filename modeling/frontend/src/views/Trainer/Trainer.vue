<template>
  <div class="about">
    <h1>Trainer 활성화 채팅창 목록</h1>
    <div v-for="(room, index) in chatRooms" :key="index">
      <div>{{ room.client_name }} 님과의 1대1 채팅</div>
      <button @click="pushChat(index)">채팅 참가하기</button>
    </div>
    <button @click="getChattingRoom()">테스트</button>
  </div>
</template>

<script>
import axios from "axios";
import constants from "@/api/constants";
import { mapState } from "vuex";
export default {
  data() {
    return {
      constants,
      chatRooms: [],
    };
  },
  methods: {
    pushChat(index) {
      let roomid = this.chatRooms[index].roomid.slice(2, -1);
      console.log(this.chatRooms[index].roomid);
      roomid;
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
          console.log(res);
        });
    },
  },
  computed: {
    ...mapState(["userToken", "username"]),
  },
  created() {
    this.getChattingRoom();
  },
};
</script>
