<template>
  <div id="main">
    <MainNavbar />

    <div>
      <div>
        <!-- feed -->
      </div>
      <section>
        
        <!-- challenge -->
        here / challenge components 

        <LogStudy />
        <!-- history -->

        <History />
      </section>
      <div>
        <!-- 여기는 status가들어가겠조? -->
      </div>
    </div>

  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import LogStudy from "@/components/Main/LogStudy"
import History from "@/components/Main/History"


export default {
  name:"Main",
  components: {
      MainNavbar,
      LogStudy,
      History,
  }

}
</script>

<style>
#main > div >section {
  width: 1000px;    
  margin: 20px auto;
    
}


</style>