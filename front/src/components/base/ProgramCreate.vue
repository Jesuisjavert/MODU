<template>
  <div class="program">
    <div class="hero">
      <p>새 프로그램</p>
    </div>
    <br />
    <div class="row">
      <div class="col-6 program-box">
        <div class="program-contents program-method">
          <span>수업 방식</span>
          <label class="box-radio-input" for="two"
            ><input
              type="radio"
              id="two"
              value="온라인"
              checked="checked"
              v-model="inputdata._type"
            /><span>온라인</span></label
          >
          <label class="box-radio-input" for="one"
            ><input
              type="radio"
              id="one"
              value="오프라인"
              v-model="inputdata._type"
            /><span>오프라인</span></label
          >
        </div>
        <div class="program-contents program-name">
          <span>프로그램 명</span>
          <input type="text" v-model="inputdata.title" placeholder="이름을 등록하세요" name="title">
        </div>
        <div class="program-contents program-tag">
          <span>태그 추가하기</span>
          <input
            @input="autocomplete"
            placeholder="태그를 등록하세요"
            type="text"
          />
        </div>
        <div class="program-contents tag-insert">
          <div class="tag-box">
            <div v-for="(tag, index) in autocompletelist" :key="index">
              <li @click="appendTag(tag)">
                <span class="tag tag-plus"
                  >{{ tag }} <i class="fas fa-plus"></i
                ></span>
              </li>
            </div>
          </div>
        </div>
        <div class="program-contents">
          <span>태그</span>
          <div class="add-tag">
            <div class="tag-list">
              <div v-for="(tag, index) in inputdata.tags" :key="index">
                <li>
                  <span class="tag"
                    >{{ tag }}
                    <i class="fas fa-minus" @click="deleteTag(index)"></i
                  ></span>
                </li>
              </div>
            </div>
          </div>
        </div>
        <div class="program-contents program-explain">
          <span>설명</span>
          <textarea
            type="text"
            v-model="inputdata.content"
            name="content"
          ></textarea>
        </div>
        <div class="program-contents program-img">
          <span>이미지</span>
          <input type="file" @change="uploadimg" name="image" />
        </div>
      </div>
      <div class="col-5 program-setting">
        <h3>프로그램 시간 및 가격 설정</h3>
        <div v-if="inputdata._type == '온라인'">
          <h4 class="day-select">시간 선택</h4>
          <div class="program-online">
            <div class="program-days" v-for="(day, index) in schedule" :key="index">
              <div class="program-day">
                <div class="day" v-if="!day.disabled">
                  <div>{{ day.day }}</div>
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
                <div class="day" v-else>
                  <div class="holiday">{{ day.day }}</div>
                </div>
                <div class="">
                  <label :for="'c' + index">휴무일</label>
                  <input
                    v-model="day.disabled"
                    type="checkbox"
                    :name="'c' + index"
                    id=""
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <h4>가격 설정</h4>
        <div class="program-cost" v-for=" (data,index) in detaildata" :key="index">
          이름 : <input type="text" placeholder="ex) PT 1회 이용권" required v-model="data.title"> 
          가격 : <input type="number" required v-model="data.price"> 
          횟수 : <input type="number" required v-model="data.online_count"> 
          <button @click="deletedata(index)"><i class="fas fa-minus"></i></button>
        </div>
        <div class="cost-explain">
          <span>항목을 필수적으로 입력해야 합니다.</span>
        </div>
        <button @click="appenddetail">추가</button>
      </div>
    </div>
    <v-col cols="4" offset="4" class="d-flex justify-center">
      <!-- <button class="submit-btn justify-content-center" @click="createProgram()">제출</button> -->
      <Btn @click="createProgram()">제출</Btn>
    </v-col>
  </div>
</template>

