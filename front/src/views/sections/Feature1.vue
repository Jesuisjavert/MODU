<template>
  <base-section
    id="features"
    class="secondary"
  >
    <v-responsive
      class="mx-auto"
      max-width="1350"
    >
      <v-container fluid>
        <v-row>
          <v-col
            v-for="card in cards"
            :key="card.title"
            cols="12"
            sm="4"
            md="3"
          >
            <base-info-card
              align="center"
              dark
              v-bind="card"
            />
          </v-col>
        </v-row>
      </v-container>
    </v-responsive>
  </base-section>
</template>

<script>
  export default {
    name: 'SectionFeatures',

    data: () => ({
      cards: [
        {
          icon: 'mdi-account-group-outline',
          title: 'Professional Trainer',
          text: '당신에게 꼭 맞는 PT프로그램을 찾아보세요',
        },
        {
          icon: 'mdi-calendar-account-outline',
          title: 'Exercise Routine manage',
          text: '내 트레이너의 일정에 맞춰 관리를 받으세요',
        },
        {
          icon: 'mdi-food-off',
          title: 'Diet management',
          text: '식단관리 캘린더로 간편하게',
        },
        {
          icon: 'mdi-chat-processing-outline',
          title: 'Realtime FaceChat',
          text: '화상채팅으로 실시간 온라인 홈트레이닝',
        },
      ],
    }),
  }
</script>
