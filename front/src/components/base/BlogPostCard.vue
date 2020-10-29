<template>
  <v-card>
    <v-img
      :src="post.img_thumb"
      height="200"
    >
      <router-link to="/blog-post">
        <v-hover>
          <template v-slot="{ hover }">
            <v-overlay
              :color="hover ? 'white' : 'black'"
              absolute
              class="align-end pa-3 justify-start"
              opacity=".2"
            >
              <!-- <v-btn
                color="#252525"
                dark
                small
              >
                {{ post.category }}
              </v-btn> -->
            </v-overlay>
          </template>
        </v-hover>
      </router-link>
    </v-img>

    <div class="px-3 pb-4">
      <v-card-title
        class="headline font-weight-bold mb-2"
        v-text="post.title"
      />
      <v-card-text class="body-1 grey--text text-darken-2">
        <div
          class="mb-4"
          v-text="post.create_date"
        />

        <div v-text="post.description" />
      </v-card-text>
      
      <button class="like-button" @click="heartClick">
        <img class="heart" src="@/assets/heart_like.png" alt="좋아요" v-if=status>
        <img class="heart" src="@/assets/heart.png" alt="좋아요" v-else>
        <span>{{heartCount}}</span>
      </button>
    </div>
  </v-card>
</template>

<script>
  import _ from 'lodash'
  import axios from 'axios'

  const API_URL = 'http://localhost:4000'

  export default {
    name: 'BlogCard',

    props: {
      post: {
        type: Object,
        default: () => ({
          category: undefined,
          date: undefined,
          blurb: undefined,
          src: undefined,
          title: undefined,
          hearts: undefined,
          id: undefined,
        }),
      },
    },
    data() {
      return {
        heartCount: 0,
        status: false,
        user_id: null,
      }
    },
    created() {
      this.getHeartInfo()
    },
    methods: {
      getHeartInfo() {
        this.heartCount = _.size(this.post.hearts)
      },
      heartClick() {
        this.status = !this.status
        if (this.status) {
          this.heartCount += 1
        } else {
          this.heartCount -= 1
        }
      },
    },

  }
</script>

<style lang="scss" scoped>
$gray: #c7c7c7;
$pink: #ff6e6f;
$bezier: cubic-bezier(.175, .885, .32, 1.275);

.like-button {
  border: 2px solid $gray;
  width: 23%;
  border-radius: 40px;
  padding: 0px 10px;
  color: darken($gray, 25%);
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  transition: all .25s $bezier;

  user-select: none;
  .heart{
    vertical-align: middle;
    width: 20px;
    height: 20px;
  }
  span {
    vertical-align: middle;
    margin-left: 12px;
  }
}
</style>