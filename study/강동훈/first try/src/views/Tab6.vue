<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Tab 6</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 6</ion-title>
        </ion-toolbar>
      </ion-header>
      
  <FullCalendar :options="calendarOptions" />
  
   </ion-content>
  </ion-page>
</template>

<script>
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

export default  {
  name: 'Tab6',
  components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, FullCalendar},
  data() {
    return {
      calendarOptions: {
        plugins: [ dayGridPlugin, interactionPlugin ],
        initialView: 'dayGridMonth'
      }
    }
  }
}
</script>