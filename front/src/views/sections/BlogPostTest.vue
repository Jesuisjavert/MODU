<template>
  <v-container
    id="blog-post"
    class="pa-0"
    fluid
    tag="section"
  >
    <base-hero :src="require('@/assets/javert2.jpg')" />

    <v-container
      class="py-12 grey lighten-2"
      fluid
    >
      <v-row justify="center">
        <v-col
          cols="11"
          md="7"
        >
          <h1
            class="display-2 font-weight-bold mb-6"
            v-text="post.title"
          />

          <div class="text-uppercase font-weight-bold body-2 pb-6">
            {{ post.date }} / {{ post.category }} / {{ post.comments.length }} Comments
          </div>
        </v-col>

        <template v-for="(t, i) in post.text">
          <v-col
            :key="`col-${i}`"
            cols="11"
            md="7"
          >
            <div
              :key="`p-${i}`"
              class="body-1"
              v-html="t"
            />
          </v-col>

          <v-col
            v-if="post.images[i]"
            :key="`img-${i}`"
            class="my-6"
            cols="7"
          >
            <v-img
              :src="post.images[i]"
              max-height="600"
            />
          </v-col>
        </template>

        <v-col
          class="d-flex flex-wrap"
          cols="11"
          md="7"
        >
          <v-btn
            v-for="(social, i) in socials"
            :key="i"
            :color="social.color"
            class="grow white--text"
            depressed
            height="60"
            min-width="175"
          >
            <v-icon
              left
              v-text="social.icon"
            />

            {{ social.text }}
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

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

    <v-container
      class="py-12 grey lighten-2"
      fluid
    >
      <v-row justify="center">
        <v-col
          cols="10"
          md="7"
        >
          <h3 class="display-1 font-weight-bold mb-8">
            Leave a Comment:
          </h3>

          <v-form>
            <v-row>
              <v-col
                cols="12"
                md="6"
              >
                <v-sheet>
                  <v-text-field
                    flat
                    hide-details
                    label="Your Name"
                    solo
                  />
                </v-sheet>
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-sheet>
                  <v-text-field
                    flat
                    hide-details
                    label="Your Email"
                    solo
                  />
                </v-sheet>
              </v-col>

              <v-col cols="12">
                <v-sheet>
                  <v-textarea
                    flat
                    hide-details
                    label="Your Comment"
                    solo
                  />
                </v-sheet>
              </v-col>
            </v-row>

            <v-btn
              :block="$vuetify.breakpoint.smAndDown"
              class="grey darken-4 white--text mt-6"
              x-large
            >
              Post a Comment
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>

    <v-container
      class="py-6 white px-12"
      fluid
    >
      <v-row>
        <v-col
          class="d-flex align-center text-uppercase"
          cols="5"
        >
          <v-btn text>
            <v-icon left>
              mdi-chevron-left
            </v-icon>

            <span class="hidden-sm-and-down">
              Previous Post
            </span>
          </v-btn>
        </v-col>

        <v-col
          class="text-center"
          cols="2"
        >
          <v-btn
            icon
            to="/blog"
          >
            <v-icon>mdi-view-grid</v-icon>
          </v-btn>
        </v-col>

        <v-col
          class="text-right"
          cols="5"
        >
          <v-btn text>
            <span class="hidden-sm-and-down">
              Next Post
            </span>

            <v-icon right>
              mdi-chevron-right
            </v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
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
        text: [
          '<div>나는 프랑스 북부 Normandie 의 Caen이라는 도시에서 유학을 했다.</div>',
          '<div class="pa-8 white--text font-italic title" style="background-color: #E95776;"> 대충 이렇게 해두면 개소리를 지껄여 놔도 명언처럼 보인다 - Jonna Isseo Boy Neun Ireum</div>',
          '<div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<div class="title font-italic">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<h2 class="display-1">Lorem ipsum dolor sit</h2>',
          '<div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<div class="title font-italic">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
          '<div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam earum ipsa quidem, ipsam adipisci, dolorum ducimus repellat vel sed cum maiores voluptatum enim illum saepe dolor fugit amet laboriosam.</div>',
        ],
        images: {
          2: require('@/assets/javert3.jpg'),
          9: require('@/assets/javert4.jpg'),
        },
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
