<template>
  <ion-page>
    <ion-header>
      <!-- <ion-toolbar>
        <ion-title>Tab 2</ion-title>
      </ion-toolbar> -->
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 2</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <Calendar name="Tab 2 page" />
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Calendar from '@/components/Calendar.vue';

export default  {
  name: 'Tab2',
  components: { Calendar, IonHeader, IonToolbar, IonTitle, IonContent, IonPage }
}
</script>