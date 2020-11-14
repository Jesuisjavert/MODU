<template>
  <div class="programs">
    <div class="hero">
      <p class="my-program">내 프로그램</p>
    </div>
    <div class="container my-4">

      <!--Carousel Wrapper-->
      <div id="multi-item-example" class="carousel slide carousel-multi-item" data-ride="carousel">

        <!--Controls-->
        <div class="controls-top">
          <div class="control-btn">
            <a class="btn-floating" href="#multi-item-example" data-slide="prev"><i class="fa fa-chevron-left"></i></a>
          </div>
          <router-link :to="{ name: 'ProgramCreate' }">새 프로그램 등록</router-link>
          <div class="control-btn">
            <a class="btn-floating" href="#multi-item-example" data-slide="next"><i class="fa fa-chevron-right"></i></a>
          </div>
        </div>
        <!--/.Controls-->

        <!--Indicators-->
        <ol class="carousel-indicators">
          <li data-target="#multi-item-example" data-slide-to="0" class="active"></li>
          <li data-target="#multi-item-example" data-slide-to="1"></li>
          <li data-target="#multi-item-example" data-slide-to="2"></li>
        </ol>
        <!--/.Indicators-->

        <!--Slides-->
        <div class="carousel-inner" role="listbox">

          <!--First slide-->
          <div class="carousel-item active">
            <div class="row">
              <div class="col-md-4"
              v-for="program in programs"
              :key="program.id">
                <div class="card mb-2">
                  <img class="card-img-top" :src="program.image_url"
                    alt="Card image cap">
                  <div class="card-body">
                    <h4 class="card-title">{{ program.title }}</h4>
                    <p class="card-text">{{ program.content }}</p>
                    <a class="btn btn-primary" @click="detail(program.id)">자세히 보기</a>
                  </div>
                </div>
              </div>

              <div class="col-md-4 clearfix d-none d-md-block">
                <div class="card mb-2">
                  <img class="card-img-top" src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(18).jpg"
                    alt="Card image cap">
                  <div class="card-body">
                    <h4 class="card-title">Card title</h4>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                      card's content.</p>
                    <a class="btn btn-primary">자세히 보기</a>
                  </div>
                </div>
              </div>
            </div>

          </div>
          <!--/.First slide-->
        </div>
        <!--/.Slides-->

      </div>
      <!--/.Carousel Wrapper-->


    </div>
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

<style scoped>
.programs {
  height: 70vh;
  width: 100%;
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
  background-image: url("../../assets/images/programs2.jpg");
  background-size: cover;
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;
  opacity: 0.6;
}

.hero p {
  font-size: 48px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 80px;
}

.program {
  display: flex;
  justify-content: center;
  align-items: center;
}

.controls-top {
  display: flex;
  justify-content: space-around;
}

.controls-top > a {
  font-size: 24px;
}

.control-btn {
  width: 40px;
  height: 40px;
  border: 1px solid #007bff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #007bff;
  margin-bottom: 20px;
}

.control-btn a {
  color: #ffffff;
  font-weight: bold;
}

.card-img-top {
  height: 232px;
  border-bottom: 1px solid #dddddd;
}

.card-body {
  height: 206px;
}

.card-text {
  height: 72px;
}
</style>
