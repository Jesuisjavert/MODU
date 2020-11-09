<template>
  <div>
      <span>새 프로그램 등록페이지입니다.</span>
      <br>
      <div>
        수업방식 : 
    <input type="radio" id="one" value="오프라인" v-model="inputdata._type">
<label for="one">오프라인</label>
<input type="radio" id="two" value="온라인" v-model="inputdata._type">
<label for="two">온라인</label>
<br>
<label for="title">프로그램 명</label>
<input type="text" v-model="inputdata.title" name="title">

<br>
<div>
  <span>태그등록 : </span>
  <input @input="autocomplete" type="text">
  태그등록
</div>

<div>
  <div v-for="(tag,index) in autocompletelist" :key="index">
    <li>{{tag}} <button @click="appendTag(tag)">추가</button></li>
   
  </div>
</div>

<div>
  <span>등록 태그 : </span>
  <div v-for="(tag,index) in inputdata.tags" :key="index">
    <li>{{tag}}</li>
     <button @click="deleteTag(index)">삭제</button>
  </div> 
</div>

<label for="content">설명 : </label>
<input type="text" v-model="inputdata.content" name="content">
<br>
<label for="image">이미지</label>
<input type="file" @change="uploadimg" name="image">
 <br>
 <div>프로그램 회수 및 가격 설정</div>
 <div v-for=" (data,index) in detaildata" :key="index">
   이름 : <input type="text" v-model="data.title">
   가격 : <input type="number" v-model="data.price">
   횟수 : <input type="number" v-model="data.online_count">
   <button @click="deletedata(index)">x</button>
 </div>
 <button @click="appenddetail">추가</button>
      </div>
      <button @click="createProgram()">제출</button>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/api/constants.js'
import { mapState } from 'vuex'
export default {
    name : 'ProgramCreate',
    data(){
      return {
        inputdata : {
          _type : '',
          title : '',
          content : '',
          thumb_img : [],
          tags : [],

        },
        detaildata :[{
          price : 0,
          title : '',
          online_count : 0
          
        }],
        constants,
        autocompletelist : [],
      }
    },
    methods: {
      uploadimg(event){
        console.log(event)
        const file = event.target.files[0]
        this.inputdata.thumb_img = []
        this.inputdata.thumb_img.push(file)
      },
      appenddetail(){
        this.detaildata.push({
          price : 0,
          title : '',
          online_count : 0
          
        })
      },
      deletedata(index){
        this.detaildata.splice(index,1)
      },
      createProgram(){
        let formData = new FormData()
        let tags = this.inputdata.tags.join()
        let Token = 'Bearer '+this.userToken
        formData.append('title',this.inputdata.title)
        formData.append('content',this.inputdata.content)
        formData.append('_type',this.inputdata._type)
        formData.append('thumb_img',this.inputdata.thumb_img[0])
        formData.append('tags',tags)
        const data = {
          program_detail : this.detaildata
        }
        this.setFormData(formData,data)
        axios.post(`${constants.API_URL}program/`,formData,{
         headers: {
                        Authorization: Token,
                    }
        })
        .then((res)=>{
          console.log(res)
        })
        .catch((err)=>{
          console.log(err.response)
        })

      },
     setFormData(formData, data, parentKey) { if (!(formData instanceof FormData)) return; if (!(data instanceof Object)) return; Object.keys(data).forEach(key => { const val = data[key]; if (parentKey) key = `${parentKey}[${key}]`; if (val instanceof Object && !Array.isArray(val)) { return this.setFormData(formData, val, key); } if (Array.isArray(val)) { val.forEach((v, idx) => { if (v instanceof Object) { this.setFormData(formData, v, `${key}[${idx}]`); } else { formData.append(`${key}[${idx}]`, v); } }); } else { formData.append(key, val); } }); }
    ,autocomplete(event){
      this.autocompletelist = []
      const inputValue = event.target.value.trim()
      if(inputValue.length > 0){
        this.constants.tags.forEach((item)=>{
         if(item.includes(inputValue)){
           this.autocompletelist.push(item)
         }
       })

      }
    },
    appendTag(tag){
      console.log(this.inputdata.tags.indexOf(tag))
      if (this.inputdata.tags.indexOf(tag) === -1){
        this.inputdata.tags.push(tag)

      }
    },
    deleteTag(index){
      this.inputdata.tags.splice(index,1)
    }


    },
    computed : {
      ...mapState(['userToken'])
    }

}
</script>

<style>

</style>