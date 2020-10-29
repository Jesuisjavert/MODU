<template>
  <div class="side_wrapper">
    <section class="about-dev">
      <header class="profile-card_header">
        <div class="profile-card_header-container">
          <div class="profile-card_header-imgbox">
            <img v-bind:src="user.picture"/>
          </div>
          <h1>{{user.name}} <span>{{user.email}}</span></h1>
        </div>
      </header>
      <div class="profile-card_about">
        <h2>For your Dream, Apolio</h2>
        <footer class="profile-card_footer">
          <div class="social-row">
            <v-btn
              color="primary"
              @click="logout"
            >
              Logout
            </v-btn>

          </div>
        </footer>
      </div>
    </section>
  </div>
</template>

<script>
  import { mapGetters } from "vuex";
  import axios from 'axios'

  const API_URL = 'http://localhost:4000/user/me'

  export default {
    name: 'Mypage',
    data() {
      return {
        key: null,
        user: {
          name: null,
          email: null,
          picture: null,
          role: null,
          created_date: null,
        }
      }
    },
    created() {
      this.getUserInfo()
    },
    methods: {
      logout() {
        this.$cookies.remove("accessToken")
        this.$router.push('/')
      },
      getUserInfo() {
        axios.get(API_URL, {
            headers: {
              Authorization: "Bearer " + this.$cookies.get("accessToken")
            }
          })
          .then((res) => {
            this.user.picture = res.data.picture
            this.user.name = res.data.username
            this.user.role = res.data.role
            this.user.created_date = res.data.created_date
            this.user.email = res.data.email
          })
          .catch((err) => {
            this.$cookies.remove("accessToken")
            this.$router.push('/membership')
          })
      }
    }
  }
</script>

<style scoped>
  * {
    box-sizing: border-box;
  }

  html {
    font-size: 100%;
  }

  body {
    padding: 0;
    margin: 0;
    min-height: 100vh;
  }

  .sidebar_wrapper {
    width: 100%;
    max-width: 26rem;
  }

  .about-dev {
    width: 100%;
    max-width: 26rem;
    margin: auto;
    box-shadow: 2px 4px 2px -2px rgba(247, 0, 0, 0.3), -2px -4px 15px -2px rgba(0, 0, 0, .2);
    animation: profile_in 0.8s;
  }

  @keyframes profile_in {
    0% {
      opacity: 0;
      transform: translateY(30%);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }


  /* profile card header */

  .profile-card_header-container {
    max-width: 15rem;
    margin: auto;
  }

  .profile-card_header {
    background: #ff6b87;
    border-left: 0.625rem solid #eaf9ff;
    padding: 1.5em 1.5em 1em;
    text-align: center;
  }


  /* profile picture */

  .profile-card_header-imgbox {
    display: block;
    width: 9.5rem;
    height: 9.5rem;
    overflow: hidden;
    border-radius: 50%;
    margin: auto;
    background: rgba(250, 214, 195, 1);
    border: 0.375rem solid rgba(250, 214, 195, 1);
  }

  .profile-card_header img {
    max-width: 100%;
    filter: grayscale(100%);
  }


  /* header heading */

  .profile-card_header h1 {
    color: #f3f3f3;
    font-size: 1.5rem;
    margin-top: 0.8em;
    font-family: 'Oswald', sans-serif;
    font-weight: normal;
    position: relative;
  }


  /* header text span */

  .profile-card_header h1 span {
    font-size: 1.2rem;
    font-weight: 300;
    display: block;
    color: rgba(220, 220, 220, .95);
    margin-top: 0.25em;
    padding-top: 0.25em;
    border-top: 0.075em solid rgba(250, 214, 195, 1);
  }


  /* about section */

  .profile-card_about {
    line-height: 1.5;
    background: #ffeaee;
    padding: 1.5em 2rem;
    color: #222;
    font-family: 'Lato', sans-serif;
  }

  .profile-card_about h2 {
    margin: 0;
    display: inline-block;
    color: #333;
    font-weight: normal;
    text-transform: uppercase;
    font-size: 1.3rem;
    position: relative;
    z-index: 2;
    vertical-align: middle;
  }

  .profile-card_about h2::before {
    content: '';
    position: absolute;
    width: 110%;
    /*  max-width: 13.8rem;
  */
    height: 1rem;
    background: #ffeaee;
    left: -5px;
    top: 50%;
    z-index: -1;
  }

  .profile-card_about p {
    font-weight: 300;
  }

  .profile-card_footer {
    margin-top: 1.5em;
    text-align: right;
  }


  /* social row */

  .social-row {
    margin-right: 0.5em;
  }

  .paw-icon,
  .heart-icon {
    display: inline-block;
    margin-left: 0.5em;
    transition: transform 0.3s;
  }

  #pawi,
  #hearti {
    height: 1.8rem;
    width: 1.8rem;
    cursor: help;
    -webkit-transition: fill 0.3s ease-in-out;
    transition: fill 0.3s ease-in-out;
  }

  #pawi path,
  #hearti path {
    fill: #272727;
  }

  .paw-icon:hover,
  .heart-icon:hover {
    transform: scale(1.2);
  }


  /* back to profile link */

  @media screen and (max-width: 26em) {
    .side_wrapper {
      min-height: 100vh;
      background: #ededed;
    }
    .about-dev {
      box-shadow: none;
    }
  }

  @media screen and (min-width: 33em) {
    .side_wrapper {
      margin: 2rem auto;
    }
    .profile-card_header {
      padding: 1.5em 4em 1em;
    }
  }

  @media screen and (min-height: 46em) {
    .side_wrapper {
      width: 100%;
      max-width: 26rem;
      margin: 0;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    .about-dev {
      max-width: 26rem;
    }
  }
</style>