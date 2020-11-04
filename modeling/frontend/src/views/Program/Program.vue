<template>
  <div>
      <div>내 프로그램 관리 페이지</div>

      <router-link :to="{name : 'ProgramCreate'}">새 프로그램 등록</router-link>
  </div>
</template>

<script>
export default {
    name : 'Program'
}
</script>

<style>

</style>