<template>
    <v-expansion-panels focusable>
        <v-expansion-panel
        v-for="(item,i) in items"
        :key="i"
        >
            <v-expansion-panel-header disable-icon-rotate>
                <p class="text-center mb-0">{{ item.title }}</p>
                <template v-slot:actions>
                    <v-icon></v-icon>
                </template>
            </v-expansion-panel-header>
            <v-expansion-panel-content v-if="item.title == '고객관리'">
                <p v-for="client in item.content" :key="client.name">
                    {{ client }}
                </p>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-else>
                {{ item.content }}
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
</template>

<script>
export default {
    name: "TrainerMypage",
    data() {
        return {
            items: [
                {
                    title: '나의 프로그램',
                    content: '줌바와 함께 줌바댄스를',
                },
                {
                    title: '고객관리',
                    content: [
                        '이창완',
                        '강동훈',
                        '강병국',
                        '배용균',
                    ]
                },
                {
                    title: '프로그램 추가',
                    content: '프로그램 추가하기'
                },
                {
                    title: '식단관리',
                    content: '식단짜주기',
                },
                {
                    title: '설정',
                    content: '설정리스트',
                }
            ],
        }
    }
}
</script>

<style>

</style>