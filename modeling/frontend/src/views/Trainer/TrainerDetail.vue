<template>
	<div>
		<h1>트레이너 디테일</h1>
		<div>
			<img :src=trainer.user.image_url height="300px">
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
    }
	},
	created() {
		this.get_trainer()
		this.get_comment()
	},
  methods: {
		get_trainer() {
			const pk = this.$route.params.pk
      axios.get(`${this.constants.API_URL}trainer/${pk}/`)
        .then((res)=>{
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
    }
  }
}
</script>