<template>
  <div>
    <v-row justify="center">
      <v-dialog
        v-model="dialog"
        persistent
        max-width="450"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            :color="'primary'"
            class="white--text"
            x-large
            v-bind="attrs"
            v-on="on"
          >
            Write
          </v-btn>
        </template>
        <v-card>
          <v-toolbar
            color="success"
          >
            <v-btn
              icon

              @click="dialog = false"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Create</v-toolbar-title>
            <v-spacer />
            <v-toolbar-items>
              <v-btn
                text
                white
                @click="createArticle"
              >
                Save
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-list
            three-line
            subheader
          >
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>글 제목</v-list-item-title>
                <!-- <base-text-field
                  id="title"
                  v-model="title"
                  label="title"
                  required
                /> -->
                <v-text-field
                  id="title"
                  v-model="title"
                  label="title"
                  required
                />
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>내 용</v-list-item-title>
                <v-textarea
                  id="content"
                  v-model="content"
                  outlined
                  name="input-7-4"
                  label="content"
                />
              </v-list-item-content>
            </v-list-item>
          </v-list>
          <v-divider />
          <v-list
            three-line
            subheader
          />
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
  import axios from 'axios'

  const API_URL = 'http://localhost:4000'

  export default {
    name: 'ArticleCreate',

    data () {
      return {
        user_id: null,
        dialog: false,
        content: null,
        title: null,
        username: null,
      }
    },
    created() {
      this.getUserId()
    },
    methods: {
      getUserId() {
        axios.get(API_URL+"/user/me", {
            headers: {
              Authorization: "Bearer " + this.$cookies.get("accessToken")
            }
          })
          .then((res) => {
            this.user_id = res.data.id
          })
          .catch((err) => {
            this.$cookies.remove("accessToken")
            this.$router.push('/membership')
          })
      },
      createArticle () {
        this.dialog = false

        const createData = {
          "content": this.content,
          "title": this.title,
          "user_id": this.user_id,
        }
        
        axios.post(API_URL + '/api/community', createData) // , RequestHeader
          .then((res) => {
            this.$router.go(0)
          })
          .catch((err) => {
          })
      },
    },
  }
</script>

<style>

</style>
