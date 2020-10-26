<template>
    <!-- 서치바 문서 더 뒤지면 종류별로 많음 -->
    <!-- Default Searchbar -->
    <ion-searchbar></ion-searchbar>
    
    <h3 class="ion-text-center">마이페이지</h3>
    <ion-col class="ion-text-center">
        <a href="/clientmanage"><p><strong>회원관리</strong></p></a>
        <a href="#"><p><strong>홈트레이닝 시작하기</strong></p></a>
        <a href="#"><p><strong>Client로 변경</strong></p></a>
        <a href="#"><p><strong>Settings</strong></p></a>
        <ion-router>
            <ion-route component="ClientManage">
                <ion-route url="/clientmage" component="ClientManage">회원관리</ion-route>
            </ion-route>
        </ion-router>
        
    </ion-col>
    
</template>

<script>
// 서치바
// import { IonSearchbar, IonToolbar } from '@ionic/vue';
// import { defineComponent } from 'vue';

export default {
    // 서치바
    // components: { IonSearchbar, IonToolbar }
}
</script>