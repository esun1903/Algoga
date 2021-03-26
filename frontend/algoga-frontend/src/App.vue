<template>
  <div id="app">
    <router-view /> 
    <!-- <ModeBtn /> -->
  </div>
</template>

<script>
// import ModeBtn from "@/components/ModeBtn"


export default {
  name: 'App',
  components: {
    // ModeBtn,
  }
}
</script>

<style>
:root {
  --font-color: black;
  --back-color: white;
  --shadow-color: rgba(0,0,0,0.5);
  --test-color: red;

}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;  
  background-color: var(--back-color);
}
.text-center{
  text-align: center;
}
</style>
