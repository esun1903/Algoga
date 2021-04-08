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
          <MainAside @profileUpdate = 'profileUpdate' />
        </div>
        <section>   
          <div class='main-box'>
            <div class='log-header'>
              <h2>Study Log</h2>  
              <button class='register-btn btn-font' @click='routeRegister'>
                <i class="fas fa-signature"></i>
                CREATE
              </button>
            </div>
            <LogStudy @userData='userData' />
          </div>           
          <!-- history -->
          <div class='main-box'>
            <h2>History</h2>  
            <History :dataHistory='dataHistory' :dataList='dataList' />
          </div>

          <!-- <button @click='test'>TEST Button router to problemSolving</button>                     -->
        </section>
        
    
      </div>
    </div>
    <UserInfoUpdate v-if = 'userUpdate' @closeUpdate='closeUpdate' />
  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import LogStudy from "@/components/Main/LogStudy"
import History from "@/components/Main/History"
import MainAside from "@/components/Main/MainAside"
import UserInfoUpdate from "@/components/Main/UserInfoUpdate"
import Feed from "@/components/Main/Feed"

export default {
  name:"Main",
  components: {
      MainNavbar,
      LogStudy,
      History,
      MainAside,
      Feed,
      UserInfoUpdate
  },
  methods:{
    test:function(){
      this.$router.push({name:'Register'})
    },
    userData:function(data){
      let data1 = data.data1
      let data2 = data.data2
      data1.reverse()
      data2.reverse()
      this.dataHistory = data1 
      this.dataList = data2     
    },
    profileUpdate:function(){
      this.userUpdate = true
    },
    closeUpdate(bool){
      this.userUpdate = false
      if (bool) {
        location.reload()
      }
    },
    routeRegister:function(){
      this.$router.push({name:'Register'})
    }
  },
  data : function(){
    return{
      feedOpened: false,
      teststring:'',
      dataHistory:[],
      dataList:[],
      userUpdate:false,
    }
  },
  
}
</script>

<style>
#main{
  transition: .3s;
  color:var(--font-color)
}
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
  bottom: 53px;
  right: 40px;
  border-radius: 50%;
  padding: 6px;
  font-size: 1rem;
  height: 33px;
  width: 33px;
  justify-content: space-between;
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
  z-index: 1000;
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
.log-header {
  display:flex; justify-content: space-between;
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
