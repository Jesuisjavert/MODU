<template>
	<div>
		<h1>트레이너 디테일</h1>
		<div>
			<img :src=trainer.user.image_url height="300px">
		</div>

    <hr>

    <div v-for="program in programs" :key="program.id">
      {{program.id}} {{program.title}}
    </div>
    <div>
      <h3>예약하기</h3>
      <input type="date" name="" id="" v-model="date">날자
      <input type="number" name="" id="" v-model="time">시간
      <input type="number" name="" id="" v-model="program_id"> 프로젝트 넘버
      <button @click="reservation"></button>
    </div>

	</div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants'
export default {
  data(){
    return {
			constants,
			comment: null,
			trainer: {
        user: {
          "image_url": null
        }
      },
      date: null,
      time: null,
      program_id: null,
      programs: null,
    }
	},
	created() {
		this.get_trainer()
    this.get_comment()
    this.get_programs()
	},
  methods: {
		get_trainer() {
			const pk = this.$route.params.pk
      axios.get(`${this.constants.API_URL}trainer/${pk}/`)
        .then((res)=>{
          console.log(res.data)
          this.trainer = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
		},
    get_comment() {
			const pk = this.$route.params.pk
      axios.get(`${this.constants.API_URL}trainer/${pk}/comment/`)
        .then((res)=>{
          this.comment = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    get_programs() {
      const pk = this.$route.params.pk
      axios.get(`${this.constants.API_URL}trainer/${pk}/program/`)
        .then((res)=>{
          this.programs = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    reservation() {
      let form = new FormData()
      form.append('date', this.date)
      form.append('time', this.time)
      form.append('program_id', this.program_id)
			const pk = this.$route.params.pk
      axios.post(`${this.constants.API_URL}trainer/${pk}/reservation/`,form)
      .then((res)=>{
        console.log(res.data)
      })
    }
  }
}
</script>