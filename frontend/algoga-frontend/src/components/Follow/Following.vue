<template>
  <div id="follow-comp">
    <div class="person-div" v-for="(person,idx) in followingList" :key="idx">
      {{person}}

    </div>
  </div>
</template>

<script>
export default {
  name:'Following',
  props:{
    followingList:Array,
  }
}
</script>

<style>

</style>