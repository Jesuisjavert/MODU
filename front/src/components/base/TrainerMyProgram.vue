<template>
    <div v-if="onlineLecturelist.length > 0">
        <div v-for="(data,idx) in onlineLecturelist">
            <div>
            <v-row>
                <v-col cols="5" class="mr-auto">
                    <v-img
                        :src="data.image_url"
                        max-width="100"
                        max-height="100"
                    ></v-img>
                </v-col>
                <v-col cols="7" class="text-start">
                    <p>프로그램 명 : {{ data.title }}</p>
                    <p class="font-weight-black brown--text darken-4--text">{{ data._type }}</p>
                    <WebCreateBtn  :data-set="`${data.id}`" v-if="onlineScheduleCheck(idx)">start</WebCreateBtn>
                </v-col>
            </v-row>
            <!-- <button v-if="onlineScheduleCheck(index)" @click="test(index)">
                수업 시작
            </button> -->
            <br />
            <!-- <div style="boarder : solid"></div> -->
            </div>
        </div>
    </div>
    <div v-else>
        <p>진행중인 프로그램이 없습니다</p>
    </div>
</template>

<script>
import constants from '@/api/constants.js'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
    name: "TrainerMyProgram",
    components: {
        WebCreateBtn: () => import('@/components/base/WebCreateBtn'),
    },
    data() {
        return {
            onlineLecturelist : [],
            constants,
        }
    },
    created(){
        this.get_programs()
    },
    computed : {
        ...mapState(['userToken'])
    },
    methods : {
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
            const a = res.data.filter((item) => {
                if (item._type == "온라인") {
                return item;
                }
            });
            a.forEach((item)=>{
                this.onlineLecturelist.push(item)
            })
            })
            .catch(() => {
            // console.log(err);
            });
        },
    },
}
</script>

<style>

</style>