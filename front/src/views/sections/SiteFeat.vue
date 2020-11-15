<template>
  <base-section id="Site Feat" space="36">
    <base-section-heading
      color="grey lighten-2"
      icon="mdi-bike"
      title="모두의 헬스 사용방법"
    />
    <v-container>
      <v-row>
        <v-col
          v-for="card in cards"
          :key="card.title"
          cols="12"
          md="4"
        >
          <base-info-card v-bind="card" />
        </v-col>
      </v-row>
    </v-container>
  </base-section>
</template>

<script>
  export default {
    name: 'SiteFeat',

    data: () => ({
      cards: [
        {
          title: 'Trainer / Client 로 가입',
          text: '원하시는 서비스를 선택하세요. 회원가입과 로그인은 카카오 로그인으로 간편하게',
          callout: '01',
        },
        {
          title: '원하시는 프로그램을 선택하세요',
          text: '원하는 프로그램을 선택하고, Trainer와 Contact 하세요. 일정을 조율하시고, 고민을 상담해보세요!',
          callout: '02',
        },
        {
          title: 'Kakao Pay를 통해 PT를 결제하세요',
          text: '카카오Pay를 통해 간단히 결제하시고, 모두의 헬스가 제공하는 모든 기능을 즐겨보세요.',
          callout: '03',
        },
      ],
    }),
  }
</script>
