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
      <ion-list>
          <ion-item class="ion-text-center" @click="() => router.push('/')">메뉴1</ion-item>
          <h4 class="ion-text-center" @click="() => router.push('/')">메뉴1</h4>
          <ion-item @click="() => router.push('/')">메뉴1</ion-item>
          <ion-item @click="() => router.push('/')">메뉴1</ion-item>
          <ion-item @click="() => router.push('/')">메뉴1</ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, alertController, IonList, IonItem } from '@ionic/vue';
import Alert from '@/components/Alert.vue';
import { useRouter } from 'vue-router';

export default  {
  name: 'Tab8',
  components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonList, IonItem },
  methods: {
    async openAlert() {
      const alert = await alertController
        .create({
          component: Alert,
          cssClass: 'my-custom-class',
          header: 'Alert',
          subHeader: 'Subtitle',
          message: '메세지 바꿔줄거',
          buttons: ['OK', 'Cancel'],
        });
      return alert.present();
    },
  },
  setup() {
    const router = useRouter();
      return { router };
  }
}
</script>