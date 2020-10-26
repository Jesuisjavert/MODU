<template>
  <ion-page>
    <ion-tabs>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="tab5" href="/tabs/tab5">
        <ion-icon name="body-outline" />
        <ion-label>Tab 5</ion-label>
        </ion-tab-button>
          
        <ion-tab-button tab="tab6" href="/tabs/tab6">
          <ion-icon name="calendar-outline" />
          <ion-label>Tab 6</ion-label>
        </ion-tab-button>
        
        <ion-tab-button tab="tab7" href="/tabs/tab7">
          <ion-icon name="chatbubbles-outline" />
          <ion-label>Tab 7</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="tab8" href="/tabs/tab8">
          <ion-icon name="apps-outline" />
          <ion-label>Tab 8</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script lang="ts">
import { IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage } from '@ionic/vue';

export default {
  name: 'Tabs',
  components: { IonLabel, IonTabs, IonTabBar, IonTabButton, IonIcon, IonPage },
}
</script>