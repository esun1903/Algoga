<template>
  <div id="password-form">
    <div>
      <label for=""><i class='fas fa-key'></i> Password</label><br>
      <input type="password" v-model='data.password' placeholder="영문 2자이상, 특수문자 및 숫자 1자 이상, 총 8자이상" @input='pwInput($event,0)' @keypress.enter='nextStage(2)'>
      <p :class="{'check-ok':check.password,'check-no':!check.password}">{{mes.password}}</p>
			<br>
      <label for=""><i class='fas fa-key'></i> Confirm Password</label><br>
      <input type="password" v-model='data.passwordConfirm' placeholder="비밀번호를 입력해주세요" @input='pwInput($event,1)' @keypress.enter='nextStage(2)'>
      <p :class="{'check-ok':check.passwordConfirm,'check-no':!check.passwordConfirm}">{{mes.passwordConfirm}}</p>
    </div>
    <div class='signup-btn-div'>
      <button @click='nextStage(-2)'>PREV</button>
      <button @click='nextStage(2)' :class="{'btn-check-ok':check.password&&check.passwordConfirm}">NEXT</button>
    </div>
  </div>
</template>

<script>
let regPw = /(?=.*\d{1,50})(?=.*[~`!@#$%^&*()-+=]{1,50})(?=.*[a-zA-Z]{2,50}).{8,50}$/;



export default {
  name:'PasswordForm',
  data:function(){
    return {
      data:{
        password:'',
        passwordConfirm:'',
      },
      check:{
        password:false,
        passwordConfirm:false,
      },
      mes:{
        password:'',
        passwordConfirm:'',
      }
    }
  },
  methods:{
    pwInput:function(event,idx){
			const input = event.target.value
			if(!input) {
				if (idx === 0) {this.check.password = false;
				this.mes.password = ''}
				else {this.check.passwordConfirm = false
				this.mes.passwordConfirm = ''}
				return
			} else if (idx === 1 && !this.check.password) {
				this.check.passwordConfirm = false
				this.mes.passwordConfirm = '비밀번호를 확인해주세요'
				return
			} else if (idx === 1 && this.check.password && this.data.password !== this.data.passwordConfirm) {
				this.check.passwordConfirm = false
				this.mes.passwordConfirm = '비밀번호를 일치시켜 주세요'
			} else if (idx === 1 && this.check.password && this.data.password === this.data.passwordConfirm) {
				this.check.passwordConfirm = true
				this.mes.passwordConfirm = '비밀번호가 확인되었습니다.'
			} 
			
			if (idx === 0 && !regPw.test(input)) {
				this.check.password = false
				this.mes.password = '비밀번호 양식을 확인해주세요.'
			} else if (idx === 0 && regPw.test(input)) {
				this.check.password = true
				this.mes.password = '안전한 비밀번호입니다'
			}
      
    },
    nextStage:function(idx){
      if ((!this.check.password || !this.check.passwordConfirm) && idx >0){return}
      this.$emit('nextStage',idx,this.data)
    },

  }

}
</script>

<style>

</style>