<template>
  <div class="about">
    <h1>Client</h1>
    <button @click="test">TEST</button>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'
export default {
	name = "Client",
  data(){
    return {
      constants,
    }
  },
  methods: {
    test() {
    }
  }
}
</script>