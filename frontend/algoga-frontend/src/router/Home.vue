<template>
  <div id='home'> 
      <HomeNavbar />
      <h1>Hello</h1>
      <button @click="loginClick" id='loginModalBtn'>로그인</button>
      <Login
        v-if='loginClicked'
        @closed ='loginClick'
      />
  </div>
</template>

<script>
import HomeNavbar from '@/components/Home/HomeNavbar'
import Login from '@/components/Home/Login'

export default {
    name : 'Home',
    components : {
      HomeNavbar,
      Login,
    },
    data : function(){
      return{
        loginClicked : false
      }
    },
    methods :{
      loginClick : function(){
        this.loginClicked = !this.loginClicked
      },
  }
}
</script>

<style>
#home{
  height:1000vh
}

</style>