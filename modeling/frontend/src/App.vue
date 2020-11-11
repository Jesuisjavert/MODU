<template>
  <div id="app">
    <div id="nav">
<<<<<<< Updated upstream
      <Header />
=======
      <Header/>

>>>>>>> Stashed changes
    </div>
    <router-view />
  </div>
</template>
<script>
import Header from "@/components/common/Header.vue";
export default {
  name: "App",
  components: {
    Header,
  },
};
</script>
<style>
body {
  padding: 0px;
  margin: 0px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  justify-content: center;
  
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
