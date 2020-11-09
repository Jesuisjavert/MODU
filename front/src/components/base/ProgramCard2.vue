<template>
  <v-container>
    <v-row justify="space-around" class="mx-4">
      <v-card width="400">
        <v-img
          height="200px"
          :src="require('@/assets/trainer8.jpg')"
        >
          <v-app-bar
            flat
            color="rgba(0, 0, 0, 0)"
          >
            <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

            <v-toolbar-title class="title white--text pl-0">
              Personal Training
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
                :src="require('@/assets/modu16.jpg')"
              >
            </v-avatar>
            <p class="ml-3">
              강관장
            </p>
          </v-card-title>
        </v-img>

        <v-card-text>
          <div class="font-weight-bold ml-8 mb-2">
            Today
          </div>

          <v-timeline
            align-top
            dense
          >
            <v-timeline-item
              v-for="message in messages"
              :key="message.time"
              :color="message.color"
              small
            >
              <div>
                <div class="font-weight-normal">
                  <strong>{{ message.from }}</strong> @{{ message.time }}
                </div>
                <div>{{ message.message }}</div>
              </div>
            </v-timeline-item>
          </v-timeline>
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>
<script>
  export default {
    data: () => ({
      messages: [
        {
          from: 'Yoga',
          message: `주 3회 온라인 PT 실시`,
          time: '10:50am',
          color: 'deep-purple lighten-1',
        },
        {
          from: 'Personal Training',
          message: '주 2회 오프라인 PT 실시',
          time: '19:00pm',
          color: 'green',
        },
        {
          from: '식단관리',
          message: '날씬한 몸매를 위한 최선의 선택',
          time: '고구마와 닭가슴살만 먹는 단순한 식단은 가라!',
          color: 'red lighten-1',
        },
      ],
    }),
  }
</script>