<template>
  <v-container class="chat">
    <h1><i class="fas fa-comments"></i>1:1 문의</h1>
    <br>
    <div class="chat-box">
      <div>
        <div v-for="(mes, ind) in messages" :key="ind">
          <div :class="{ active: sameuser(ind), deactive: !sameuser(ind) }">
            <div :class="{ mychat: sameuser(ind), yourchat: !sameuser(ind) }">
              <div class="message-box">
                <span :class="{ mymessage: sameuser(ind), yourmessage: !sameuser(ind) }">{{ mes.message }}</span>
                <span class="time">{{ mes.time.slice(12,16) }}</span>
              </div>
              <!-- {{ mes.username }} -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="chat-insert">
      <input type="text" v-model="inputmessage" @keydown.enter="chat()" />
      <v-btn depressed @click="chat()">입력</v-btn>
    </div>
  </v-container>
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
      await axios.post(`${constants.API_URL}chat/log/`, data).then(() => {
        let acz = 0
        acz + 1
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
.chat {
  height: 80vh;
  width: 60vw;
  margin: auto;
}

i {
  color: #007BFF;
  margin-right: 10px;
}

.chat-box {
  padding: 12px;
  height: 60vh;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  border: 1px solid #dddddd;
  overflow-y:scroll
}

.active {
  text-align: right;
}
.deactive {
  text-align: left;
}

.mychat {
  color: #ffffff;
}

.yourchat {
  max-width: 20vw;
}

.chat-insert {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.chat-insert input {
  width: 700px;
  margin-right: 8px;
  border: 1px solid;
}

.chat-insert button {
  font-size: 16px;
  padding: 4px 8px;
}

.message-box {
  display: flex;
  flex-direction: column;
  margin: 4px 0px;
}

.mymessage {
  margin-left: 35vw;
  background-color: #007BFF;
  border-radius: 20px;
  padding: 8px 12px;
}

.yourmessage {
  min-width: 5vw;
  background-color: #E5E5EA;
  border-radius: 20px;
  padding: 8px 12px;
}

.time {
  margin: 2px;
  font-size: 12px;
  color: #cecece;
}
</style>
