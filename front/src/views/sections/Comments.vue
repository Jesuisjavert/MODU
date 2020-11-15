<template>
  <v-container
      class="py-12"
      fluid
    >
      <v-row justify="center">
        <v-col
          cols="11"
          md="7"
        >
          <h3 class="display-1 font-weight-bold mb-8">
            Comments:
          </h3>

          <template v-for="(comment, i) in post.comments">
            <blog-post-comment
              :key="i"
              :comment="comment"
            />
          </template>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
  export default {
    name: 'BlogPost',

    components: {
      BlogPostComment: () => import('@/components/base/Comment'),
    },

    data: () => ({
      post: {
        title: 'Javert의 유럽 생존기',
        date: 'September 18, 2020',
        category: 'Nature',
        comments: [
          {
            avatar: 'https://randomuser.me/api/portraits/men/51.jpg',
            user: 'Lee Seungbeom',
            date: '20 September, 2018',
            text: '넌 사슴이야 니 목소리는 날 녹용',
            replies: [
              {
                avatar: 'https://randomuser.me/api/portraits/women/51.jpg',
                user: 'Yonggyun Bae',
                date: '20 September, 2018',
                text: '갑자기 튀어나오는 바퀴벌레 vs 인사하고 튀어나오는 바퀴벌레. 둘 중에 뭐가 좋으세요?',
              },
            ],
          },
          {
            avatar: 'https://randomuser.me/api/portraits/women/32.jpg',
            user: 'Jonna Ippeun Noona',
            date: '21 September, 2018',
            text: '니 리뷰 존나 별로.. 내 마음 속의 별로.. 니 리뷰 그닥 .. 내 마음으로 달그닥',
          },
        ],
      },
      socials: [
        {
          icon: 'mdi-facebook',
          text: 'Facebook',
          color: '#29478A',
        },
        {
          icon: 'mdi-google-plus',
          text: 'Google+',
          color: '#C83820',
        },
        {
          icon: 'mdi-twitter',
          text: 'Twitter',
          color: '#219ACD',
        },
        {
          icon: 'mdi-pinterest',
          text: 'Pinterest',
          color: '#B71117',
        },
      ],
    }),
  }
</script>


<style>

</style>