<template>
  <v-btn
    @click="startWeb"
  >
  <slot />
  </v-btn>
</template>

<script>
import { uuid } from 'vue-uuid';

export default {
    name: "WebCreateBtn",
    data() {
        return {
            uuid: '',
        }
    },
    methods: {
        startWeb() {
            var newUuid = this.$uuid.v4()
            this.uuid = newUuid
            this.$router.push({ name: 'WebCam' })
        }
    },
}
</script>

<style>

</style>