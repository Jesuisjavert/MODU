<template>
  <div>
    <h1>This is an Chat page</h1>
    <div v-for="(mes, ind) in messages" :key="ind">
      <div :class="{ active: sameuser(ind), deactive: !sameuser(ind) }">
        {{ ind }} : {{ mes.username }} : <span>{{ mes.message }}</span> 작성시간
        :{{ mes.time }}
      </div>
    </div>
    <input type="text" v-model="inputmessage" />
    <button @click="chat()">제출</button>
    <button @click="getChatLog()">테스트!</button>
  </div>
</template>

<script>
import axios from "axios";
import constants from "@/api/constants.js";
import { mapState } from "vuex";
export default {
  name: "Chat",
  data() {
    return {
      messages: [],
      inputmessage: "",
      constants,
    };
  },
  methods: {
    async getChatLog() {
      await axios
        .get(`${constants.API_URL}chat/log`, {
          params: { roomId: this.chatroomId },
          headers: {
            Authorization: `Bearer ${this.userToken}`,
          },
        })
        .then((res) => {
          res.data.forEach((item) => {
            this.messages.push(item);
          });
        });
    },
    async chat() {
      const roomId = this.chatroomId;
      const username = this.username;
      let today = new Date();

      let year = today.getFullYear(); // 년도
      let month = today.getMonth() + 1; // 월
      let date = today.getDate(); // 날짜
      let hours = today.getHours(); // 시
      let minutes = today.getMinutes(); // 분
      let seconds = today.getSeconds(); // 초
      let time = `${year}-${month}-${date}T${hours}:${minutes}:${seconds}`;

      const data = {
        chatroomId: roomId,
        username: username,
        message: this.inputmessage,
        time: time,
      };
      await axios.post(`${constants.API_URL}chat/log/`, data).then((res) => {
        console.log(res);
      });
      this.$socket.emit("chat", roomId, username, this.inputmessage, time);
      this.messages.push({
        username: username,
        message: this.inputmessage,
        time: time,
      });
      this.inputmessage = "";
    },
    sameuser(ind) {
      if (this.username == this.messages[ind].username) {
        return true;
      } else {
        return false;
      }
    },
  },
  computed: {
    ...mapState(["username", "userToken"]),
    chatroomId() {
      return sessionStorage.getItem("chatroomId");
    },
  },
  created() {
    this.getChatLog();
    this.$socket.on("chat", (data) => {
      this.messages.push({
        username: data.username,
        message: data.message,
        time: data.time,
      });
    });
  },
};
</script>

<style scoped>
.active {
  background-color: yellow;
  text-align: right;
}
.deactive {
  text-align: left;
}
</style>
