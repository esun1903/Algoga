<template>
  <div id ='review'>
    <div id='reviewToggle' @click='toggle = !toggle'>
      <div>
        <span id='langIcon'><i :class='iconClass'></i></span><span>{{review.language}}</span>
        <img id='userImg' :src="review.profile" alt="">
        <span>{{review.writer}}</span>
      </div>
      <div>
        <span><i class="fas fa-thumbs-up"></i>{{review.like}}</span>
        <span>{{review.date}}</span>
      </div>
    </div>
    <transition name='slide'>
      <div id='userBoard' v-if="toggle">

      </div>
    </transition>  
  </div>
</template>

<script>
export default {
  name : 'review',
  data : function(){
    return{
      toggle : false,
      iconClass : '',
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
    if(this.review.language ==='파이썬'){
      this.iconClass= 'fab fa-python'
    }else if(this.review.language === '자바'){
      this.iconClass= 'fab fa-java'
    }else if(this.review.language === '자바스크립트'){
      this.iconClass= 'fab fa-js'
    }else{
      this.iconClass= 'fas fa-code'
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
  border-bottom: 0.5px solid #354673;
}
#reviewToggle:hover{
  cursor: pointer;
  background-color: rgba(236, 236, 236, 0.568);
}
#userImg{
  height: 40px;
}
#userBoard{
  width: 80%;
}
#userBoard{
  width: 100%;
  height: 30vh;
  background-color: red;
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