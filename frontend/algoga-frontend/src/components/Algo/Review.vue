<template>
  <div id ='review'>
    <div id='reviewToggle' @click='toggle = !toggle'>
      <div>
        <span>Writer :</span>
        <img id='userImg' src="../../assets/userNull.png" alt="">
        <span>{{review.writer}}</span>
        <span id='thumbIcon'><i class="fas fa-thumbs-up"></i>{{review.like_cnt}}</span>
        <span id='langIcon'><i :class='iconClass'></i></span><span>{{review.language}}</span>
        <!-- <img id='userImg' :src="review.profile" alt=""> -->
      </div>
      <div>
        <span id='registeredDate'>{{review.register_date | dateChange}}</span>
      </div>
    </div>
    <transition name='slide'>
      <div id='userBoard' v-if="toggle">
        <CodeBoardDetail />
      </div>
    </transition>  
  </div>
</template>

<script>
// import CodeHighlighter from "@/components/Main/CodeHighlighter"
// import CodeBoardComment from "@/components/Main/CodeBoardComment"
import axios from 'axios'
import CodeBoardDetail from '@/components/Algo/CodeBoardDetail'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
// const SERVER_URL = 'http://j4a302.p.ssafy.io'

export default {
  name : 'review',
  components : {
    CodeBoardDetail
  },
  data : function(){
    return{
      toggle : false,
      iconClass : '',
      commentList : [],
    }
  },
  props : {
    review : {
      type : Object,
    }
  },
  methods : {
  },
  async created(){
    if(this.review.language ==="PYTHON"){
      this.iconClass= 'fab fa-python'
    }else if(this.review.language === 'JAVA'){
      this.iconClass= 'fab fa-java'
    }else if(this.review.language === 'JAVASCRIPT'){
      this.iconClass= 'fab fa-js'
    }else{
      this.iconClass= 'fas fa-code'
    }
    await axios.get(`${SERVER_URL}/apps/v1/commentList/${this.review.seq}`)
      .then(res =>{
        this.commentList = res.data
      })
      .catch((err)=>{
        console.log(err)
      })    
    await axios.get(`${SERVER_URL}/apps/v1/userInfo/${this.review.user_seq}`)
      .then(res =>{
        this.review.writer = res.data.nickname
        this.review.profile = res.data.profile_image
      })
      .catch((err)=>{
        console.log(err)
      })    
  },
  filters : {
    dateChange : function(date){
      return date.split('T')[0]
    }
  }
}
</script>

<style>
#reviewToggle{
  display: flex;
  width: 100%;
  justify-content: space-between;
  height: 50px;
  align-items: center;
  border-radius: 10px;
  background-color: #35467309;
  margin-top: 5px;
  border-bottom: 0.1px solid #354673;
}
#reviewToggle:hover{
  cursor: pointer;
  background-color: rgba(236, 236, 236, 0.568);
}
#reviewToggle > div:nth-child(1){
  display: flex;
  align-items: center;
}
#thumbIcon{
  margin : 0 8px 0 20px
}
#thumbIcon > svg{
  margin-right: 8px;
}
#langIcon{
  margin : 0 8px 0 20px
}
#langIcon > svg{
  margin-right: 4px;
}
#reviewToggle > div:nth-child(1) > span:nth-child(1){
  margin-left: 20px;
}
#userImg{
  height: 40px;
}
#userBoard{
  width: 100%;
  margin: 0 auto;
  height: fit-content;
}
#code-highlighter{
  width: 80%;
}
#code-board-comment{
  width: 100%;
  height: 40px;
  display: block;
}
#registeredDate{
  margin-right: 30px;
}





/* 슬라이드 */
.slide-enter-active {
  -moz-transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  -o-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -moz-transition-timing-function: ease-in;
  -webkit-transition-timing-function: ease-in;
  -o-transition-timing-function: ease-in;
  transition-timing-function: ease-in;
}

.slide-leave-active {
  -moz-transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  -o-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -moz-transition-timing-function: ease-out;
  -webkit-transition-timing-function: ease-out;
  -o-transition-timing-function: ease-out;
  transition-timing-function: ease-out;
}

.slide-enter-to, .slide-leave {
  max-height: 480px;
  overflow: hidden;
}

.slide-enter, .slide-leave-to {
  overflow: hidden;
  max-height: 0;
}
</style>