<template>
  <v-container>
    <v-row class="justify-space-around">
        <v-col cols="2">
            <ClientManage/>
        </v-col>
        <v-col cols="9">
            <Calendar/>
        </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ClientManage from '@/components/base/ClientManage.vue'
import Calendar from '@/components/base/Calendar.vue'

export default {
    components: {
        ClientManage,
        Calendar,
    }
}
</script>

<style>

</style>