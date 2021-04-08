<template>
  <div>
    <div style='text-align:center;'>
      <div v-if='!sending'>
        <h2 class='animate__animated animate__fadeIn animate__delay-1s'>회원가입이 완료되었습니다.</h2>      
        <h2 class='animate__animated animate__fadeIn animate__delay-1s'>메일을 전송 중입니다.</h2>      
        <h2 class='animate__animated animate__fadeIn animate__delay-2s'>잠시만 기다려주세요</h2>    
      </div>            
      <div v-if='sending'>
        <h2 class='animate__animated animate__fadeIn animate__delay-1s'>메일이 전송되었습니다.</h2>      
        <h2 class='animate__animated animate__fadeIn animate__delay-2s'>메일을 확인해주세요.</h2>      
        <button @click='login' class='animate__animated animate__fadeIn animate__delay-3s' style='background-color:blue'>로그인 바로가기</button>  
      </div>
    </div>    
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://j4a302.p.ssafy.io'


export default {
  name:'EmailMessageForm',
  props:{
    data:[Object],
  },
  data(){
    return {
      sending:false,
    }
  },
  methods:{
    sendingMail:function(){
      axios.get(`${SERVER_URL}/apps/v1/sendEmail/${this.data.email}`)
        .then(()=>{
          this.sending = true
        })
    },
    login:function(){      
      axios.post(`${SERVER_URL}/apps/v1/login`,{
        'email':this.data.email,
        'password':this.data.password
      })
        .then(res => { 
          if(res.status !== 200){
            alert('로그인실패')
            return;
          }
          if(!res.data.userInfo[0].is_active){
            alert('이메일인증을 완료해주세요!')
            return
          }
          this.$emit('nextStage',2)
          localStorage.setItem('email',res.data.userInfo[0].email)
          localStorage.setItem('userNo',res.data.userInfo[0].seq)
          localStorage.setItem('register_date',res.data.userInfo[0].register_date)
          localStorage.setItem('JWT',res.data.access_token)          
          setTimeout(() => {
            this.$router.push({name:'Main',params:{nickname:this.data.email}})
            }, 3000);
          })
        .catch(()=>{alert('이메일인증을 완료해주세요!')})
    }

  },
  created(){
    setTimeout(() => {
      this.sendingMail()
    }, 1000);
  }

}
</script>