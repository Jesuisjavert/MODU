<template>
    <video-bg 
    :sources="['https://static.videezy.com/system/resources/previews/000/049/906/original/2645_SlowBeautifulWomanLiftWeightWithTrainer.mp4']" 
    img="https://static.videezy.com/system/resources/previews/000/049/906/original/2645_SlowBeautifulWomanLiftWeightWithTrainer.mp4"
    class="background-video"
    >
        <slot />
    </video-bg>
</template>

<script>
export default {
    name: "VideoBg",
}
</script>

<style scoped>
    .background-video {
        opacity: 0.81;
    }
</style>