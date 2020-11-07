<template>
  <v-btn
    @click="joinWeb"
  >
  <slot />
  </v-btn>
</template>

<script>

export default {
    name: "WebJoinBtn",
    methods: {
        joinWeb() {
          $cookies.set('roomID', this.joinRoomId)
          this.$router.push({ name: 'WebCam' })
        },
    },
    data () {
        return {
            joinRoomId: 'public-room',
        }
    },
    mounted() {
        
    }
}
</script>

<style>

</style>