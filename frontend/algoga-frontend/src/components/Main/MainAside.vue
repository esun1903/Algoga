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
            <p class='tooltiptext'>너의 문제</p>
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
        <div class='transBtn' @click='asideContent = !asideContent'>
          <span><i class="fas fa-arrow-left"></i></span>
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
        <div class='transBtn' @click='asideContent = !asideContent'>
          <span><i class="fas fa-arrow-left"></i></span>
        </div>
      </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProfileBox from '@/components/Main/ProfileBox'
const SERVER_URL = 'http://j4a302.p.ssafy.io'
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
          hoverBorderWidth: 20
        },        
        data : [],
      }
    },
    methods : {
      profileUpdate:function(){
        this.$emit('profileUpdate')
        },
      reloadAlgos : function(){
        const userMail = localStorage.getItem('email')
        axios.post(`${SERVER_URL}/apps/v1/userInfoUpdate/${userMail}`)
          .then(()=>{
            console.log('리스트 갱신')
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

      await axios.get(`${SERVER_URL}/apps/v1/userTypeInfo/1`)
        .then(res => {
          let myList = new Array();
          myList.push(['Type','Number'])
          res.data.forEach(element => {
            myList.push([element.type_name, element.type_cnt])
          });
          // this.solvedList = myList
          // this.data.labels = Object.keys(myList)
          this.data = myList
          // console.log(this.data)
        })
        .catch(err=> {
          console.log(err)
        })
    },
}
</script>

<style>
p{
  margin: 0;
}
#mainAside{
  width: 400px;
  /* width: 80%;
  margin: 0 auto; */
  position:sticky;
  top:70px;
  border-right: 1px solid rgba(61, 61, 61, 0.479);
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
  translate: all 1s ease-out;
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
</style>