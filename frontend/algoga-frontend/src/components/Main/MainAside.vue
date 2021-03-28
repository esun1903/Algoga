<template>
  <div id="mainAside">
    <div id = 'profileBox'>
      <img id='profileImg' src="http://storage.enuri.info/pic_upload/knowbox2/202005/08362910620200507cd5549b2-9c1f-4447-aa00-72645ae3a069.jpg" alt="">
      <div id='userInfo'>
        <p id ='userId'>Unnamed</p>
        <p><span class='profileLink'>My blog</span><span class='profileLink'>My account</span></p>
      </div>
    </div>
    <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p> -->
    <div id ='userContent'>
      <transition name="fade" mode="out-in">
      <div v-if="asideContent" id ='summary-box'>
        <p class='text-center'>
          <span class='box-title'>Solved Summary</span>
          <span class='tooltip'>
            <i class="fas fa-question-circle"></i>
            <p class='tooltiptext'>너의 문제</p>
          </span>
        </p>
        <div id='graphBox'>
          <img id='userGraph' src="https://file.mk.co.kr/meet/neds/2017/08/image_readbot_2017_571580_15036508393005867.jpg" alt="">
        </div>
        <div id='problemSummary'>
          <div 
            v-for="(idx,problem) in solvedList"
            :key='idx'
          >
            <span>{{problem}} : {{solvedList[problem]}}</span>
          </div>
        </div>
        <p @click='asideContent = !asideContent' class='content-toggle'>recommend</p>
      </div>
      </transition>
      <transition name="fade" mode="out-in">
      <div v-if='!asideContent' id ='recommendBox'>
        <p class='text-center'>
          <span class='box-title'>Recommended Problem</span>
          <span class='tooltip'>
            <i class="fas fa-question-circle"></i>
            <p class='tooltiptext'>어떠한 방식을 통해 추천함</p>
          </span>
        </p>
        <p @click='asideContent = !asideContent'  class='content-toggle'>summary</p>      
      </div>
      </transition>
    </div>
  </div>
</template>

<script>

export default {
    name:"MainAside",
    data: function(){
      return{
        asideContent : true,
        solvedList: {
          'dfs' : 21,
          'bfs' : 16,
          'tree' : 4,
          'simulation' : 27,
          'dp' : 5,
          'string' : 20,
          'sorting' : 8,
        }
      }
    },
    methods : {

    }
}
</script>

<style>
p{
  margin: 0;
}
#mainAside{
  width: 400px;
  border-right: 1px solid rgba(61, 61, 61, 0.479);
}
#profileBox{
  display: flex;
  width: 100%;
  margin-top: 55px;
  padding-bottom: 25px;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(197, 195, 195, 0.205);
}
#profileImgBox{
  padding-top: 40px;
}
#profileImg{
  width: 22%;
  border-radius: 50%;
  margin-left: 2em;
}
#userId{
  font-size: 1.8rem;
  margin-top: 10px;
  font-weight: bold;
  margin-right: 5rem;
}
#userId + p{
  margin-top: 6px;
  margin-left: 3rem;
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
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to{
  opacity: 0;
}
</style>