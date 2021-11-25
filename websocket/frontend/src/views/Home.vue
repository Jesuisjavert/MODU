<template>
  <div class="home">
    방 번호 :<input type="text" v-model="roomId" /> 유저네임 :
    <input type="text" v-model="username" />
    <button @click="join()">테스트</button>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
  data() {
    return {
      roomId: "",
      username: "",
    };
  },
  methods: {
    join() {
      this.$socket.emit("join", this.roomId, this.username);
      sessionStorage.setItem("roomId", this.roomId);
      sessionStorage.setItem("username", this.username);
      this.$router.push({ name: "About" });
    },
  },
};
</script>
