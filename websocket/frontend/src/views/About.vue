<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div v-for="(mes, ind) in messages" :key="ind">
      {{ ind }} : {{ mes.username }} : {{ mes.message }} 작성시간 :{{
        mes.time
      }}
    </div>
    <input type="text" v-model="inputmessage" />
    <button @click="chat()">제출</button>
  </div>
</template>

<script>
export default {
  name: "Chat",
  data() {
    return {
      messages: [],
      inputmessage: "",
    };
  },
  methods: {
    chat() {
      const roomId = sessionStorage.getItem("roomId");
      const username = sessionStorage.getItem("username");
      let today = new Date();

      let year = today.getFullYear(); // 년도
      let month = today.getMonth() + 1; // 월
      let date = today.getDate(); // 날짜
      let hours = today.getHours(); // 시
      let minutes = today.getMinutes(); // 분
      let seconds = today.getSeconds(); // 초
      let time = `${year}-${month}-${date}T${hours}:${minutes}:${seconds}`;
      this.$socket.emit("chat", roomId, username, this.inputmessage, time);
      this.messages.push({
        username: username,
        message: this.inputmessage,
        time: time,
      });
      this.inputmessage = "";
    },
  },
  created() {
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
