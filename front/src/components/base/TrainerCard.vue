<template>
  <v-card
    :loading="loading"
    class="mx-4 my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      :src="this.$attrs.user.image_url"
    ></v-img>

    <v-card-title>{{this.$attrs.name}}</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ml-4">
          4.5 (413)
        </div>
      </v-row>

      <div class="my-4 subtitle-1" v-for="tag in this.$attrs.tags" :key="tag.id">
        <p>- {{tag.name}} </p>
      </div>

      <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Tonight's availability</v-card-title>

    <v-card-text>
      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      >
        <div v-for="scheudle in scheudles" :key="scheudle.id">
          <v-chip>{{scheudle}}</v-chip>
        </div>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="reserve"
      >
        Reserve
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
  export default {
    data: () => ({
      loading: false,
      selection: 1,
      holyday: false,
      scheudles: [],
    }),
    props: ['trainer'],
    created() {
      this.get_schedule()
    },
    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
      get_schedule() {
        var week = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'];
        var dayOfWeek = week[new Date().getDay()];

        var flag = true

        for (var i=0, item; item=this.$attrs.trainerschedule[i]; i++) {
          if (item.day==dayOfWeek)
            flag = false
            for (var i=8; i<18 ; i++){
              this.scheudles.push(i +":00 " +(i<12 ? "AM" : "PM"))
            }
        }
        if (flag){
          console.log("휴무일 입니다.")
        }
      },
    },
  }
</script>