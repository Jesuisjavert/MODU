<template>
    <VideoBg>
    <!-- <div> -->
        <ItemRow v-if="isLogined === false">
            <base-heading class="white--text text-center">당신의 운동 파트너</base-heading>
            <base-heading class="white--text text-center mt-10">모두의 헬스와 함께</base-heading>
            <base-heading class="white--text text-center my-10 pb-5">카카오톡을 통해 지금 바로 시작해보세요</base-heading>
            <KakaoLoginBtn class="mt-10 pt-5"></KakaoLoginBtn>
        </ItemRow>
        <ItemRow v-else-if="isLogined === true">
            <div v-if="!selected">
                <base-heading class="white--text text-center">모두의 헬스가</base-heading>
                <base-heading class="white--text text-center mt-10">처음이시군요</base-heading>
                <base-heading class="white--text text-center my-10 pb-5">가입하실 방법을 선택해주세요</base-heading>
            </div>
            <v-row class="justify-center mt-10 pt-5">
                <!-- <JoinBtn class="mx-5">트레이너</JoinBtn>
                <JoinBtn class="mx-5">손님</JoinBtn> -->
                <div v-if="!selected">
                    <Btn class="mx-5" @click="select('trainer')">트레이너</Btn>
                    <Btn class="mx-5" @click="select('client')">손님</Btn>
                </div>
                <div v-else>
                    <div v-if="selected === 'trainer'">
                        <TrainerSubmit></TrainerSubmit>
                    </div>
                    <div v-else-if="selected === 'client'">
                        <ClientSubmit></ClientSubmit>
                    </div>
                    <v-col class="font-weight-black">
                        <span class="mr-5">혹시 선택을 잘못하셨나요?</span>
                        <span class="blue--text text-decoration-underline" @click="clear" style="cursor: pointer">초기화</span>
                        <span class="ml-1">버튼을 눌러보세요</span>
                    </v-col>
                </div>
            </v-row>
        </ItemRow>
    <!-- </div> -->
    </VideoBg>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name : 'LoginView',
    components: {
        VideoBg: () => import('@/components/base/VideoBg'),
        ItemRow: () => import('@/components/base/ItemRow'),
        KakaoLoginBtn: () => import('@/components/base/KakaoLoginBtn'),
        // JoinBtn: () => import('@/components/base/JoinBtn'),
        Btn: () => import('@/components/base/Btn'),
        TrainerSubmit: () => import('@/components/base/TrainerSubmit'),
        ClientSubmit: () => import('@/components/base/ClientSubmit'),
    },
    computed: {
        ...mapGetters(['isLogined'])
    },
    watch: {
        isKakaoLoginCheck: function () {
            // console.log('여긴 watch', newVal)
        }
    },
    data () {
        return {
            isKakaoLoginCheck: false,
            selected: false
        }
    },
    methods: {
        select(input) {
            this.selected = input
        },
        clear() {
            this.selected = false
        }
    }
}
</script>

<style>

</style>