<template>
    <video-bg
    :sources="['https://static.videezy.com/system/resources/previews/000/051/317/original/001528-HD-FitnessDYB18.mp4']"
    img="https://static.videezy.com/system/resources/previews/000/051/317/original/001528-HD-FitnessDYB18.mp4"
    class="background-video"
    >
        <slot />
    </video-bg>
</template>

<script>
export default {
    name: "MypageBg",
}
</script>

<style scoped>
    .background-video {
        opacity: 1;
    }
</style>