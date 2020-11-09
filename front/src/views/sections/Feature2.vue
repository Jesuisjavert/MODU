<template>
  <base-section id="theme-features">
    <base-section-heading title="Site Features">
      사이트 주요 기능을 소개합니다
    </base-section-heading>

    <v-container>
      <v-row>
        <v-col
          v-for="(feature, i) in features"
          :key="i"
          cols="12"
          md="6"
        >
          <base-avatar-card
            v-bind="feature"
            align="left"
            horizontal
          />
        </v-col>
      </v-row>
    </v-container>
  </base-section>
</template>

<script>
  export default {
    name: 'SectionThemeFeatures',

    data: () => ({
      features: [
        {
          title: 'Write your Comment',
          icon: 'mdi-fountain-pen-tip',
          content: '당신의 감상을 한줄평으로 남겨보세요.',
        },
        {
          title: 'Mobile accesibility',
          icon: 'mdi-cellphone',
          content: '우리 사이트는 모바일로도 들어올 수 있는 반응형 웹입니다. 스마트폰으로도 편하게 접속하세요.',
        },
        {
          color: 'primary',
          dark: true,
          title: 'Let your idea spread',
          icon: 'mdi-pencil-box-outline',
          content: '심도 있는 전문 리뷰를 쓰고, 읽고, 느끼세요!',
        },
        {
          title: 'Responsive Image',
          icon: 'mdi-image-size-select-actual',
          content: '영화의 포스터, 시놉시스, 디테일한 정보를 찾아보세요',
        },
        {
          title: 'Signup',
          icon: 'mdi-ice-pop',
          content: '회원가입을 통해 멤버쉽 혜택을 누려보세요',
        },
        {
          title: '24/7 Support',
          icon: 'mdi-help-circle-outline',
          content: '24시간 일주일 내내 당신의 의견에 귀 기울이겠습니다',
        },
      ],
    }),
  }
</script>
