<template>
 <ion-page>
    <ion-content fullscreen class="ion-padding" scroll-y="false">
      <ion-slides>

        <ion-slide>
          <div class="slide">
            <img src="@/assets/logo3.png"/>
            <h2>Welcome</h2>
            <p>모두의 헬스에 오신 것을 환영합니다</p>
          </div>
        </ion-slide>

        <ion-slide>
          <img src="@/assets/035-gym.png"/>
          <h2>모두의 헬스에선?</h2>
          <p><b> 내게 꼭 맞는 Personal Trainer</b> 를 만나 볼까요?</p>
        </ion-slide>

        <ion-slide>
          <img src="@/assets/013-calendar.png"/>
          <h2>Trainer와의 1:1 연결</h2>
          <p><b>모두의 헬스 어플로</b> 운동루틴과 식단관리 도움을 받을 수 있습니다.</p>
        </ion-slide>

        <ion-slide>
          <img src="@/assets/049-muscle.png"/>
          <h2>오늘 더 건강히</h2>
          <p> 모두의 헬스, 당신의 건강한 삶을 위해</p>
            <a href="/tabs/tab1"> Trainer</a>
            <a href="/tabs/tab5"> Trainee</a>
        </ion-slide>

      </ion-slides>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonSlide, IonPage, IonContent, IonSlides } from '@ionic/vue';

export default  {
  name: 'Tab8',
  components: { IonContent, IonPage, IonSlide, IonSlides }
}
</script>

<style>
  ion-slides {
    height: 100%;
  }

  .swiper-slide {
    display: block;
  }

  .swiper-slide h2 {
    margin-top: 2.8rem;
  }

  .swiper-slide img {
    max-height: 50%;
    max-width: 80%;
    margin: 60px 0 40px;
    pointer-events: none;
  }

  b {
    font-weight: 500;
  }

  p {
    padding: 0 40px;
    font-size: 14px;
    line-height: 1.5;
    color: var(--ion-color-step-600, #60646b);
  }

  p b {
    color: var(--ion-text-color, #000000);
  }
  </style>