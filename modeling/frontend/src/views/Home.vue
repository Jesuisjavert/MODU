<template>
  <div class="home">
    <h1>kakao login</h1>
    <button @click="kakaoLogin"></button>
  </div>
</template>

<script>
import axios from 'axios'
    export default {
        methods: {
            kakaoLogin() {
                window.Kakao.Auth.login({
                    scope : 'profile, account_email',
                    success: this.GetMe,
                });
            },
            async GetMe(authObj){
                console.log(authObj);
                window.Kakao.API.request({
                    url:'/v2/user/me',
                    success : res => {
                        const kakao_account = res.kakao_account;
                        console.log(kakao_account)
                        const userInfo = {
                            nickname : kakao_account.profile.nickname,
                            email : kakao_account.email,
                            password : '',
                            account_type : 2,
                        }
                        console.log(userInfo)
                        let accessToken = authObj.access_token
                        let form = new FormData()
                        form.append('access_token', accessToken)
                        axios.post('http://127.0.0.1:8000/api/rest-auth/kakao/login/',form)
                        .then((res)=>{
                          console.log(res)
                        })
                        .catch((err)=>{
                          console.log(err)
                        })

                    },
                    fail : error => {
                        console.log(error);
                    }
                })
            }
        }
    }
</script>
