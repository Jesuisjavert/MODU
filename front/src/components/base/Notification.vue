<template>
    <!-- 연락처 관리에서 treeview 써보기 -->
    <div>
        <notifications group="foo" />
    </div>
</template>

<script>
export default {
    name: "Notification",
    created() {
        this.$notify({
            group: 'foo',
            type: 'default',
            duration: 5000,
            title: 'Important message',
            text: 'Hello user! This is a notification!'
        })
    },
}
</script>

<style>

</style>