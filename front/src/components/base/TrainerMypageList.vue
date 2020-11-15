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
            <v-expansion-panel-content v-else-if="item.title == '나의 프로그램'">
                <TrainerMyProgram></TrainerMyProgram>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-else-if="item.title == '이번달 수입'">
                <RevenueGraph></RevenueGraph>
            </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
</template>

<script>
export default {
    name: "TrainerMypage",
    components: {
        TrainerMyProgram: () => import('@/components/base/TrainerMyProgram'),
        RevenueGraph: () => import('@/components/base/RevenueGraph'),
    },
    data() {
        return {
            items: [
                {
                    title: '나의 프로그램',
                },
                
                {
                    title: '프로그램 추가',
                },
                {
                    title: '이번달 수입',
                },
                {
                  title: '식단관리',
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
            ],
        }
    },
}
</script>

<style>

</style>