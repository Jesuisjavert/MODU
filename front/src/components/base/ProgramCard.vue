<template>
  <v-container>
    <v-row justify="space-around" class="mx-4">
      <v-card width="400">
        <v-img
          height="200px"
          :src="this.$attrs.image_url"
        >
          <v-app-bar
            flat
            color="rgba(0, 0, 0, 0)"
          >
            <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

            <v-toolbar-title class="title white--text pl-0">
              {{this.$attrs.title}}
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn
              color="white"
              icon
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </v-app-bar>

          <v-card-title class="white--text mt-8">
            <v-avatar size="56">
              <img
                alt="user"
                :src="this.$attrs.trainer.user.image_url"
              >
            </v-avatar>
            
          </v-card-title>
        </v-img>

        <v-card-text>
          <div class="font-weight-bold ml-8 mb-2">
            {{this.$attrs.trainer.name}}
          </div>

          <v-timeline
            align-top
            dense
          >
            <v-timeline-item
              color="deep-purple lighten-1"
              small
            >
              <div>
                <div class="font-weight-normal">
                  <strong>소개</strong> @{{ this.$attrs._type }}
                </div>
                <div>{{ this.$attrs.content }}</div>
              </div>
            </v-timeline-item>
            
            <v-timeline-item
              color="green"
              small
            >
              <div>
                <div class="font-weight-normal">
                  <strong>프로그램 스케쥴</strong>
                  <span v-if="this.$attrs._type=='온라인'"> @주 {{this.$attrs.programschedule.length}}회</span>
                </div>
                <div v-for="schedule in this.$attrs.programschedule" :key="schedule.id">
                  <strong>{{ schedule.day }}</strong> {{schedule.start_hour.substr(0,5)}} ~ {{schedule.end_hour.substr(0,5)}}
                </div>
                <div v-if="this.$attrs._type=='오프라인'">오프라인 프로그램입니다.</div>
              </div>
            </v-timeline-item>

            <v-timeline-item
              color="red lighten-1"
              small
            >
              <div>
                <div class="font-weight-normal">
                  <strong>가격</strong>
                </div>
                <div v-for="price in this.$attrs.programprice" :key="price.id">
                  <strong>{{ price.title }}</strong> {{price.price | currency}}원
                </div>
              </div>
            </v-timeline-item>
          </v-timeline>
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
    </v-row>
  </v-container>
</template>
<script>
  export default {
    data: () => ({
    }),
    created() {
    },
    methods: {
      go_detail() {
        this.$router.push("/program/" + this.$attrs.id);
      },
    },
    filters: {
      currency: function (value) {
        var num = new Number(value);
        return num.toFixed(0).replace(/(\d)(?=(\d{3})+(?:\.\d+)?$)/g, "$1,")
      }
    },
  }
</script>