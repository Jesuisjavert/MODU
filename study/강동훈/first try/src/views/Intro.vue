<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Intro</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Intro</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <ExploreContainer name="Intro page" />
      <a href="/tabs/tab1"> Trainer</a>
      <a href="/tabs/tab5"> Trainee</a>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import ExploreContainer from '@/components/ExploreContainer.vue';

export default  {
  name: 'Tab8',
  components: { ExploreContainer, IonHeader, IonToolbar, IonTitle, IonContent, IonPage }
}
</script>