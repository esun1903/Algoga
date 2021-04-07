<template>
  <div id="follow-comp">
    <div class="person-div" v-for="(person,idx) in followingList" :key="idx">
      {{person}}
      <img :src="profileImage(person)" alt="" height='100px' width='100px'>

    </div>
  </div>
</template>

<script>
export default {
  name:'Following',
  props:{
    followingList:Array,
},
  computed:{
    profileImage(){
      return (person) => {
        console.log(person)
        console.log(`require("${person.profile_image}")`)
        
        
        return `'require("${person.profile_image}")'`
      }
    }
  },
}
</script>

<style>

</style>