<template>
  <div id='reviews'>
    <div>
      <span>등록된 풀이 보기</span>
      <div @click='chageToggle()' id='icon-container'>
        <span id='toggleIcon'>
          <i class="fas fa-sort-down"></i>
        </span>
      </div>
    </div>
    <transition name='slide'>
      <h1 v-if="toggle" >dasdas</h1>
    </transition>
  </div>
</template>

<script>
export default {
  name : 'Reviews',
  data : function(){
    return{
      toggle : false,
    }
  },
  methods : {
    chageToggle : function(){
      let toggleSection = document.querySelector('#toggleIcon')
      if(this.toggle){
        toggleSection.innerHTML = '<i class="fas fa-sort-down"></i>'
      }else{
        toggleSection.innerHTML = '<i class="fas fa-sort-up"></i>'
      }
      this.toggle = !this.toggle
    }
  },
  
}
</script>

<style>
#reviews{
  width: 70%;
  margin: 0 auto;
}
#reviews > div:nth-child(1){
  width: 100%;
  display: flex;
  justify-content: space-between;
  height: 8vh;
  border-radius: 10px;
  background-color: #05106638;
  align-items: center;
}
#reviews > div:nth-child(1) > span:nth-child(1){
  margin: 0 0 0 5%;
}
#icon-container{
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  padding: 6px;
  font-size: 1rem;
  height: 40px;
  width: 40px;
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
  margin: 0 10% 0 0;
}
#icon-container:hover{
  cursor: pointer;
  background-color: rgb(241, 241, 241);
  transition: all 0.5s;
}
#icon-container>span{
  text-align: center;
  margin: auto;
  font-size: 22px;
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