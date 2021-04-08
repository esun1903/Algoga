<template>
  <div id='problem'>
    <MainNavbar />
    <div>
      <h1 id='algoTitle'><span>{{algo.number}}. {{algo.name}}</span></h1>
      <div @click='goBack()'>
        <span><i class="fas fa-arrow-left"></i></span>
      </div>
    </div>
    <div id='explainSection'>

      <img :src="imgsrc" alt="">
      <div>
        <p>Lv.{{algo.level}} <span id='emojiExplain'></span></p>
        <p>{{algo.algorithms}}</p>
        <p>정답률 : {{algo.correct_rate}} %</p> 
        <p>350000명 중 {{algo.correct_user}}명이 풀었어요!</p> 
      </div>
    </div>
    <Preview
      :link = bojLink
      :title = bojTitle
      :description = bojDescription
    />
    
    <ReviewsList
      :algoSeq = algo.seq
    />
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
          imgsrc : ''
      }
    },
    created(){
        this.algo = this.$route.params
    },
    mounted(){
      const emojiExplain = document.querySelector('#emojiExplain')
      if(this.algo.level <=3 ){
        this.imgsrc = require('@/assets/positive.png')
        emojiExplain.innerText = 'Easy'
      }else if(this.algo.level <=7 ){
        this.imgsrc = require('@/assets/happy.png')
        emojiExplain.innerText = 'So So'
      }else{
        this.imgsrc = require('@/assets/anxiety.png')
        emojiExplain.innerText = 'Very Hard'
      }

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
  padding: 30px 0;
  text-align: center;
  margin: 40px 20% 40px 20%;
  box-shadow: 0 1px 0 0 rgb(37 40 47 / 30%);
}
#problem > div > h1 > span{
  margin-bottom: 40px;
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
  cursor: pointer;
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
#explainSection{
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin: 40px auto;
  width: 40%;
  /* border: 1px solid black; */
}
#explainSection > img{
  width: 150px;
  height: 150px;
}

#explainSection > div > p:nth-child(1){
  font-size: 1.5rem;
}
#explainSection > div > p:nth-child(2){
  margin-bottom: 10px;
}
#explainSection > div > p:nth-child(3){
  font-size : 1.2rem
}
</style>