<template>
  <div id="email-form">
    <div>
      <label for=""><i class='far fa-envelope-open'></i> E-mail</label><br>
      <input type="text" v-model='data.email' placeholder="ex) alroha@algoga.com" @input='emailInput'>
      <p :class="{'check-ok':check.email,'check-no':!check.email}">{{mes.email}}</p>
    </div>
    <div class='signup-btn-div'>
      <button style='visibility:hidden'>PREV</button>
      <button @click='nextStage(2)' :class="{'btn-check-ok':check.email}">NEXT</button>
    </div>
  </div>
</template>

<script>
// let regEmail = /^[A-Za-z0-9_-]+@[A-Za-z0-9]+[.]+[A-Za-z0-9]+/;
let regEmail = /^[A-Za-z0-9_-]+@[A-Za-z0-9]+[.]+['com']+/;

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
      this.check.email = true
      this.mes.email = '이메일이 확인되었습니다.'
    },
    nextStage:function(idx){
      if (this.check.email === false) {return}
      this.$emit('nextStage',idx,this.data)
    }
  }

}
</script>

<style>

</style>