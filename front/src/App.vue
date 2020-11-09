<template>
  <div>
    <v-fade-transition mode="out-in">
      <router-view />
    </v-fade-transition>
    <FBA></FBA>
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
