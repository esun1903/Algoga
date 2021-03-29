<template>
  <div id="register">
    <MainNavbar />
    <RegisterProblem />
    
  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import RegisterProblem from "@/components/Main/RegisterProblem"


export default {
    name:"Register",
    components: {
      MainNavbar,
      RegisterProblem,
    },

}
</script>

<style>

</style>