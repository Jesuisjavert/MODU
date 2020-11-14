<template>
  <v-card
    :loading="loading"
    class="mx-4 my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      :src="this.$attrs.user.image_url"
    ></v-img>

    <v-card-title>{{this.$attrs.name}}</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="this.$attrs.comment.rate"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ml-4">
          {{this.$attrs.comment.rate}} ({{this.$attrs.comment.count}})
        </div>
      </v-row>

      <div class="my-4 subtitle-1" v-for="tag in this.$attrs.tags" :key="tag.id">
        <p>- {{tag.name}} </p>
      </div>

      <div>{{this.$attrs.content}}</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Tonight's availability</v-card-title>

    <v-row>
      <v-col
        cols="10"
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
    </v-row>

    <v-card-text>
      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
        v-if="holiday"
      >
        <div v-for="scheudle in scheudles" :key="scheudle.id">
          <v-chip>{{scheudle}}</v-chip>
        </div>
      </v-chip-group>
      <div v-else>
        <p>휴무일 입니다.</p>
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="go_detail()"
      >
        상세보기
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
  export default {
    data: () => ({
      loading: false,
      selection: 1,
      holiday: false,
      scheudles: [],
      date: new Date().toISOString().substr(0, 10),
      menu2: false,
    }),
    props: ['trainer'],
    created() {
      this.get_schedule()
    },
    methods: {
      reserve () {
        this.loading = false

        setTimeout(() => (this.loading = false), 2000)
      },
      go_detail() {
        this.$router.push("trainer/" + this.$attrs.id);
      },
      get_schedule() {
        this.scheudles = []
        let date = new Date(this.date)
        var week = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'];
        var dayOfWeek = week[date.getDay()];
        this.holiday = false

        let nowHour = new Date() < date ? 0 : new Date().getHours()

        for (var i=0, item; item=this.$attrs.trainerschedule[i]; i++) {
          if (item.day==dayOfWeek) {
            this.holiday = true
            for (var j=8; j<18 ; j++){
              if (nowHour < j){
                this.scheudles.push(j +":00 " +(j<12 ? "AM" : "PM"))
              }
            }
          }
        }
      },
    },
    watch: {
      date (val) {
        this.get_schedule()
      },
    },
  }
</script>