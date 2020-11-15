<template>
  <v-btn
    @click="startWeb"
  >
  <slot />
  </v-btn>
</template>

<script>
import { uuid } from 'vue-uuid';
import { mapState } from 'vuex';
import axios from 'axios'
import constants from '@/api/constants.js'

export default {
    name: "WebCreateBtn",
    data() {
        return {
            uuid: '',
            constants
        }
    },
    methods: {
        startWeb() {
            var newUuid = this.$uuid.v4()
            this.uuid = newUuid
             
            let data = {
        program_id: this.$el.dataset.set,
        webRtcroomId: this.uuid,
      };
      const Token = "Bearer " + this.userToken;
      axios
        .post(`${constants.API_URL}trainer/program/online/`, data, {
          headers: {
            Authorization: Token,
          },
        })
        .then((res) => {
            $cookies.set('roomID', res.data.data)
            this.$router.push({ name: 'WebCam' })
        });
        }
    },
    computed :{
        ...mapState(['userToken'])
    }
}
</script>

<style>

</style>