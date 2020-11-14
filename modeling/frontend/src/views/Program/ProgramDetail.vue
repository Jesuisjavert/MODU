<template>
  <div>
    <div class="title">
      <h3 class="title">{{program.title}}</h3>
    </div>
    <div class="row">
      <div class="col-4">
        <div class="program-explain">
          <img :src=program.image_url>
          <h3>프로그램 설명</h3>
          <div>{{program.content}}</div>
        </div>
        <div class="program-question" v-if="userType == 'client'">
          <button class="btn btn-primary" @click="joinChatNumber()">문의하기</button>
        </div>
      </div>
      <div class="col-6">
        <div class="price-explains">
          <h3>가격</h3>
          <div v-for="price in program.programprice" :key="price.id">
            <div class="price-explain">
              <p>이용권 이름 : {{price.title}}</p>
              <p>온라인 횟수 : {{price.online_count}}회</p>
              <p>오프라인 횟수 : {{price.offline_count}}회</p>
              <p>가격 : {{price.price}}원</p>
            </div>
          </div>
        </div>
        <div class="select-box">
          <label for="price">상품 선택</label>
          <select name="price" id="price" v-model="selectPrice">
            <option :value=item.id v-for="item in program.programprice" :key="item.id">{{item.title}}</option>
          </select>
          <button class="btn btn-primary" @click="program_apply()">신청하기</button>
        </div>
        <h3>댓글 작성</h3>
        <div class="comment-box">
          <div class="comment-create">
            <input v-model="submitData.rate" type="number" max='5' min='0' name="rate">
            <textarea name="content" v-model="submitData.content"></textarea>
          </div>
          <button class="btn btn-primary" @click="comment_submit">작성</button>
        </div>
        <div class="comments">
          <div class="comment" v-for="comment in comments" :key="comment.id">
            <div>
              <img :src="comment.client.user.image_url" alt="">
            </div>
            <div>
              <div class="comment-top">
                <div class="comment-left">
                  <span>{{comment.client.user.username}}</span>
                  <span>{{comment.rate}}점</span>
                </div>
                <div class="comment-right">
                  <span class="gara">수정</span>
                  <span class="gara">삭제</span>
                </div>
              </div>
              <div class="comment-bottom">{{comment.content}}</div>
            </div>
          </div>
        </div>

      </div>
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

<style scoped>
.title {
  margin: 4vh 0px;
  font-size: 48px;
}
.row {
  display: flex;
  justify-content: center;
}

.col-4 {
  margin-left: 10%;
}

.program-explain {
  border: solid 1px #dddddd;
  border-radius: 4px;
  height: 60vh;
  padding: 0px;
}

.program-explain img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-bottom: 1px solid #dddddd;
}

.program-explain h3 {
  margin-top: 10px;
}

.program-explain div {
  font-size: 18px;
  padding: 8px 12px;
  text-align: start;
}

.program-question {
  margin-top: 10px;
}

.price-explains{
  margin: auto;
  width: 75%;
  border-bottom: solid 2px #dddddd;
}

.price-explain {
  display: flex;
  justify-content: center;
}

.price-explain p {
  margin-right: 10px;
}

.select-box {
  margin: 24px;
}

.select-box label {
  font-size: 18px;
  margin-right: 12px;
}

.select-box select {
  font-size: 18px;
  margin-right: 12px;
  padding-left: 4px;
}

.btn-primary {
  padding: 4px 8px;
}

.comment-box {
  display: flex;
  justify-content: center;
}

.comment-create {
  display: flex;
  flex-direction: column;
  width: 25vw;
  margin-right: 10px;
}

.comment-create input {
  width: 50px;
  font-size: 14px;
  margin-bottom: 4px;
}

.comment-create textarea {
  resize: none;
  height: 60px;
}

.comment-box button {
  margin-top: 30px;
  height: 60px;
}

.comments {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.comment {
  width: 28.5vw;
}

.comment img {
  height: 15px;
  width: 15px;
}

.comment-top {
  display: flex;
}

.comment-left {
  display: flex;
  flex: 6;
  justify-content: flex-start;
}

.comment-right {
  display: flex;
  flex: 6;
  justify-content: flex-end;
  font-size: 13px;
  color: #aaaaaa;
}

.gara {
  cursor: pointer;
}

.comment span {
  margin-right: 6px;
}

.comment-bottom {
  border: 1px solid #dddddd;
  border-radius: 4px;
  min-height: 40px;
  text-align: start;
  padding: 2px 6px;
}
</style>
