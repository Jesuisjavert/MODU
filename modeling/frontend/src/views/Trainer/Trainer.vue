<template>
  <div class="about">
    <h1>1:1 문의 목록</h1>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">글쓴이</th>
          <th scope="col">답변상태</th>
          <th scope="col">답변하기</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(room, index) in chatRooms" :key="index">
          <th class="table-item" scope="row">{{index + 1 }}</th>
          <td class="table-item">{{ room.client_name }}님의 문의</td>
          <td class="table-item">답변대기</td>
          <td><button class="btn btn-primary" @click="pushChat(index)">채팅 참가하기</button></td>
        </tr>
      </tbody>
    </table>
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

<style scoped>
.about {
  width: 70vw;
  margin: auto;
}

h1 {
  margin-top: 40px;
}

.table {
  margin-top: 40px;
}

.table-item {
  vertical-align: middle;
}
</style>