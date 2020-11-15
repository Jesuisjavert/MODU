<template>
  <v-container
    id="trainer detail"
    class="pa-0"
    fluid
    tag="section"
  > 
    <v-row>
      <v-col
        cols="6"
        align="right"
      >
        <v-avatar size="150">
          <img
            alt="user"
            :src="this.trainer.user.image_url"
          >
        </v-avatar>
      </v-col>
      <v-col
        cols="6"
        align="left"
      >
        <h1>{{trainer.name}} </h1>
        <p>"{{trainer.content}}"</p>

        <p class="grey--text text--lighten-1 mb-1">전문분야</p>
        <v-chip
          label
          v-for="tag in this.trainer.tags" :key="tag.id"
          class="mr-2"
        >{{tag.name}}</v-chip>
      </v-col>
    </v-row>
    
    <ItemColumn>
      <v-col
        cols="8"
      >
        <h3>예약하기</h3>
        <v-row>
          <v-col
            cols="6"
          >
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="date"
                  label="예약 일정 선택"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="date"
                @input="menu2 = false"
              ></v-date-picker>
            </v-menu>
          </v-col>
          <v-col
            cols="6"
          >
            <v-select
              v-model="program_id"
              label="프로그램 선택"
              :items="programs"
              item-text="title"
              item-value="id"
            ></v-select>
          </v-col>
        </v-row>

        <v-chip-group
          column
        >
          <div v-for="(scheudle, index) in scheudles" :key="index" v-if="index>=8">
            <!-- {{scheudle}} -->
            <v-chip @click="set_time(scheudle.value)" v-if="scheudle.status" color="green">{{scheudle.time}}</v-chip>
            <v-chip v-else :ripple="false" :disabled="false">{{scheudle.time}}</v-chip>
          </div>
        </v-chip-group>


        <v-btn
          class="d-block mb-10"
          depressed
          color="primary"
          @click="reservation"
        >
          예약
        </v-btn>

        <h3 class="d-inline">트레이닝 후기</h3>
        <v-row
          align="center"
          class="mx-0 d-inline"
        >
          <v-rating
            :value="this.trainer.comment.rate"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
            class="d-inline"
          ></v-rating>

          <div class="grey--text ml-4 d-inline">
            {{Math.round(this.trainer.comment.rate*100)/100}} ({{this.trainer.comment.count}})
          </div>
        </v-row>

        <template v-for="(comment, i) in comments">
          <blog-post-comment
            :key="i"
            :comment="comment"
          />
        </template>


        <h3 class="mt-10">프로그램</h3>
        <VueSlickCarousel v-if="programs!=null">
          <div v-for="program in programs" :key="program.id"><ProgramCard v-bind="program"/></div>
        </VueSlickCarousel>
      </v-col>
    </ItemColumn>
  </v-container>
</template>

<script>
  import axios from "axios";
  import { mapState } from "vuex";
  import constants from "@/api/constants";
  import VueSlickCarousel from 'vue-slick-carousel'
  import ProgramCard from '@/components/base/ProgramCard'

  export default {
    name: 'TrainerDetail',
    components: {
      VueSlickCarousel,
      ProgramCard,
      ItemRow: () => import('@/components/base/ItemRow'),
      ItemColumn: () => import('@/components/base/ItemColumn'),
      BlogPostComment: () => import('@/components/base/Comment'),
    },
    data(){
      return {
        constants,
        comments: null,
        trainer: {
          
          user: {
            "image_url": null
          },
          comment: {
            "rate": 0
          }
        },
        selection: 1,
        date: null,
        time: null,
        program_id: null,
        scheudles: [],
        programs: null,
        date: new Date().toISOString().substr(0, 10),
        menu2: false,
        holiday: false,
      }
    },
    created() {
      this.get_trainer()
      this.get_comment()
      this.get_programs()
    },
    methods: {
      set_time(time) {
        this.time = time
      },
      get_trainer() {
        const pk = this.$route.params.pk
        axios.get(`${this.constants.API_URL}trainer/${pk}/`)
          .then((res)=>{
            this.trainer = res.data
            this.get_schedule()
          })
          .catch((err)=>{
            console.log(err)
          })
      },
      get_comment() {
        const pk = this.$route.params.pk
        axios.get(`${this.constants.API_URL}trainer/${pk}/comment/`)
          .then((res)=>{
            this.comments = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
      },
      get_programs() {
        const pk = this.$route.params.pk
        axios.get(`${this.constants.API_URL}trainer/${pk}/program/`)
          .then((res)=>{
            this.programs = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
      },
      reservation() {
        let Token = "Bearer " + this.userToken;
        let form = new FormData()
        form.append('date', this.date)
        form.append('time', this.time)
        form.append('program_id', this.program_id)
        const pk = this.$route.params.pk
        axios.post(`${this.constants.API_URL}trainer/${pk}/reservation/`, form, {
          headers: {
            Authorization: Token,
          },
        })
        .then(()=>{
        })
      },
      get_schedule() {
        this.scheudles = []
        let date = new Date(this.date)
        var week = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'];
        var dayOfWeek = week[date.getDay()];
        this.holiday = false

        let nowHour = new Date() < date ? 0 : new Date().getHours()

        // 처음 디폴트 시간표
        for (var i=0; i<23; i++){
          let item = {
            "value": i +":00 ",
            "time": (i +":00 " +(i<12 ? "AM" : "PM")),
            "status": false,
          }
          this.scheudles.push(item)
        }

        // 트레이너 시간표
        for (var i=0, item; item=this.trainer.trainerschedule[i]; i++) {
          if (item.day==dayOfWeek) {
            let start_hour = (item.start_hour.substr(0,2))
            let end_hour = (item.end_hour.substr(0,2))
            for (var j=Number(start_hour); j<Number(end_hour); j++){
              this.scheudles[j].status = true
            }
          }
        }

      },
    },
    computed: {
      ...mapState(["userToken"]),
    },
    watch: {
      date (val) {
        this.get_schedule()
      },
    },
  }
</script>


