<template>
  <div id='home'> 
      <HomeNavbar @signup = "signupClick" @signin = "loginClick"/>
      <h1>Hello</h1>
      <button @click="loginClick" id='loginModalBtn'>로그인</button>
      <Login
        v-if='loginClicked'
        @closed ='loginClick'
      />
      <Signup
        v-if ="signupClicked"
        @closed = "signupClick"
      />
  </div>
</template>

<script>
import HomeNavbar from '@/components/Home/HomeNavbar'
import Login from '@/components/Home/Login'
import Signup from '@/components/Home/Signup'

export default {
    name : 'Home',
    components : {
      HomeNavbar,
      Login,
      Signup,
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
  }
}
</script>

<style>


</style>