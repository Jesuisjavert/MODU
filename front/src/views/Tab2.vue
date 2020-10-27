<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>당신의 스케쥴</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 2</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <Card />

    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Card from '@/components/Card.vue';

export default  {
  name: 'Tab2',
  components: { Card, IonHeader, IonToolbar, IonTitle, IonContent, IonPage}
}
</script>