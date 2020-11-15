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
                    :src="userData[0].user.image_url"
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
            @click="pressClose"
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
        const Token = 'Bearer ' + this.userToken 
        axios.get(`${constants.API_URL}rest-auth/user`, {
          headers: {
            Authorization: Token,
            },
        })
        .then((res) => {
          // console.log(res.data)
            this.userData.push(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    newTagPush() {
      // console.log(this.userData[0].tags.indexOf(this.newTag))
      // console.log(this.userData[0].tags)
      if (this.userData[0].tags.indexOf(this.newTag) === -1){
        console.log('냠냠냠')
        this.userData[0].tags.push(this.newTag)
        print(this.userData[0].tags)
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
    pressClose() {
      this.dialog = false
      this.$router.go(0)
    }
  },
}
</script>

<style>

</style>