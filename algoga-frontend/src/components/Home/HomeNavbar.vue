<template>
  <div id='home-navbar'>
    <nav>
      <div>        
        <h1 @click='homeToTop()'><span>//</span>ALGOGA</h1>
        <!-- <div>
          <div>first link</div>
          <div>second link</div>
          <div>third link</div>                   
        </div> -->
      </div>
      <div>
        <a href="#" @click="emitSign(1)">Signin</a>
        <a href="#" @click ="emitSign(2)">SignUp</a>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
    name : 'HomeNavbar',
    methods:{
      emitSign:function(status){        
        if (status === 1) {
          this.$emit("signin")
        } else {
          this.$emit("signup")
        }
      },
      homeToTop : function(){
          window.scrollTo({top: 0, behavior: 'smooth'});
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
    }
}
</script>

<style>

#home-navbar {    
  position:sticky;
  top: 0px;
  width: 95%;
  height: 60px;   
  margin:0px auto 0 auto;
  background-color: var(--back-color);  
  border-radius: 5px;  
  color: var(--font-color);
  z-index: 1000;
    
}

.nav-shadow {
  box-shadow: 0px 2px 5px var(--shadow-color);
}

#home-navbar > nav {
  display:flex;
  justify-content: space-between;
  align-items: center;
  width:80%;
  margin:0 auto;
}

#home-navbar > nav > div:nth-child(1) {
  /* background-image: url("../../assets/2.jpg"); */
  /* background-repeat: no-repeat; */
  display:flex;
  
}

#home-navbar > nav >div:nth-child(1) > h1 {
  font-style:italic;  
  margin-left: 20px;

}
#home-navbar > nav >div:nth-child(1) > h1 > span {
  color:var(--logo-color);
  font-weight: bold;
}

#home-navbar > nav >div:nth-child(1) > div {  
  display:flex;
  background-color: var(--back-color);
  align-items: center;  
  height:100%;
  margin: auto 0;
  cursor:pointer;
}

#home-navbar > nav >div:nth-child(1) > div > div {
  padding-left: 40px;
  
}

#home-navbar > nav > div:nth-child(2) > a{  
  color:var(--font-color);
  text-decoration: none;
  padding-right: 20px;
}



</style>