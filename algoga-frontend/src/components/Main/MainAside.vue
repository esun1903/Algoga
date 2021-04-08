<template>
  <div id="mainAside">

    <ProfileBox @profileUpdate='profileUpdate'/>
    <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p> -->
    <div id ='userContent'>
      <transition name="fade" mode="out-in">
      <div class='contentBox' v-if="asideContent" id ='summary-box'>
        <p class='text-center'>
          <span class='box-title'>Solved Summary</span>
          <span class='tooltip'>
            <i class="fas fa-question-circle"></i>
            <p class='tooltiptext'>당신의 문제 풀이를 분석하는 공간입니다.</p>
          </span>
        </p>
        <div id='graphBox'>
          <Chart :chartdata="data" :options="chartOptions" />
        </div>
        <div id='problemSummary'>
          <div 
            v-for="(idx,problem) in solvedList"
            :key='idx'
          >
            <span>{{problem}} : {{solvedList[problem]}}</span>
          </div>
        </div>
          <p id='explain'><span>{{user.nickname}}</span>님은 '<span>{{mostSolved}}</span>' 유형을 가장 많이 풀었고,<span id='sectionStart'>『</span></p>
          <p>'<span>{{leastSolved}}</span>' 유형의 문제 풀이가 필요합니다.<span id='sectionEnd'>』</span></p>
          
          
        <div v-show="isMine" class='transTxt' @click='asideContent = !asideContent'>
          <span>> Get Algorithm Recommendation</span>
        </div>
      </div>
      </transition>
      <transition name="fade" mode="out-in">
      <div class='contentBox' v-if='!asideContent' id ='recommendBox'>
        <p class='text-center'>
          <span class='box-title'>Alogorithms For You</span> 
          <span class='tooltip'>
            <i class="fas fa-question-circle"></i>
            <p class='tooltiptext'>맞은 문제와 틀린 문제를 분석하여 추천</p>
          </span>
          <span @click='reloadAlgos()' id='refreshIcon'><i class="fas fa-retweet"></i></span>
        </p>
        <Recommend />
        <div class='transTxt' @click='asideContent = !asideContent'>
          <span>> Back to Summary</span>
        </div>
      </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://j4a302.p.ssafy.io'
import ProfileBox from '@/components/Main/ProfileBox'
import Chart from '@/components/Main/Chart'
import Recommend from '@/components/Main/Recommend'

export default {
    name:"MainAside",
    components : {
      Chart,
      ProfileBox,
      Recommend
    },
    data: function(){
      return{
        asideContent : true,
        userNo : 1,
        solvedList: [],
        user : {},
        chartOptions: {
          hoverBorderWidth: 20,
          width : 400,
          height : 300,
          is3D: true,
          sliceVisibilityThreshold: .02,
          chartArea:{left:0,top:40,width:'100%',height:'100%'},
          fontName : 'Hack',
          legend : {position :'labeled', textStyle: {color: 'black'}},
          colors : [
            '#FF6666', '#99CCFF', '#CCFF99', '#FFFF99','#FF9966', '#66FFCC', 
          ],
          tooltip : {textStyle: {color: 'black'}, showColorCode: true},
          pieSliceTextStyle : {color: 'black', fontName: 'Hack',fontSize: 14},
          pieSliceBorderColor : 'white',
        },        
        data : [],
        mostSolved : '',
        leastSolved : '',
      }
    },
    methods : {
      profileUpdate:function(){
        this.$emit('profileUpdate')
        },
      reloadAlgos : function(){
        axios.get(`${SERVER_URL}/apps/v1/userProblem/${this.userNo}`)
          .then(()=>{            
            window.location.reload()
          })
          .catch(err=>{
            console.log(err)
          })
      }
    },
    async created(){
      this.userNo = localStorage.getItem('userNo')
      await axios.get(`${SERVER_URL}/apps/v1/userInfo/${this.userNo}`)
        .then(res => {
          this.user = res.data
        })
        .catch(err => {
          console.log(err)
        })

      await axios.get(`${SERVER_URL}/apps/v1/userTypeInfo/${this.userNo}`)
        .then(res => {
          let myList = new Array();
          myList.push(['Type','Number'])
          res.data.forEach(element => {
            myList.push([element.type_name, element.type_cnt])
          });
          this.data = myList
          this.mostSolved = this.data[1][0]
          this.leastSolved = this.data[this.data.length -1][0]
        })
        .catch(err=> {
          console.log(err)
        })
    },
    computed : {
      isMine : function(){
        const user1 = localStorage.getItem('userNo')
        var url = window.location.href
        if(url ==='http://j4a302.p.ssafy.io/'){
          return true
        }
        const userA = url.split('/')
        const user2 = userA[userA.length -1 ]
        if(user1 == user2){
          return true
        }else{
          return false
        }
      }
    }
}
</script>

