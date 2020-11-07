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
          height="calc(100vh - 96px - 156px)"
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
            Hello.<br>
          </h1>

          <p>
           모두의 헬스
          </p>

          <div class="signature">
            Health for everyone
          </div>
        </v-responsive>
      </v-col>
    </v-row>

  <cam-slider />

  </v-container>
</template>

<script>
  export default {
    name: 'Aboutus',
    components: {
      CamSlider: () => import('@/components/base/CamSlider'),
    }
  }
</script>

<style lang="sass">
  .signature
    font-family: 'Cedarville Cursive', cursive !important
    font-size: 2rem
    font-style: italic
</style>
