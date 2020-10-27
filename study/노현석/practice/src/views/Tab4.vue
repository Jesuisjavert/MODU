<template>
  <ion-page>
    <ion-header>
      <!-- <ion-toolbar>
        <ion-title>Tab 4</ion-title>
      </ion-toolbar> -->
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 4</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <Mypage name="Mypage" />
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Mypage from '@/components/Mypage.vue';

export default  {
  name: 'Tab4',
  components: { Mypage, IonHeader, IonToolbar, IonTitle, IonContent, IonPage }
}
</script>