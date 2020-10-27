<template>
  <div>
    <ion-header>
      <ion-toolbar>
        <ion-title> 요기가 제목</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      내용이 요기
    </ion-content>
  </div>
</template>

<script>
import { IonContent, IonHeader, IonTitle, IonToolbar } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Modal',
  props: {
    title: { type: String, default: 'Super Modal' },
  },
  data() {
    return {
      content: 'Content',
    }
  },
  components: { IonContent, IonHeader, IonTitle, IonToolbar }
});
</script>