<template>
    <!-- <v-row justify="center"> -->
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <!-- <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Open Dialog
        </v-btn> -->
        <v-icon style="cursor: pointer"
            @click="updateProfile"
            v-bind="attrs"
            v-on="on"
        >
            mdi-cog
        </v-icon>
      </template>
      <v-card v-if="!!this.userData.length">
        <v-card-title>
          <span class="headline">회원정보수정</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="4"
              >
                <v-img
                    v-if="!profile_img.length"
                    src="data:image/jpeg;base64,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"
                    max-height="150"
                    max-width="150"
                    class="rounded-circle mr-5"
                    @click="onClickImageUpload"
                >
                </v-img>
                <v-img
                    v-else
                    :src="preview_img[0]"
                    max-height="150"
                    max-width="150"
                    class="rounded-circle mr-5"
                    @click="removeImg"
                ></v-img>
                <input 
                    ref="imageInput"
                    type="file" 
                    @change="uploadimg" 
                    hidden
                    name="profile" 
                />
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="6"
              >
                <v-text-field
                  label="이름"
                  v-model="userData[0].name"
                  type="text"
                  :rules="rules"
                ></v-text-field>
                <v-row>
                  <v-col cols="6" class="mr-auto">
                    <v-text-field
                      label="나이"
                      v-model="userData[0].age"
                      type="number"
                      :rules="rules"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-select
                      label="성별"
                      :items="genders"
                      v-model="userData[0].gender"
                      :rules="rules"
                    ></v-select>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="태그"
                  type="text"
                  v-model="newTag"
                  @keypress.enter="newTagPush"
                ></v-text-field>
              </v-col>
              <v-col v-if="!!this.userData[0].tags.length">
                <v-row>
                  <v-col v-for="(tag, i) in userData[0].tags" :key="tag.id">
                    <v-chip
                      v-if="!!userData[0].tags[i]"
                      class="ma-2"
                      close
                      color="red"
                      text-color="white"
                      @click:close="deleteTag(i)"
                    >
                      {{ userData[0].tags[i] }}
                    </v-chip>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="주소"
                  type="text"
                  v-model="userData[0].address"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="12"
              >
                <v-textarea
                label="자기소개"
                type="text"
                no-resize
                rows="10"
                style="min-width: 96px"
                v-model="userData[0].content"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="submitTrainer"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  <!-- </v-row> -->
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants.js'
import { mapState } from 'vuex'

export default {
  name: "TrainerInfoModal",
  data: () => ({
    userData: [],
    newTag: '',
    tempImg: 'http://d3v9ilm5vhs4go.cloudfront.net/media/api/profile/4eb1dd70-25b3-11eb-b6fa-982cbcaa7282default_img.jpg',
    uploadImg: null,
    rules: [
      value => !!value || '필수 입력사항입니다.',
        // value => (value && value.length >= 3) || 'Min 3 characters',
    ],
    genders: [
      '남',
      '여',
    ],
    dialog: false,
    constants,
    chip2: true,
    profile_img: [],
    preview_img: [],
  }),
  computed: {
    ...mapState(['userToken']),
  },
  methods: {
    updateProfile() {
      console.log('프록필수정')
        const Token = 'Bearer ' + this.userToken 
        axios.get(`${constants.API_URL}rest-auth/user`, {
          headers: {
            Authorization: Token,
            },
        })
        .then((res) => {
          // console.log(res.data)
            this.userData.push(res.data)
            console.log(this.userData[0])
        })
        .catch((err) => {
          console.log(err)
        })
    },
    newTagPush() {
      console.log(this.userData[0].tags.indexOf(this.newTag))
      if (this.userData[0].tags.indexOf(this.newTag) === -1){
        this.userData[0].tags.push(this.newTag)
        this.newTag = ''
      } else {
        alert('이미 존재하는 태그입니다.')
      }
    },
    deleteTag(i){
      this.userData[0].tags.splice(i, 1)
    },
    // 이미지 없을때 이미지 누름
    onClickImageUpload() {
        this.$refs.imageInput.click()
    },
    uploadimg(event) {
        console.log(event);
        const file = event.target.files[0];
        this.profile_img = [];
        this.preview_img = [];
        this.profile_img.push(file);
        this.preview_img.push(URL.createObjectURL(file));
    },
    removeImg() {
        this.profile_img = []
        this.preview_img = []
    },
    profileSubmit() {
        const Token = "Bearer " + this.userToken;
        console.log(Token);
        let formData = new FormData();
        formData.append("profile_img", this.profile_img[0]);
        axios.post(`${constants.API_URL}rest-auth/user/profile/`, formData, {
        headers: {
            Authorization: Token,
        },
        })
        .then((res) => {
          this.$router.go(0)
        });
    },
    submitTrainer(){
        const Token = 'Bearer '+ this.userToken
        let tags = this.userData[0].tags.join();
        console.log(this.userData)
        this.userData[0].taglist = tags;
        this.userData[0].is_first = '1'
        axios.put(`${constants.API_URL}rest-auth/user/`, this.userData[0], {
            headers: {
                Authorization: Token,
            },
        })
        .then(() => {
        if (this.profile_img.length > 0) {
            this.profileSubmit();
            // this.$router.push({ name: 'Home' })
        }
        this.dialog = false
        })
        .catch((err) => {
        console.log(err.response);
        });
    },
    
  },
}
</script>

<style>

</style>