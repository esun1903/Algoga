<template>
  <tr @click='goToAlgo(algo)' id='listOneLine'>
    <th><span>no.</span>{{algo.seq}}</th>
    <th><span>lv.</span>{{algo.level}}</th>
    <th>{{algo.algorithms | lastType}}</th>
    <th>{{algo.name}}</th>
    <th>{{algo.submission_cnt}}</th>
    <th>{{algo.correct_rate | round}}%</th>
    <th>{{algo.review_count}}</th>
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
  },
  filters :{
    round : function(v){
      return Math.ceil(10*v) / 10;
    },
    lastType : function(str){
      let splited = str.split(',')
      return splited[splited.length - 1]
    }
  },
  methods : {
    goToAlgo : function(algo){
      this.$router.push({
        name : 'Problem',
        params : algo,
        query : {no : algo.seq}
      })
    },    
  },
}
</script>

<style>

</style>