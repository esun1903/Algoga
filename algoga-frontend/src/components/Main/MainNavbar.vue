<template>
  <div id='home-navbar' style='margin-bottom:50px'>
    <nav>
      <div>        
        <h1 @click='routerNav(0)'><span>//</span>ALGOGA</h1>
        <div>
          <div @click='routerNav(1)'>Problems</div>
          <div @click='routerNav(2)'>My Code</div>
          <div @click='routerNav(3)'>Follow</div>                   
        </div>
      </div>
      <div class='sign-out-btn' @click='signout'>
        <p>SignOut</p>
      </div>
    </nav>
  </div>
</template>

<script>

export default {
    name : 'MainNavbar',
    methods:{
      signout:function(){
        if (confirm('로그아웃 하시겠습니까?')===true){
          localStorage.removeItem('email')
          localStorage.removeItem('userNo')
          localStorage.removeItem('register_date')
          localStorage.removeItem('JWT')
          this.$router.push({name:'Home'})
        }
      },
      routerNav:function(idx){                
        if (idx === 0) {
          this.$router.push({name:'Main',params:{nickname:localStorage.getItem('email'),userno:localStorage.getItem('userNo')}})
        } else if (idx===1) {
          this.$router.push({name:'List'})
          } else if (idx===2) {
          this.$router.push({name:'Mycode'})
        } else {
          this.$router.push({name:'Follow'})
        }

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
  margin-right: 2%;
}
.sign-out-btn > p { margin-top: 5px;}

nav > div {cursor:pointer}
</style>