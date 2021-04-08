<template>
  <div id ='review'>
    <div id='reviewToggle' @click='toggle = !toggle'>
      <div>
        <div>
          <span>Writer :</span>
          <div id='imgBox'>
            <img id='userImg' :src="imgSrc" alt="">
          </div>
          <span>{{writerName}}</span>
        </div>
        <div>
          <span id='thumbIcon'><i class="fas fa-thumbs-up"></i>{{review.like_cnt}}</span>
        </div>
        <div>
          <span id='langIcon'><i :class='iconClass'></i></span><span>{{review.language}}</span>
        </div>
        <!-- <img id='userImg' :src="review.profile" alt=""> -->
      </div>
      <div>
        <span id='registeredDate'>{{review.register_date | dateChange}}</span>
      </div>
    </div>
    <transition name='slide'>
      <div id='userBoard' v-if="toggle">
        <CodeBoardDetail
          :code_board_seq = 'review.seq'
        />
      </div>
    </transition>  
  </div>
</template>

<script>
import axios from 'axios'
import CodeBoardDetail from '@/components/Algo/CodeBoardDetail'
const SERVER_URL = 'http://j4a302.p.ssafy.io'


export default {
  name : 'review',
  components : {
    CodeBoardDetail
  },
  data : function(){
    return{
      toggle : false,
      iconClass : '',
      code_board_seq : '',
      writerName : '',
      imgSrc : '',
    }
  },
  props : {
    review : {
      type : Object,
    }
  },
  methods : {
  },
  created(){
    if(this.review.language ==="PYTHON"){
      this.iconClass= 'fab fa-python'
    }else if(this.review.language === 'JAVA'){
      this.iconClass= 'fab fa-java'
    }else if(this.review.language === 'JAVASCRIPT'){
      this.iconClass= 'fab fa-js'
    }else{
      this.iconClass= 'fas fa-code'
    }
    this.writerName = ''
    axios.get(`${SERVER_URL}/apps/v1/userInfo/${this.review.user_seq}`)
      .then(res =>{
        this.writerName = res.data.nickname
        this.imgSrc = res.data.profile_image
      })
      .catch((err)=>{
        console.log(err)
      })    
  },
  filters : {
    dateChange : function(date){
      return date.split('T')[0]
    }
  },
  computed : {
    profileImage(){
      return (data) => {      
        return data.profile_image
      }
    },
  }
}
</script>

<style>
#reviewToggle{
  display: flex;
  width: 100%;
  justify-content: space-between;
  height: 60px;
  align-items: center;
  border-radius: 10px;
  background-color: #35467309;
  margin-top: 5px;
  border-bottom: 0.1px solid #354673;
  font-size: 1rem;
}
#reviewToggle:hover{
  cursor: pointer;
  background-color: rgba(236, 236, 236, 0.568);
}
#reviewToggle > div:nth-child(1){
  width: 100%;
  display: flex;
  align-items: center;
}
#reviewToggle > div:nth-child(2){
  width: 15%;
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
#reviewToggle > div:nth-child(1) > div:nth-child(1){
  margin-left: 20px;
  display: flex;
  align-items: center;
  width: 20%;
  min-width: 120px;
}
#imgBox{
  width: 40px;
  overflow: hidden;
  border-radius: 12px;
  margin: 0 5px;
  text-align: center;
}
#userImg{
  width: 40px;
  height: 40px;
}
#userBoard{
  width: 100%;
  margin: 40px auto;
}
#code-highlighter{
  width: 80%;
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