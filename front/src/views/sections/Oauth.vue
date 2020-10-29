<template>
  
</template>

<script>
export default {
  name: 'Oauth',
  data() {
    return {
      key: null
    }
  },
  mounted() {
    this.$cookies.set('accessToken', this.$route.query.token)
    this.$router.push('/')
  }
}
</script>

