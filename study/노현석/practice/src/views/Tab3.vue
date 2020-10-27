<template>
  <ion-page>
    <ion-header>
      <!-- <ion-toolbar>
        <ion-title>Tab 3</ion-title>
      </ion-toolbar> -->
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 3</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <Chat name="Chat page" />
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Chat from '@/components/Chat.vue';

export default  {
  name: 'Tab3',
  components: { Chat, IonHeader, IonToolbar, IonTitle, IonContent, IonPage }
}
</script>