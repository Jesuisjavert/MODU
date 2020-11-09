<template>
  <v-container
    id="about us"
    class="pa-0"
    fluid
    tag="section"
  >
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
        <v-img
          src="@/assets/logo.png"
        />
      </v-col>

      <v-col
        class="d-block d-md-flex align-center grey lighten-3 pa-6"
        cols="12"
        md="6"
      >
        <v-responsive
          class="mx-auto px-3 px-md-12"
          max-width="750"
        >
          <h1
            class="mb-6"
            :class="$vuetify.breakpoint.mdAndUp ? 'display-1' : 'display-1'"
          >
            Hi, We're Health for Everyone<br>
          </h1>

          <p>
           모두의 헬스는 온/오프라인 헬스 트레이너–개인PT회원 관리 및 
           <br>온라인 홈트레이닝 화상대면 관리 플랫폼 서비스입니다.
          </p>

          
        </v-responsive>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
  export default {
    name: 'Aboutus',
    components: {
    }
  }
</script>