<style>
p{
  margin: 0;
}
#mainAside{
  width: 400px;
  position:sticky;
  top:70px;
  /* border-right: 1px solid rgba(61, 61, 61, 0.479); */
}

#profileImgBox{
  padding-top: 40px;
}


#userContent{
  width: 100%;
  padding-top: 40px;
}
#summary-box{
  width: 100%;
}
#userGraph{
  width: calc(100% - 40px);
}
.profileLink{
  font-size: 0.8rem;
  margin-right: 8px;
}
.profileLink:hover{
  color: red;
  cursor: pointer;
  text-decoration-line: underline;
}
.box-title{
  font-size: 1.5rem;
}
#graphBox{
  text-align: center;
  margin-top: 30px;
  box-shadow: 0 -1px 0 0 rgb(37 40 47 / 10%);
}
.tooltip {
  position: absolute;
  margin-left: 6px;
  font-size: 12px;
  color: rgb(126, 126, 126);
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  position: absolute;
  z-index: 1;
  bottom: 150%;
  left: 50%;
  margin-left: -60px;
}

.tooltip .tooltiptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: black transparent transparent transparent;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}
#problemSummary{
  margin: 20px 40px;
  box-sizing: content-box;
}
.content-toggle{
  float: right;
}
.fade-enter-active,
.fade-leave-enter {
    transform: translateX(0);
    transition: all .3s linear;
}
.fade-enter,
.fade-leave-to {
    transform: translateX(-100%);
}

@media screen and (max-width:1100px) {
  #mainAside{
    width: 100%;
    margin: 0 auto; 
    position:sticky;
    top:70px;  
  }
}
#refreshIcon{
  margin : 5px 0 0 40px;
}
#refreshIcon:hover{
  cursor: pointer;
  color: red;
}
.transBtn{
  position: absolute;
  left: -14%;
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
.transBtn:hover{
  color: red;
  cursor: pointer;
}
.transBtn:active{
  box-shadow: -1px 0px 4px 0 rgb(0 0 0 / 40%);
  background-color: rgba(119, 136, 153, 0.089);
}
.transBtn> span{
  text-align: center;
  margin: auto;
  font-size: 22px;
}
.contentBox{
  position: relative;
}
.transTxt{
  text-align: center;
  font-size: 1.1rem;
  box-shadow: -1px 0px 4px 0 rgb(0 0 0 / 60%);
  margin: 60px 20px 0 0;
  padding: 20px 10px;
}
.transTxt:hover{
  cursor: pointer;
  color: #C84160;
  background-color: rgba(241, 241, 241, 0.521);
}

#explain{
  font-size: 0.8rem;
  position: relative;
  white-space: nowrap;
}
#explain span{
  font-weight: 600;
  font-size: 1.1rem;
}
#explain + p{
  white-space: nowrap;
  font-size: 0.8rem;
  position: relative;
  margin-left: 30px;
}
#explain +p span{
  font-weight: 600;
  font-size: 1.1rem;
}
#sectionStart{
  position: absolute;
  top: -5px;
  left: -20px;
  font-size: 40px;
}
#sectionEnd{
  position: absolute;
  bottom: -5px;
  right: 5px;
  font-size: 40px;
}
@media screen and  (max-width : 1080px) {
  #userContent{
    text-align: center !important;
  }
  #graphBox > div > div> div > div{
    margin: 0 auto !important;
  }
}
</style>