<template>
  <div>
    <v-fade-transition mode="out-in">
      <router-view />
    </v-fade-transition>
    <FBA v-if="this.$store.state.userType === 'client'"></FBA>
  </div>
</template>

<script>
  export default {
    name: 'HealthforEveryone',
    components: {
      FBA: () => import('@/components/base/FBA'),
    }
  }
</script>
