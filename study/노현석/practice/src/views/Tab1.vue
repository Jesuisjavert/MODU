<template>
  <ion-page>
    <ion-header>
      <!-- <ion-toolbar>
        <ion-title>Tab 1</ion-title>
      </ion-toolbar> -->
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 1</ion-title>
        </ion-toolbar>
      </ion-header>
    
      <Home name="Home Page" />
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Home from '@/components/Home.vue';

export default  {
  name: 'Tab1',
  components: { Home, IonHeader, IonToolbar, IonTitle, IonContent, IonPage }
}
</script>