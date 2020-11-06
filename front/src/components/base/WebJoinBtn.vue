<template>
  <v-btn
    @click="joinWeb"
  >
  <slot />
  </v-btn>
</template>

<script>
import RTCMultiConnection from 'rtcmulticonnection';
require('adapterjs');

export default {
    name: "WebJoinBtn",
    methods: {
        joinWeb() {
            
        },
    },
    data () {
        return {
            joinRoomId: '',
        }
    },
    mounted() {
        
    }
}
</script>

<style>

</style>