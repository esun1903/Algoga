<template>
  <div id='home'> 
      <HomeNavbar @signup = "signupClick" @signin = "loginClick"/>
      <Login v-if='loginClicked' @closed ='loginClick'/>
      <Signup v-if ="signupClicked" @closed = "signupClick"/>
      <!-- <button @click="loginClick" id='loginModalBtn'>로그인</button> -->
      <FirstHome />
      <Home2nd />

      <footer>asd</footer>

  </div>
</template>

<script>
import HomeNavbar from '@/components/Home/HomeNavbar'
import Login from '@/components/Home/Login'
import Signup from '@/components/Home/Signup'
import FirstHome from '@/components/Home/FirstHome'
import Home2nd from '@/components/Home/Home2nd'

export default {
  name : 'Home',
  components : {
    HomeNavbar,
    Login,
    Signup,
    FirstHome,
    Home2nd,
  },
  data : function(){
    return{
      loginClicked : false,
      signupClicked: false,
    }
  },
  methods :{
    loginClick : function(){
      this.loginClicked = !this.loginClicked
    },
    signupClick: function(){
      this.signupClicked = !this.signupClicked

    }
  },
  created(){
    let jwt = localStorage.getItem('JWT')
    let email = localStorage.getItem('email')
    if (jwt&&email) {
      this.$router.push({name:'Main',params:{'nickname':email}})
    }
  }
  
}
</script>

<style>

#home> footer {
  height:100vh
}
</style>