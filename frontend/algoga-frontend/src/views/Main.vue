<template>
  <div id="main">
    <MainNavbar />

    <div>
      <div>
        <!-- feed -->
      </div>
      <div id='main-content'>
        
        <section>
          <!-- challenge -->
          here / challenge components 

          <LogStudy />
          <!-- history -->

          <History />

          <button @click='test'>TEST Button router to problemSolving</button>

        </section>
        <div>
        <!-- 여기는 status가들어가겠조? -->
          <MainAside />
        </div>
        
    
      </div>
    </div>

  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import LogStudy from "@/components/Main/LogStudy"
import History from "@/components/Main/History"
import MainAside from "@/components/Main/MainAside"


export default {
  name:"Main",
  components: {
      MainNavbar,
      LogStudy,
      History,
      MainAside,
  },
  methods:{
    test:function(){
      this.$router.push('register')
    }
  }

}
</script>

<style>
#main > div:nth-child(2){
  display: flex;
}
#main > div > div > section {
  width: 1000px;    
  margin: 20px 50px 20px 0;
  
}
#main-content{
  display: flex;
  margin: 0 auto;
}
</style>
