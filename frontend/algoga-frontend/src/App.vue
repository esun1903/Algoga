<template>
  <div id="app">
    <router-view /> 
    <ModeBtn v-if='modeBtn' />
  </div>
</template>

<script>
import ModeBtn from "@/components/ModeBtn"

export default {
  name: 'App',
  components: {
    ModeBtn,
  },
  data(){
    return {
      modeBtn:true
    }
  },
  methods:{
    checkJWT:function(){
      const jwt = localStorage.getItem('JWT')      
      if (!jwt) {
        this.$router.push({name:'Home'})
      }

    },
    routerCheck:function(){      
      if (this.$route.path =='/') {
        this.modeBtn = false
        return
      }
      this.modeBtn = true
    }
  },
  created(){
    window.addEventListener('click',function(event){
      let d = document.createElement('div')
      d.className = 'clickEffect'
      d.style.top = event.clientY + 'px'; d.style.left = event.clientX+'px';
      d.addEventListener('animationend',function(){
          d.parentElement.removeChild(d)
        })
      document.body.appendChild(d)

    })
    this.checkJWT()
    this.routerCheck()
  },
  watch:{
    $route(to,from){
      if (to.path!==from.path){
        this.checkJWT()
        this.routerCheck()
      }
    }
  }

}
</script>

<style>
:root {
  --font-color: black;
  --font-color2:white;
  --back-color: white;
  --signup-line: brown;
  --shadow-color: rgba(0,0,0,0.5);
  --test-color: red;
  --logo-color: rgb(252, 69, 69);
  --oneDay-back: rgba(0,0,0,0.1);
}

@keyframes clickEffect{
  0%{
    opacity:1;
    width:0.5em; height:0.5em;
    margin: -0.25em;
    border-width: 0.5em;
  }
  100%{
    opacity:0.2;
    width:3em; height:3em;
    margin: -1.5em;
    border-width: 0.05em;
  }
}

input::placeholder {opacity: 0.5;}





#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: Hack,Avenir;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;  
  background-color: var(--back-color);
  transition: 0.3s; 
  min-height: 100vh;
  
}

.btn-font {
  font-family: Hack,Avenir;
}

.text-center{
  text-align: center;
}

.clickEffect {
  position:fixed;
  box-sizing: border-box;
  border-style: solid;
  border-color: var(--shadow-color);
  border-radius: 50%;
  animation:clickEffect 0.4s ease-out;
  z-index:99999;
}

</style>
