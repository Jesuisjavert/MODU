<template>
  <v-container
    id="blog"
    class="pa-0"
    fluid
    tag="section"
  >
    <blog-hero
      class="text-center white--text align-center"
      height="30vh"
    >
      <h1 class="display-2">
        Things that I learned
      </h1>
    </blog-hero>

    <v-responsive
      class="mx-auto"
      max-width="1280"
    >
      <v-container>
        <v-filter :tabs="tabs" />

        <v-row>
          <v-col
            v-for="(post, i) in posts"
            :key="i"
            class="d-flex"
            cols="12"
            md="4"
          >
            <post-card :post="post" />
          </v-col>
        </v-row>
      </v-container> <v-spacer/>
      <div class="text-center">
        <v-btn
          class="white--text"
          color="black"
          x-large
          @click="createBlog"
        >
          Write
        </v-btn>
      </div>
    </v-responsive>
  </v-container>
</template>

<script>
  import axios from 'axios'

  const API_URL = 'http://localhost:4000'

  export default {
    name: 'Blog',

    components: {
      PostCard: () => import('@/components/base/BlogPostCard'),
      BlogHero: () => import('@/components/base/BlogHero'),
      VFilter: () => import('@/components/base/Filter'),
    },

    data () {
      return {
        tabs: [
          'All',
          '운영체제',
          '소프트웨어공학',
          '자료구조',
          'Django',
          '알고리즘',
          '스프링',
          '클라우드',
        ],
        posts: []
      }
    },
    created() {
      this.loadblog()
    },
    methods: {
      createBlog() {
        axios.get(API_URL+"/user/me", {
            headers: {
              Authorization: "Bearer " + this.$cookies.get("accessToken")
            }
          })
          .then((res) => {
            this.$router.push('/blog/create')
          })
          .catch((err) => {
            this.$cookies.remove("accessToken")
            this.$router.push('/membership')
          })
      },
      loadblog() {
        axios.get(API_URL+"/api/blog")
          .then((res) => {
            this.posts = res.data
          })
          .catch((err) => {
          })
      },
    }
  }
</script>
