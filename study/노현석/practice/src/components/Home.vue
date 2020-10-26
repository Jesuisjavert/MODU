<template>
  <div id="container">
    <!-- <strong>{{ name }}</strong> -->
    <ion-grid>
      <ion-row>
        <ion-col size="5" offset="7">
          <ion-row>
            <ion-input size="serach" placeholder="검색"></ion-input>
            <ion-buttons end>
              <button ion-button> 
                <!-- 위 태그 안에 함수 설정 -->
                <ion-icon name="search-outline"></ion-icon>
              </button>
            </ion-buttons>
          </ion-row>
        </ion-col>
      </ion-row>
    </ion-grid>
    <!-- <p>Explore <a target="_blank" rel="noopener noreferrer" href="https://ionicframework.com/docs/components">UI Components</a></p> -->
    <strong>인기 프로그램</strong>
    <!-- 슬라이드 -->
      <ion-slides pager="true" :options="slideOpts">
        <ion-slide>
          <!-- <h1>Slide 1</h1> -->
          <img src="@/assets/푸카룡.png" alt="" />
        </ion-slide>
        <ion-slide>
          <!-- <h1>Slide 2</h1> -->
          <img src="@/assets/프로필기본사진.jpg" alt="" />
        </ion-slide>
        <ion-slide>
          <!-- <h1>Slide 3</h1> -->
          <img src="@/assets/내프로필사진.jpg" alt="" />
        </ion-slide>
      </ion-slides>

    <strong>인기 트레이너</strong>
    <!-- 카드 -->
      <ion-grid>
        <ion-row v-for="card in cards" :key="card.src">
          <ion-card>
            <!-- <ion-img :src="card.src"></ion-img> -->
            <!-- <img :src="card.src" alt="" /> -->
            <img src="@/assets/내프로필사진.jpg" alt="">
            <ion-card-header>
              <ion-card-subtitle>Card Subtitle</ion-card-subtitle>
              <ion-card-title>Card Title</ion-card-title>
            </ion-card-header>

            <ion-card-content>
              Keep close to Nature's heart... and break clear away, once in awhile,
              and climb a mountain or spend a week in the woods. Wash your spirit clean.
            </ion-card-content>
          </ion-card>
        </ion-row>
      </ion-grid>
    </div>

  <!-- </div> -->
</template>

<script lang="ts">
// 카드
import { IonCard, IonCardContent, IonCardSubtitle, IonCardTitle, IonIcon } from '@ionic/vue';
import { pin, walk, warning, wifi, wine } from 'ionicons/icons';
// import { defineComponent } from 'vue';

// 슬라이드
import { IonSlides, IonSlide } from '@ionic/vue';
import { defineComponent } from 'vue';

export default {
  name: 'Home',
  props: {
    name: String
  },
  // 카드
  // components: { IonCard, IonCardContent, IonCardSubtitle, IonCardTitle, IonIcon, IonItem, IonLabel }
  // 슬라이드
  // components: { IonSlides, IonSlide },
  // 통합
  components: { IonCard, IonCardContent, IonCardSubtitle, IonCardTitle, IonIcon, IonSlides, IonSlide },
  setup() {
    // Optional parameters to pass to the swiper instance. See http://idangero.us/swiper/api/ for valid options.
    const slideOpts = {
      initialSlide: 1,
      speed: 400
    };
    const cards = [{
      'text': 'Card 1',
      'src': '@/assets/내프로필사진.jpg'
    }, {
      'text': 'Card 2',
      'src': '@/assets/푸카룡.png'
    }, {
      'text': 'Card 3',
      'src': '@/assets/프로필기본사진.jpg'
    }];
    return { slideOpts, cards }
  }
}
</script>

<style scoped>
#container {
  /* text-align: center; */
  position: absolute;
  left: 10px;
  right: 10px;
  top: 6%;
  /* transform: translateY(-50%); */
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
}
</style>