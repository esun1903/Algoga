<template>
  <div id='main-navbar'>
    position check

  </div>
</template>

<script>
export default {
    name : 'MainNavbar',
    mounted: function(){
      window.addEventListener("scroll",function(){                
        if (window.scrollY > 10) {
          document.querySelector("#main-navbar").classList.add('nav-shadow')          
        } else {
          if (document.querySelector("#main-navbar").classList.contains('nav-shadow')){
            document.querySelector("#main-navbar").classList.remove('nav-shadow')
          } 
        }
      })
    }
}
</script>

<style>
#main-navbar {
  position:sticky;
  top: 0px;
  width: 80vw;
  height: 60px;   
  margin:10px auto 0 auto;
  background-color: var(--back-color);  
  border-radius: 5px; 
  background-color: var(--test-color);
}

</style>