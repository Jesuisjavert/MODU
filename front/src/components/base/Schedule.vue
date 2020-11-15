<template>
    <div class="text-center">
        <v-dialog
        v-model="dialog"
        width="500"
        >
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                color="red lighten-2"
                dark
                v-bind="attrs"
                v-on="on"
                >
                스케줄관리
                </v-btn>
            </template>

            <v-card>
                <v-card-title class="headline grey lighten-2">
                선호하는 일정
                </v-card-title>

                <v-card-text>
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
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="primary"
                    text
                    @click="complete"
                >
                    선택
                </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import EventBus from '@/api/eventbus.js'
export default {
    name: "Schedule",
    methods: {
        complete() {
            // this.$emit(this.schedule)
            // console.log(this.$el.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode)
            EventBus.$emit('schedule',this.schedule)
            this.dialog = false
        }
    },
    data () {
        return {
            dialog: false,
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
        }
    },
}
</script>

<style>

</style>