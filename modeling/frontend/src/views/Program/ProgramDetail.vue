<template>
  <div>
    <div>프로그램 디테일</div>
    <img :src="program.image_url" height="300px" />

    <hr />

    <div>
      <label for="price">상품 선택</label>
      <select name="price" id="price" v-model="selectPrice">
        <option
          :value="item.id"
          v-for="item in program.programprice"
          :key="item.id"
          >{{ item.title }}</option
        >
      </select>

      <button @click="program_apply()">신청하기</button>
    </div>

    <h3>{{ program.title }}</h3>

    <hr />

    <div>
      <h3>가격</h3>
      <div v-for="price in program.programprice" :key="price.id">
        <p>{{ price }}</p>
      </div>
    </div>

    <hr />

    <div>
      <h3>신청한 유저들</h3>
      <div v-for="client in clients" :key="client.id">
        <p>{{ client }}</p>
      </div>
    </div>

    <hr />

    <div>
      <h3>댓글 작성</h3>
      <label for="rate"></label>
      <input
        v-model="submitData.rate"
        type="number"
        max="5"
        min="0"
        name="rate"
      />
      <label for="content"></label>
      <textarea
        name="content"
        cols="30"
        rows="10"
        v-model="submitData.content"
      ></textarea>
      <button @click="comment_submit">제출</button>
    </div>

    <hr />

    <div>
      <h3>프로그램 댓글</h3>
      <div v-for="comment in comments" :key="comment.id">
        <p>{{ comment }}</p>
      </div>
    </div>

    <div v-if="userType == 'client'">
      문의하기 버튼이 있는 곳이다.
      <button @click="joinChatNumber()">문의하기</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
import constants from "@/api/constants";

export default {
  name: "ProgramDetail",

  data() {
    return {
      constants,
      program: {
        image: null,
        title: null,
        content: null,
      },
      clients: null,
      comments: null,
      submitData: {
        content: null,
        rate: null,
      },
      selectPrice: null,
    };
  },

  created() {
    this.get_program();
    this.get_client();
    this.get_comment();
  },

  methods: {
    joinChatNumber() {
      const data = {
        program_id: this.program.id,
      };
      const Token = "Bearer " + this.userToken;
      axios
        .post(`${constants.API_URL}chat/`, data, {
          headers: {
            Authorization: Token,
          },
        })
        .then((res) => {
          console.log(res.data);
        });
    },
    get_program() {
      const pk = this.$route.params.pk;
      axios
        .get(`${this.constants.API_URL}program/` + pk)
        .then((res) => {
          this.program = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_client() {
      const pk = this.$route.params.pk;
      axios
        .get(`${this.constants.API_URL}program/` + pk + "/user/")
        .then((res) => {
          this.clients = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_comment() {
      const pk = this.$route.params.pk;
      axios
        .get(`${this.constants.API_URL}program/` + pk + "/comment/")
        .then((res) => {
          this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    comment_submit() {
      const pk = this.$route.params.pk;
      const Token = "Bearer " + this.userToken;
      axios
        .post(
          `${this.constants.API_URL}program/` + pk + "/comment/",
          this.submitData,
          {
            headers: {
              Authorization: Token,
            },
          }
        )
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    program_apply() {
      console.log(this.selectPrice);
      console.log(this.program);
      this.$router.push({
        name: "ProgramApply",
        query: { program: this.program.id, price: this.selectPrice },
      });
    },
  },

  computed: {
    ...mapState(["userToken", "userType"]),
  },
};
</script>

<style></style>
