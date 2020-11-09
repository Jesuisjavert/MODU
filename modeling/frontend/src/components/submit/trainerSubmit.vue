<template>
  <div>
    <div>여기는 TrainerSubmit 하는 곳입니다.</div>
    <label for="name"> 이름 </label>
    <input v-model="submitData.name" type="text" name="name" id="" />
    <label for="age">나이</label>
    <input
      v-model="submitData.age"
      type="number"
      max="99"
      min="10"
      name="age"
    />
    <label for="gender">성별</label>
    <select v-model="submitData.gender" name="gender" id="">
      <option value="남">남</option>
      <option value="녀">녀</option>
    </select>

    <div>
      <span>태그등록 : </span>
      <input @input="autocomplete" type="text" />
      태그등록
    </div>

    <div>
      <div v-for="(tag, index) in autocompletelist" :key="index">
        <li>{{ tag }} <button @click="appendTag(tag)">추가</button></li>
      </div>
    </div>

    <label for="address"> 주소 </label>
    <input type="text" name="address" v-model="submitData.address" />
    <label for="content"> 자기소개 </label>
    <input type="text" name="content" v-model="submitData.content" />
    <div v-for="(day, index) in schedule" :key="index">
      <div v-if="!day.disabled">
        <label :for="'e' + index">{{ day.day }}</label>
        <input
          v-model="day.start_hour"
          type="time"
          step="3600"
          :name="'e' + index"
        />
        ~
        <input
          v-model="day.end_hour"
          type="time"
          step="3600"
          :name="'e' + index"
        />
      </div>
      <div v-else>{{ day.day }} 는 쉬는날입니다.</div>
      <label :for="'c' + index">휴무일</label>
      <input v-model="day.disabled" type="checkbox" :name="'c' + index" id="" />
    </div>
    <button @click="submitTrainer()">제출</button>
  </div>
</template>

<script>
import axios from "axios";
import { mapState, mapMutations } from "vuex";
import constants from "@/api/constants";
export default {
  name: "trainerSubmit",
  data() {
    return {
      submitData: {
        name: "",
        age: "",
        gender: "",
        address: "",
        is_first: "1",
        content: "",
      },
      schedule: [
        {
          day: "월요일",
          start_hour: "00:00",
          end_hour: "23:00",
          disabled: false,
        },
        {
          day: "화요일",
          start_hour: "00:00",
          end_hour: "23:00",
          disabled: false,
        },
        {
          day: "수요일",
          start_hour: "00:00",
          end_hour: "23:00",
          disabled: false,
        },
        {
          day: "목요일",
          start_hour: "00:00",
          end_hour: "23:00",
          disabled: false,
        },

        {
          day: "금요일",
          start_hour: "00:00",
          end_hour: "23:00",
          disabled: false,
        },
        {
          day: "토요일",
          start_hour: "00:00",
          end_hour: "23:00",
          disabled: false,
        },
        {
          day: "일요일",
          start_hour: "00:00",
          end_hour: "23:00",
          disabled: false,
        },
      ],
      constants,
    };
  },
  methods: {
    submitTrainer() {
      const Token = "Bearer " + this.userToken;
      this.submitData["schedule"] = this.schedule;
      axios
        .post(`${constants.API_URL}rest-auth/user/`, this.submitData, {
          headers: {
            Authorization: Token,
          },
        })
        .then(() => {
          this.SET_TYPETOKEN("trainer");
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    ...mapMutations(["SET_TYPETOKEN"]),
  },
  computed: {
    ...mapState(["userToken"]),
  },
};
</script>

<style></style>
