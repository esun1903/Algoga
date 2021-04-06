<template>
  <div id="email-form">
    <div>
      <label for=""><i class='far fa-envelope-open'></i> E-mail</label><br>
      <input type="text" v-model='data.email' placeholder="ex) alroha@algoga.com" @input='emailInput' @keydown.enter="nextStage(2)">
      <p :class="{'check-ok':check.email,'check-no':!check.email}">{{mes.email}}</p>
    </div>
    <div class='signup-btn-div '>
      <button style='visibility:hidden'>PREV</button>
      <button @click='nextStage(2)' :class="{'btn-check-ok':check.email}" id='sendLoadingBtn'>
        Next
      </button>
    </div>
  </div>
</template>

<script>
// let regEmail = /^[A-Za-z0-9_-]+@[A-Za-z0-9]+[.]+[A-Za-z0-9]+/;
let regEmail = /^[A-Za-z0-9_-]+@[A-Za-z0-9]+[.]+['com']+/;

import axios from 'axios'

const SERVER_URL = 'http://j4a302.p.ssafy.io'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL




export default {
  name:'EmailForm',
  data:function(){
    return {
      data:{
        email:'',
      },
      check:{
        email:false,
      },
      mes:{
        email:""
      }
    }
  },
  methods:{
    emailInput:function(event){
      const input = event.target.value
      
      if (!input){
        this.mes.email = ''
        return
      } else if (!regEmail.test(input)) {
        this.mes.email = '형식을 확인해주세요'
        this.check.email = false
        return
      }

      axios.get(`${SERVER_URL}/apps/v1/emailoverlapCheck/${input}`)
        .then((res)=>{
          console.log(res)
          this.check.email = true
          this.mes.email = '이메일이 확인되었습니다.'
        })
        .catch(()=>{
          this.check.email = false
          this.mes.email = '중복된 메일이 존재합니다.'
        })      
      // this.check.email = true
      // this.mes.email = '이메일이 확인되었습니다.'
    },
    nextStage:function(idx){
      if (this.check.email === false) {return}
      this.$emit('nextStage',idx,this.data)
    },
  }

}
</script>

<style>


.loading {
  width: 20px;
  height:20px;
  border-radius: 50%;
  border: 2px solid white;
  border-bottom: none;
  border-left: none;
  animation: loading 0.5s infinite;
  margin: 0 auto;
}

@keyframes loading {
  to {
    transform: rotate(360deg);
  }
  
}


</style>