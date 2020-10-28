<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Tab 8</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 8</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <ion-button @click="openAlert">알림창</ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, alertController } from '@ionic/vue';
import Alert from '@/components/Alert.vue';

export default  {
  name: 'Tab8',
  components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage },
  methods: {
    async openAlert() {
      const alert = await alertController
        .create({
          component: Alert,
          cssClass: 'my-custom-class',
          header: 'Alert',
          subHeader: 'Subtitle',
          message: 'This is an alert message.',
          buttons: ['OK'],
        });
      return alert.present();
    },
  }
}
</script>