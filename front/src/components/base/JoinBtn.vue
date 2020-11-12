<template>
    <Btn @click="join">
        <slot />
    </Btn>
</template>

<script>
export default {
    name: "JoinBtn",
    components: {
        Btn: () => import('@/components/base/Btn')
    },
    methods: {
        join() {
            
        }
    },
}
</script>

<style>

</style>