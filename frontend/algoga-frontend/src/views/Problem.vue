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
      <div>
        <GChart
          type="ColumnChart"
          :data = crdata
          :options = chartOptions
        />
      </div>
      <div>
        <p>Lv.{{algo.level}}</p>
        <div id='emoji'></div>
        <p id='emojiExplain'></p>
      </div>
      <div>
        <GChart
          type="PieChart"
          :data = crdata2
          :options = chartOptions2
        />
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
import { GChart } from 'vue-google-charts'

export default {
    name : 'Problem',
    components : {
        MainNavbar,
        Preview,
        ReviewsList,
        GChart
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
          crdata : [],
          chartOptions: {
            chart: {
            }
          },
          crdata2 :[],
          chartOptions2: {
            chart: {
            }
          },
      }
    },
    created(){
        this.algo = this.$route.params
        this.chartType = 'ColumnChart'
        const newData = []
        newData.push(['columChart','correct_user','submission_cnt'])
        newData.push([`${this.algo.correct_rate}%`,this.algo.correct_user, this.algo.submission_cnt])
        this.crdata = newData

        const newData2 =[]
        newData.push(['PieChart','correct_user','all_user'])
        newData.push([`${this.algo.correct_rate}%`,this.algo.correct_user, 34900])
        this.crdata = newData2
        // console.log(this.crdata)
    },
    mounted(){
      const emoji = document.querySelector('#emoji')
      const emojiExplain = document.querySelector('#emojiExplain')
      if(this.algo.level <=3 ){
        emoji.innerHTML = '<i class="far fa-laugh-beam"></i>'
        emojiExplain.innerText = 'Easy'
        emoji.style = 'color : yellow;'
      }else if(this.algo.level <=7 ){
        emoji.innerHTML = '<i class="far fa-smile"></i>'
        emoji.style = 'color : green;'
        emojiExplain.innerText = 'So So'
      }else{
        emoji.innerHTML = '<i class="far fa-tired"></i>'
        emoji.style = 'color : red;'
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
  padding: 0 10%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 40px 0;
}
#explainSection > div:nth-child(1){
  width: 25%;
}
#explainSection > div:nth-child(2){
  text-align: center;
}
#emoji{
  font-size: 6rem;
}
</style>