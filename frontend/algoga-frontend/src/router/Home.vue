<template>
  <div id='home'> 
      <HomeNavbar />
      <h1>Hello</h1>
  </div>
</template>

<script>
import HomeNavbar from '@/components/Home/HomeNavbar'


export default {
    name : 'Home',
    components : {
      HomeNavbar,
    },
}
</script>

<style>
#home{
  height:1000vh
}

</style>