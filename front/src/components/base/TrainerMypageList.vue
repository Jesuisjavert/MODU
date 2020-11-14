<template>
    <v-expansion-panels focusable>
        <h1>바보 창완</h1>
        
            <div v-for="(data,idx) in onlineLecturelist">
      <div>
        <img :src="data.image_url" width="20%" alt="" />
        프로그램 명 : {{ data.title }}
        <!-- <button v-if="onlineScheduleCheck(index)" @click="test(index)">
          수업 시작
        </button> -->
        <WebCreateBtn  :data-set="`${data.id}`" v-if="onlineScheduleCheck(idx)">start</WebCreateBtn>
        <br />
        <div style="boarder : solid"></div>
      </div>
    </div>
        <v-expansion-panel
        v-for="(item,i) in items"
        :key="i"
        >
            <v-expansion-panel-header disable-icon-rotate>
                <p class="text-center mb-0">{{ item.title }}</p>
                <template v-slot:actions>
                    <v-icon></v-icon>
                </template>
            </v-expansion-panel-header>
            <v-expansion-panel-content v-if="item.title == '고객관리'">
                <p v-for="client in item.content" :key="client.name">
                    {{ client }}
                </p>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-else>
                {{ item.content }}
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
</template>

<script>
import constants from '@/api/constants.js'
import axios from 'axios'
import { mapState } from 'vuex'
export default {
    name: "TrainerMypage",
    components: {
        WebCreateBtn: () => import('@/components/base/WebCreateBtn'),
    },
    data() {
        return {
            onlineLecturelist : [],
            constants,
            items: [
                {
                    title: '나의 프로그램',
                    content: '줌바와 함께 줌바댄스를',
                },
                {
                    title: '고객관리',
                    content: [
                        '이창완',
                        '강동훈',
                        '강병국',
                        '배용균',
                    ]
                },
                {
                    title: '프로그램 추가',
                    content: '프로그램 추가하기'
                },
                {
                    title: '식단관리',
                    content: '식단짜주기',
                },
                {
                    title: '설정',
                    content: '설정리스트',
                }
            ],
        }
    },
    methods : {
    testclick(){
        console.log('눌러졌네요.')
    },
    test(index) {
      
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
        console.log(res,'여기는 반응입니다.')
          const a = res.data.filter((item) => {
            console.log(item,'item입니다.')
            if (item._type == "온라인") {
              return item;
            }
          });
          a.forEach((item)=>{
              this.onlineLecturelist.push(item)
          })
          console.log(this.onlineLecturelist,'-0---')
        })
        .catch((err) => {
          console.log(err);
        });
    },
    },
    computed : {
        ...mapState(['userToken'])
    },
    created(){
        this.get_programs()
    }
}
</script>

<style>

</style>