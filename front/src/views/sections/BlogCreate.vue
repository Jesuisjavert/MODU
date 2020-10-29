<template>
  <v-container
    id="BlogCreate"
    class="pa-0"
    fluid
    tag="section"
  >
    <blog-create-form />

  </v-container>
</template>

<script>
  export default {
    name: 'BlogCreate',

    components: {
      BlogCreateForm: () => import('@/components/base/BlogCreateForm'),
    },

    data () {
      return {
      }
    },
  }
</script>
