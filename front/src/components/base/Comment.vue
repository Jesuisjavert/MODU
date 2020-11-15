<template>
  <v-row>
    <v-col cols="auto">
        <v-img 
          :src="comment.client.user.image_url" 
          max-width="60"
          max-height="60"
          class="rounded-circle"
        />
    </v-col>

    <v-col cols="9">
        <v-col
          class="body-1 font-weight-black text-start pa-0"
          cols="12"
          v-text="comment.client.name"
        />
        <v-col class="pa-0">
          <v-rating
              :value="comment.rate"
              color="amber"
              dense
              half-increments
              readonly
              size="14"
              class="pa-0 text-start"
            ></v-rating>
        </v-col>
        <v-col
          class="body-2 font-weight-bold text-start ma-0 pa-0 pt-2"
          cols="12"
        >
          <p class="text-start grey--text">{{ comment.content }}</p>
        </v-col>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    name: 'BlogPostComment',

    props: {
      comment: {
        type: Object,
        // default: () => ({
        //   avatar: undefined,
        //   user: undefined,
        //   date: undefined,
        //   replies: [],
        //   text: undefined,
        // }),
      },
      nested: {
        type: Boolean,
        default: false,
      },
    },
  }
</script>
