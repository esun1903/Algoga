<template>
  <div id='problem'>
    <MainNavbar />
    <div>
      <h1>{{algo.name}}</h1>
      <div @click='goBack()'>
        <span><i class="fas fa-arrow-left"></i></span>
      </div>
    </div>
    <Preview
      :link = bojLink
      :title = bojTitle
      :description = bojDescription
    />
    <ReviewsList />
  </div>
</template>

<script>
import MainNavbar from '@/components/Main/MainNavbar'
import Preview from '@/components/Algo/Preview'
import ReviewsList from '@/components/Algo/ReviewsList'

export default {
    name : 'Problem',
    components : {
        MainNavbar,
        Preview,
        ReviewsList,
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
    methods :{
      goBack : function(){
        window.history.back();
      }
    }
}
</script>

<style>
#problem > div{
  position: relative;
}
#problem > div > h1{
  text-align: center;
}
#problem > div > h1 + div{
  position: absolute;
  left: 10%;
  top: 50%;
  transform: translate(-50%,-50%);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  height: 40px;
  width: 40px;
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
}
#problem > div > h1 + div:hover{
  color: red;
}
#problem > div > h1 + div:active{
  box-shadow: -1px 0px 4px 0 rgb(0 0 0 / 40%);
  background-color: rgba(119, 136, 153, 0.089);
}
#problem > div > h1 + div > span{
  text-align: center;
  margin: auto;
  font-size: 22px;
}
</style>