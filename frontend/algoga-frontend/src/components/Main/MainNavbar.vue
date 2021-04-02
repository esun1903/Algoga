<template>
  <div id='home-navbar' style='margin-bottom:50px'>
    <nav>
      <div>        
        <h1><span>//</span>ALGOGA</h1>
        <div>
          <div>Problems</div>
          <div>Regist</div>
          <div>Community</div>                   
        </div>
      </div>
      <div class='sign-out-btn' @click='signout'>
        <p>SignOut</p>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name : 'MainNavbar',
    methods:{
      signout:function(){
        const user = localStorage.getItem('email')
        axios.get(`${SERVER_URL}/apps/v1/logout/${user}`)
          .then(res => {
            console.log(res)
          })
          .catch(err=>{
            console.log(err)
          })
      }
    },
    mounted: function(){
      window.addEventListener("scroll",function(){                
        if (window.scrollY > 10) {
          document.querySelector("#home-navbar").classList.add('nav-shadow')          
        } else {
          if (document.querySelector("#home-navbar").classList.contains('nav-shadow')){
            document.querySelector("#home-navbar").classList.remove('nav-shadow')
          } 
        }
      })
    },
    
}
</script>

<style>
.sign-out-btn{
  position:relative;
  border:1px solid grey;
  background-color: grey;
  border-radius: 10px;
  text-align: center;
  width:80px;
  height: 30px; 
  cursor:pointer;
  color:white;
  
}
.sign-out-btn > p { margin-top: 5px;}
</style>