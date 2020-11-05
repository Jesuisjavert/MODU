<template>
  <v-theme-provider :dark="dark">
    <div>
      <base-img
        :src="require('@/assets/logo2.png')"
        contain
        max-width="128"
        min-height="78"
        width="100%"
      />

      <base-title
        size="body-1"
        space="4"
        title="Brand Logo Origin"
        weight="regular"
      />

      <base-body>
        팀명 Lumière는 세계 최초로 영화를 개발한 루미에르 형제에서 이름을 따왔습니다. 루미에르 형제가 영화를 통해 우리 삶을 밝혀주었듯, 이 사이트를 통해 여러분의 영화 인생이 밝혀졌으면 합니다.
      </base-body>

      <base-btn
        class="mb-12"
        color="white"
        outlined
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
