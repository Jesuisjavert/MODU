<template>
  <v-theme-provider :dark="dark">
    <div>
      <base-img
        :src="require('@/assets/modublack.png')"
        contain
        max-width="128"
        min-height="78"
        width="100%"
      />
      <br>
      <base-title
        size="body-1"
        space="4"
        title="Brand Logo Origin"
        weight="regular"
      />

      <base-body>
        MODU 는 모두의 헬스를 나타내는 심벌입니다. 색의 3원색인 빨강,노랑,파랑이 의미하는 '기본'에 기존의 규칙을 따르지 않는다는 의미의 초록을 추가함으로써, 오프라인 피트니스 시장의 틀을 깨는 서비스를 만들겠다는 의미를 담았습니다.
      </base-body>

      <base-btn
        class="mb-12"
        color="white"
        outlined
        href="/about"
      >
        More Info
      </base-btn>
    </div>
  </v-theme-provider>
</template>

<script>
  export default {
    name: 'BaseInfo',

    props: {
      title: String,
      dark: Boolean,
    },

  }
</script>