<script>
import axios from "axios";
import constants from "@/api/constants.js";
import { mapState } from "vuex";
export default {
  name: "ProgramCreate",
  components: {
    Btn: () => import('@/components/base/Btn'),
  },
  data() {
    return {
      inputdata: {
        _type: "온라인",
        title: "",
        content: "",
        thumb_img: [],
        tags: [],
      },
      detaildata: [
        {
          price: 0,
          title: "",
          online_count: 0,
          offline_count: 0,
        },
      ],
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
      autocompletelist: [],
    };
  },
  watch: {
    "inputdata._type": function(newVal, oldVal) {
      if (oldVal == "온라인") {
        this.detaildata = this.detaildata.map((item) => {
          item.online_count = 0;
          return item;
        });
      } else {
        this.detaildata = this.detaildata.map((item) => {
          item.offline_count = 0;
          return item;
        });
      }
    },
  },
  methods: {
    uploadimg(event) {
      console.log(event);
      const file = event.target.files[0];
      this.inputdata.thumb_img = [];
      this.inputdata.thumb_img.push(file);
    },
    schedulesubmit(id) {
      const pushdata = {
        schedule: this.schedule,
      };
      axios
        .post(`${constants.API_URL}program/${id}/schedule/`, pushdata)
        .then((res) => {
          console.log(res);
        });
    },
    appenddetail() {
      this.detaildata.push({
        price: 0,
        title: "",
        online_count: 0,
        offline_count: 0,
      });
    },
    deletedata(index) {
      this.detaildata.splice(index, 1);
    },
    createProgram() {
      let formData = new FormData();
      let tags = this.inputdata.tags.join();
      let Token = "Bearer " + this.userToken;
      formData.append("title", this.inputdata.title);
      formData.append("content", this.inputdata.content);
      formData.append("_type", this.inputdata._type);
      formData.append("thumb_img", this.inputdata.thumb_img[0]);
      formData.append("tags", tags);
      const data = {
        program_detail: this.detaildata,
      };
      this.setFormData(formData, data);
      axios
        .post(`${constants.API_URL}program/`, formData, {
          headers: {
            Authorization: Token,
          },
        })
        .then((res) => {
          console.log(res);
          if (this.inputdata._type == "온라인") {
            this.schedulesubmit(res.data.id);
          }
          this.$router.push({ name: 'Mypage' })
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    setFormData(formData, data, parentKey) {
      if (!(formData instanceof FormData)) return;
      if (!(data instanceof Object)) return;
      Object.keys(data).forEach((key) => {
        const val = data[key];
        if (parentKey) key = `${parentKey}[${key}]`;
        if (val instanceof Object && !Array.isArray(val)) {
          return this.setFormData(formData, val, key);
        }
        if (Array.isArray(val)) {
          val.forEach((v, idx) => {
            if (v instanceof Object) {
              this.setFormData(formData, v, `${key}[${idx}]`);
            } else {
              formData.append(`${key}[${idx}]`, v);
            }
          });
        } else {
          formData.append(key, val);
        }
      });
    },
    autocomplete(event) {
      this.autocompletelist = [];
      const inputValue = event.target.value.trim();
      if (inputValue.length > 0) {
        this.constants.tags.forEach((item) => {
          if (item.includes(inputValue)) {
            this.autocompletelist.push(item);
          }
        });
      }
    },
    appendTag(tag) {
      console.log(this.inputdata.tags.indexOf(tag));
      if (this.inputdata.tags.indexOf(tag) === -1) {
        this.inputdata.tags.push(tag);
      }
    },
    deleteTag(index) {
      this.inputdata.tags.splice(index, 1);
    },
  },
  computed: {
    ...mapState(["userToken"]),
  },
};
</script>

<style scoped>
.program {
  width: 100vw;
}

.row {
  margin: 0px;
}

.hero {
  display: flex;
  position : relative;
  height: 330px;
  z-index: 1;
  justify-content: center;
  align-items: center;
}


.hero::after {
  content: "";
  width: 100%;
  height: 100%;
  background-image: url("../../assets/images/programcreate2.jpg");
  background-size: cover;
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;
  opacity: 0.7;
}

.hero p {
  font-size: 48px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 80px;
}

.box-radio-input {
  margin: 0px 10px 0px 0px;
}

.box-radio-input input[type="radio"] {
  display: none;
}

.box-radio-input input[type="radio"] + span {
  display: inline-block;
  border-radius: 4px;
  background: none;
  border: 1px solid #dfdfdf;
  padding: 0px 10px;
  text-align: center;
  height: 35px;
  line-height: 33px;
  font-weight: 500;
  cursor: pointer;
}

.box-radio-input input[type="radio"]:checked + span {
  border: 1px solid #1f85de;
  border-radius: 4px;
  background: #1f85de;
  color: #fff;
}

.program-box {
  padding-left: 15%;
}

.program-contents {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 20px;
  overflow: hidden;
}

.program-contents > span {
  font-size: 18px;
  width: 120px;
  margin-right: 25px;
  text-align: end;
}

.program-contents > input {
  width: 400px;
  border: none;
  border-bottom: 1px solid #1f85de;
}

.tag-insert {
  height: 50px;
  padding-left: 147px;
  display: flex;
  list-style: none;
}

.tag-box {
  display: flex;
}

.tag-box li {
  cursor: pointer;
}

.tag-insert li {
  margin-right: 12px;
}

.tag {
  border: 2px solid #dfdfdf;
  font-size: 14px;
  border-radius: 8px;
  color: #000000;
  background-color: #fff;
  text-align: center;
  padding: 6px 8px;
}

.tag i {
  margin-left: 4px;
}

.tag-plus:hover {
  border: 2px solid #1f85de;
  background-color: #1f85de;
  color: #ffffff;
  transition: ease-in-out 0.2s;
}

.add-tag {
  width: 400px;
  border-bottom: 1px solid #1f85de;
}

.tag-list {
  height: 40px;
  display: flex;
  list-style: none;
  align-items: center;
}

.tag-list li {
  margin-right: 12px;
}

.tag-list span i {
  cursor: pointer;
}

.tag-list span i:hover {
  transition: ease-in-out 0.2s;
  color: #e61717;
}

.program-explain textarea {
  border-color: #1f85de;
  width: 400px;
  height: 100px;
  resize: none;
}

.program-setting {
  border: 1px solid #1f85de;
  padding: 10px 0px;
}

.program-online {
  display: flex;
  justify-content: space-around;
}

.program-online .day-select {
  display: inline;
}

.program-days {
  display: flex;
}

.program-day {
  width: 5.5vw;
  display: flex;
  flex-direction: column;
}

.day {
  height: 110px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.day .holiday {
  color: #e61717;
}

.day input {
  font-size: 13px;
}


.program-cost {
  margin: 12px 0px;
}

.program-cost input {
  width: 180px;
  margin-right: 20px;
}

.cost-explain {
  font-size: 13px;
  margin-left: 20px;
  text-align: start;
  color: #ff6262;
}

.submit-btn {
  font-size: 18px;
  margin-top: 10px;
  padding: 3px 10px 1px;
  border-radius: 8px;
  border: solid #dfdfdf;
  background-color: #ffffff;
  transition: ease-in-out 0.2s;
}

.submit-btn:hover {
  border-color: #5ed6a4;
  background-color: #54dba3;
  color: #ffffff;
  font-weight: 600;
}
</style>
