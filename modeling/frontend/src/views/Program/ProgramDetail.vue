<template>
  <div>
      <div>프로그램 디테일</div>
			<img :src=program.image_url height="300px">

			<hr>

			<h3>{{program.title}}</h3>

			<hr>

			<div>
				<h3>가격</h3>
				<div v-for="price in program.programprice" :key="price.id">
					<p>{{price}}</p>
				</div>
			</div>

			<hr>

			<div>
				<h3>신청한 유저들</h3>
				<div v-for="client in clients" :key="client.id">
					<p>{{client}}</p>
				</div>
			</div>

			<hr>

			<div>
				<h3>프로그램 댓글</h3>
				<div v-for="comment in comments" :key="comment.id">
					<p>{{comment}}</p>
				</div>
			</div>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'

export default {
    name : 'ProgramDetail',
  
    data(){
      return {
        constants,
        program: {
					"image": null,
					"title": null,
					"content": null,
				},
				clients: null,
				comments: null,
      }
    },

    created() {
			this.get_program()
			this.get_client()
			this.get_comment()
    },

    methods: {
      get_program() {
				const pk = this.$route.params.pk
        axios.get(`${this.constants.API_URL}program/`+pk)
          .then((res)=>{
            this.program = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
			},
			get_client() {
				const pk = this.$route.params.pk
        axios.get(`${this.constants.API_URL}program/` + pk + '/user/')
          .then((res)=>{
            this.clients = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
			},
			get_comment() {
				const pk = this.$route.params.pk
        axios.get(`${this.constants.API_URL}program/` + pk + '/comment/')
          .then((res)=>{
            this.comments = res.data
          })
          .catch((err)=>{
            console.log(err)
          })
			}
    },
    
    computed : {
    }

}
</script>

<style>

</style>