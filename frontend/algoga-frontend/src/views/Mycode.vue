<template>
  <div id="my-code">
    <MainNavbar />

    <div class='my-code-section'>
      <div v-for='(prob,idx) in data' :key='idx'>        
        <MycodeComp :data = 'prob'/>
      </div>
    </div>
  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import MycodeComp from "@/components/Mycode/MycodeComp"

import axios from "axios"

const SERVER_URL = 'http://j4a302.p.ssafy.io'


export default {
  name:"Mycode",
  components:{
    MainNavbar,
    MycodeComp
  },
  data(){
    return {
      data:[]
    }
  },
  methods:{
    loadData:function(email){
      axios.get(`${SERVER_URL}/apps/v1/codeBoardUser/${email}`)
        .then(res=>{
          this.data = res.data
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
  created(){
    const userEmail = localStorage.getItem('email')
    const userNo = localStorage.getItem('userNo')
    
    if (!userEmail||!userNo){
      this.$router.push({name:'Home'})
      return
    }
    
    this.loadData(userEmail)
  }
}
</script>

<style>
.my-code-section {
  width: 80%;
  margin:5vh auto 0;
}

</style> 