<template>
    <div>
        <base-heading class="white--text text-center mb-10 pb-5">손님 가입 페이지입니다</base-heading>
        <v-card color="rgb(255, 255, 255, 0.3)" class="container">
            <div class="mx-5 my-5">
                <v-text-field
                label="이름"
                :rules="rules"
                hide-details="auto"
                type="text"
                ></v-text-field>
                <v-row class="mt-5">
                    <v-col cols="5">
                        <v-text-field
                        label="나이"
                        :rules="rules"
                        hide-details="auto"
                        type="number"
                        ></v-text-field>
                    </v-col>
                    <v-col cols="5" offset="2">
                        <v-select
                        :items="genders"
                        label="성별"
                        ></v-select>
                    </v-col>
                </v-row>
            </div>
        </v-card>
    </div>
</template>

<script>
export default {
    name: "ClientSubmit",
    data() {
        return {
            rules: [
                value => !!value || '필수 입력사항입니다.',
                // value => (value && value.length >= 3) || 'Min 3 characters',
            ],
            genders: [
                '남',
                '여',
            ]
        }
    },
}
</script>

<style>

</style>