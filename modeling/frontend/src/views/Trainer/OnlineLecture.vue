<template>
  <div>
    Online 수업 관리 페이지입니다.
    <div v-for="(data, index) in onlineLecturelist" :key="index">
      <div>
        <img :src="data.image_url" width="20%" alt="" />
        프로그램 명 : {{ data.title }}
        <button v-if="onlineScheduleCheck(index)" @click="test(index)">
          수업 시작
        </button>
        <br />
        <div style="boarder : solid"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import constants from "@/api/constants.js";
import { mapState } from "vuex";
export default {
  name: "OnlineLecture",
  data() {
    return {
      onlineLecturelist: [],
      constants,
    };
  },
  methods: {
    test(index) {
      function guid() {
        function s4() {
          return (((1 + Math.random()) * 0x10000) | 0)
            .toString(16)
            .substring(1);
        }
        return (
          s4() +
          s4() +
          "-" +
          s4() +
          "-" +
          s4() +
          "-" +
          s4() +
          "-" +
          s4() +
          s4() +
          s4()
        );
      }
      let webRtcroomId = guid();
      let data = {
        program_id: this.onlineLecturelist[index].id,
        webRtcroomId: webRtcroomId,
      };
      const Token = "Bearer " + this.userToken;
      axios
        .post(`${constants.API_URL}trainer/program/online/`, data, {
          headers: {
            Authorization: Token,
          },
        })
        .then((res) => {
          console.log(res);
        });
    },
    onlineScheduleCheck(index) {
      let onlinelecture = this.onlineLecturelist[index];
      let today = new Date();
      var week = [
        "일요일",
        "월요일",
        "화요일",
        "수요일",
        "목요일",
        "금요일",
        "토요일",
      ];
      var dayOfWeek = week[today.getDay()];
      let flag = false;
      onlinelecture.programschedule.forEach((item) => {
        if (item.day == dayOfWeek) {
          flag = true;
        }
      });
      if (flag) {
        return true;
      } else {
        return false;
      }
    },
    get_programs() {
      const Token = "Bearer " + this.userToken;
      axios
        .get(`${this.constants.API_URL}trainer/program/online/`, {
          headers: {
            Authorization: Token,
          },
        })
        .then((res) => {
          this.onlineLecturelist = res.data.filter((item) => {
            if (item._type == "온라인") {
              return item;
            }
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapState(["userToken"]),
  },
  mounted() {
    this.get_programs();
  },
};
</script>

<style></style>
