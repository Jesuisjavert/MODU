<template>
  <div>
    <div>내 프로그램 관리 페이지</div>
    <div
      v-for="program in programs"
      :key="program.id"
      @click="detail(program.id)"
    >
      <h3>{{ program.title }}</h3>
      <img :src="program.image_url" height="100px" />
      <p>{{ program.content }}</p>
      <br />
    </div>
    <router-link :to="{ name: 'ProgramCreate' }">새 프로그램 등록</router-link>
  </div>
</template>

<script>
import axios from "axios";
import constants from "@/api/constants";
import { mapState } from "vuex";

export default {
  name: "Program",

  data() {
    return {
      constants,
      programs: null,
    };
  },

  created() {
    this.get_programs();
  },

  methods: {
    get_programs() {
      const Token = "Bearer " + this.userToken;
      axios
        .get(`${this.constants.API_URL}trainer/program/`, {
          headers: {
            Authorization: Token,
          },
        })
        .then((res) => {
          console.log(res.data, "0-");
          this.programs = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    detail(pk) {
      this.$router.push("program/" + pk);
    },
  },

  computed: {
    ...mapState(["userToken"]),
  },
};
</script>

<style></style>
