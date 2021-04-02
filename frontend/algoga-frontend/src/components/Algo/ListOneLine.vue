<template>
  <tr @click='goToAlgo(algo)' id='listOneLine'>
    <th><span>no.</span>{{algo.seq}}</th>
    <th><span>lv.</span>{{algo.level}}</th>
    <th>type</th>
    <th>{{algo.name}}</th>
    <th>{{algo.correct_rate | round}}%</th>
    <th>{{algo.correct_user}}</th>
  </tr>
</template>

<script>
export default {
  name : 'ListOneLine',
  props : {
    algo : {
      type : Object,
    },
  },
  created(){
    console.log(this.algo)
  },
  filters :{
    round : function(v){
      return Math.ceil(10*v) / 10;
    }
  },
  methods : {
    goToAlgo : function(algo){
      console.log(algo.seq)
      this.$router.push({
        name : 'Problem',
        params : algo,
        query : {no : algo.seq}
      })
    },    
  }
}
</script>

<style>

</style>