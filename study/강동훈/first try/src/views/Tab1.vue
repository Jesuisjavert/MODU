<template>
  <ion-page>
    <ion-header>  
        <ion-toolbar>
          <ion-title>Tab 2</ion-title>
        </ion-toolbar>
    </ion-header>  
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 1</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-button @click="openModal">모달 모달</ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonButton, IonContent, IonPage, modalController, IonHeader, IonToolbar, IonTitle} from '@ionic/vue';
import Modal from '@/components/Modal.vue'

export default {
  name: 'Tab1',
  components: { IonButton, IonContent, IonPage, IonHeader, IonToolbar,IonTitle },
  methods: {
    async openModal() {
      const modal = await modalController
        .create({
          component: Modal,
          cssClass: 'my-custom-class',
          componentProps: {
            data: {
              content: 'New Content',
            },
            propsData: {
              title: 'New title',
            },
          },
        })
      return modal.present();
    },
  },
}
</script>