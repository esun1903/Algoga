<template>
  <div id="follow-comp">
    <div class="person-div" v-for="(person,idx) in followerList" :key="idx">
      <img :src="profileImage(person)" alt="" height='100px' width='100px'>
      
      {{person}}

    </div>
  </div>
</template>

<script>
export default {
  name:'Follower',
  props:{
    followerList:Array,
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
  mounted(){
    console.log(this.followerList)
  }
}
</script>

<style>

</style>