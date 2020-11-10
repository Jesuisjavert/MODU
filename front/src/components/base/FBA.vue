<template>
    <v-menu
        v-model="menu"
        :close-on-content-click="false"
        top
        left
        max-width="90%"
        min-width="275"
        offset-x
        offset-y
        origin="bottom right"
        transition="scale-transition"
    >
        <template v-slot:activator="{ attrs, on }">
        <v-card
            id="settings"
            class="py-2 px-4 icon-card"
            color="rgb(255, 0, 0, 0)"
            black
            flat
            style="position: fixed; bottom: 10%; right: 6%;"
            v-bind="attrs"
            v-on="on"
        >
            <v-icon large>
            mdi-bell
            </v-icon>
        </v-card>
        </template>

        <v-card class="">
        <base-title
            align="center"
            title="알림창"
            space="0"
        />

        <v-card-text>
            <v-alert color="green" type="success" class="mb-1">
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <p>{ 프로그램이름 } 의 강의가 시작되었습니다.</p>
                    </v-col>
                    <v-col cols="auto">
                        <WebJoinBtn>입장하기</WebJoinBtn>
                    </v-col>
                </v-row>
            </v-alert>
            <v-alert color="blue" type="info" class="mb-1">
                <v-row>
                    <v-col cols="auto" class="mr-auto">
                        <p>{ 프로그램이름2 } 의 강의가 시작되었습니다.</p>
                    </v-col>
                    <v-col cols="auto">
                        <WebJoinBtn>입장하기</WebJoinBtn>
                    </v-col>
                </v-row>
            </v-alert>
        </v-card-text>
        </v-card>
    </v-menu>
</template>

<script>
export default {
    name: "FBA",
    data() {
        return {
            menu: false,
        }
    },
    components: {
        WebJoinBtn: () => import('@/components/base/WebJoinBtn'),
    }
}
</script>

<style>
    
</style>