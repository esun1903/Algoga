<template>
  <div id="app">
    <router-view /> 
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {

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
  text-align: center;
  color: #2c3e50;  
}
</style>
