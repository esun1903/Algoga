<template>
  <div id="signup-section">    
    <EmailForm v-if='nowIdx === 0' @nextStage='nextStage'/>
    <PasswordForm v-else-if='nowIdx === 2' @nextStage='nextStage'/>
    <BojForm v-else-if='nowIdx === 4' @nextStage='nextStage'/>
    <UserForm v-else-if='nowIdx === 6' @nextStage='nextStage'/>
    <StartForm v-else />
  </div>
</template>

<script>
import EmailForm from "@/components/Signup/EmailForm"
import PasswordForm from "@/components/Signup/PasswordForm"
import BojForm from "@/components/Signup/BojForm"
import UserForm from "@/components/Signup/UserForm"
import StartForm from "@/components/Signup/StartForm"

import axios from "axios"

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
const SERVER_URL = 'http://j4a302.p.ssafy.io:8000'

export default {
  name:"SignupSection",
  components:{
    EmailForm,
    PasswordForm,
    BojForm,
    UserForm,
    StartForm,

  },
  props:{
    nowIdx:Number,
  },
  data:function(){
    return{
      data:{
        email:'',
        password:'',
        bake_id:'',
        nickname:'',
        profile_image:'profile image test null',
        register_date: "2021-03-25T11:22:05.954Z",
      },
    }
  },
  methods:{
    nextStage:function(idx,data){
      if (this.nowIdx === 0) {
        this.data.email = data.email
      } else if (this.nowIdx === 2) {
        this.data.password = data.password
      } else if (this.nowIdx === 4) {
        this.data.bake_id = data.boj
      } else if (this.nowIdx === 6) {
        this.data.nickname = data.nickname
        if (idx === 2) {
          this.signUp()
        }
      }
      if (idx === 2 && this.nowIdx === 6) {
        return
      }
      this.$emit('nextStage',idx) 
    },
    signUp:function(){
      axios.post(`${SERVER_URL}/apps/v1/signUp`,this.data)
        .then(res => {
          if (res.status === 201) {
            this.$emit('nextStage',2) 
            this.login()
          }
        })
        .catch(err=>{
          alert(err.data)
        })
    },
    login: function(){
      
      axios.get(`${SERVER_URL}/apps/v1/login/${this.data.email}/${this.data.password}`)
        .then(res=>{
          if(res.status !== 200) {
            alert('로그인실패')
            return
          }
          setTimeout(() => {
            this.$router.push({name:'Main',params:{nickname:this.data.nickname}})
            
          }, 3000);
        })
        .catch(err => {
          alert(err.data)
        })


      
    }
  }
  
}
</script>

<style>
#signup-section {
  width: 50%;
  height:70%;
  margin:50px auto 0;
  padding: 50px 0 0;
  display:flex; justify-content: flex-start;  flex-direction: column;    
}

#signup-section button{
  width: 150px;height: 50px;
  border:none; outline: none;  
  border-radius: 50px;
  color:white;
  font-weight: bold;
  transition: .3s;;
  
}

#signup-section button:nth-child(1) {
  background-color: grey;
  cursor:pointer;
}

.btn-check-ok {
  cursor:pointer;
  background-color: rgb(45, 45, 196);
}

.btn-check-no {
  cursor:not-allowed;
  background-color: grey;
}

.signup-btn-div {
  position:absolute; display: flex; bottom:10%; left: 50%; justify-content: space-between;
  width: 600px;
  transform:translateX(-50%)
}

#signup-section  input {
  width: 0; height: 50px;
  margin: 20px 0;
  border: none; border-bottom: 1px solid grey;
  animation: inputAni 0.3s ease-in forwards;
  animation-delay: 0.5s;
  opacity: 0;
  outline:none;
}

@keyframes inputAni {
  to {
    width: 100%;
    opacity: 1;
  } 
}

.check-ok,.check-no {
  text-align: right;
  font-size: 0.8em;
  font-weight: bold;
  margin-top: -20px;
}
.check-ok {color:rgb(8, 250, 20);}

.check-no {color:red;}



</style>