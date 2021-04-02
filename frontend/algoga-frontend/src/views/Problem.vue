<template>
  <div id='problem'>
    <MainNavbar />
    <h1>{{algo.name}}</h1>
    <Preview
      :link = bojLink
      :title = bojTitle
      :description = bojDescription
    />
    <Reviews />
  </div>
</template>

<script>
import MainNavbar from '@/components/Main/MainNavbar'
import Preview from '@/components/Algo/Preview'
import Reviews from '@/components/Algo/Reviews'

export default {
    name : 'Problem',
    components : {
        MainNavbar,
        Preview,
        Reviews,
    },
    data : function(){
        return{
          algo : {
              seq: 0,
              number: 0,
              name: "",
              correct_user: 0,
              submission_cnt: 0,
              correct_rate: 0,
              level: 0,
              avg_try: 0
            },
        }
    },
    created(){
        this.algo = this.$route.params
    },
    computed : {
      bojLink : function(){
        return `https://www.acmicpc.net/problem/${this.algo.number}`
      },
      bojTitle : function(){
        return `[${this.algo.number}] ${this.algo.name}`
      },
      bojDescription : function(){
        return `Lv.${this.algo.level} correct_rate : ${this.algo.correct_rate}%`
      }
    },
}
</script>

<style>

</style>