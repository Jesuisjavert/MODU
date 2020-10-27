<template>
  <ion-app>
    <ion-toolbar color="primary">
      <ion-title class="ion-text-center" color="light">모두의 헬스</ion-title>
    </ion-toolbar>
      <ion-router-outlet />
  </ion-app>
</template>

<script lang="ts">
import { IonApp, IonRouterOutlet } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  components: {
    IonApp,
    IonRouterOutlet
  }
});
</script>