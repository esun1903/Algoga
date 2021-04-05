<template>
  <div id="main">
    <MainNavbar />
    <div>
      <div>
        <!-- feed -->
        <div v-show='!feedOpened'  @click="feedOpened = !feedOpened" id='feed-container'>
          <span id='feed-btn'>
            <i class="far fa-bell"></i>
          </span>
        </div>
        <transition name="slide-fade">
          <Feed
            v-show="feedOpened"
            @closeFeed='feedOpened = !feedOpened'
          />
        </transition>
      </div>
      <div id='main-content'>
        <div>
          <MainAside />
        </div>
        <section>
          챌린지 디브          

          <LogStudy @userData='userData' />
          <!-- history -->

          <History :dataHistory='dataHistory' :dataList='dataList' />

          <button @click='test'>TEST Button router to problemSolving</button>                    
        </section>
        
    
      </div>
    </div>

  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import LogStudy from "@/components/Main/LogStudy"
import History from "@/components/Main/History"
import MainAside from "@/components/Main/MainAside"
import Feed from "@/components/Main/Feed"

// import axios from "axios"


// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:"Main",
  components: {
      MainNavbar,
      LogStudy,
      History,
      MainAside,
      Feed
  },
  methods:{
    test:function(){
      this.$router.push({name:'Register'})
    },
    userData:function(data){
      let data1 = data.data1
      let data2 = data.data2
      data1.reverse()
      this.dataHistory = data1 
      this.dataList = data2     
    },
  },
  data : function(){
    return{
      feedOpened: false,
      teststring:'',
      dataHistory:[],
      dataList:[],
    }
  }

}
</script>

<style>
#main > div:nth-child(2){
  display: flex;
}
#main-content > section {
  width: 1000px;    
  margin: 20px 20px 20px 50px;
  
}
#main-content{
  display: flex;
  margin: 0 auto;
}
#feed-btn{
  border-radius: 50%;
  font-size: 30px;
}
#feed-container:hover{
  cursor: pointer;
  background-color: rgb(241, 241, 241);
  transition: all 0.5s;
}
#feed-container{
  display: flex;
  position: fixed;
  justify-content: center;
  align-items: center;
  bottom: 100px;
  right: 100px;
  border-radius: 50%;
  padding: 6px;
  font-size: 1rem;
  height: 40px;
  width: 40px;
  justify-content: space-between;
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
}
#feed-container > span{
  text-align: center;
  margin: auto;
  font-size: 22px;
}
.slide-fade-enter-active {
  transition: all .1s ease;
}
.slide-fade-leave-active {
  transition: all .1s ease;
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}

@media screen and (max-width:1100px) {
  #main-content {
    display: block;
  }
  #main-content > section{
    margin: 0 auto;
  }
}

</style>
