<template>
  <div id="my-code">
    <MainNavbar />
    <div class='my-code-header-box'>
      <div class='my-code-header'> 
        <h1>
          Mycodes
        </h1>
        <button class='register-btn btn-font' @click='routeRegister'>
          <i class="fas fa-signature"></i>
          CREATE
        </button>
      </div>
    </div>
    <div v-if='!data' class='my-code-section'>
    </div>
    <div class='my-code-section' v-else>
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
    },
    routeRegister:function(){
      this.$router.push({name:'Register'})
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

.my-code-header-box{
  width:80%; margin:0 auto
}

.register-btn {
  width: 100px; height: 30px;
  cursor:pointer; outline: none; border:none; border-radius: 10px;
  background-color:rgba(26, 172, 26, 0.473);
  color:white;
}

.my-code-header {
  width: 80%; margin: 0 auto; display:flex; 
  justify-content: space-between; align-items: center;
  color:var(--font-color);
}

.my-code-section {
  width: 80%;
  margin:1vh auto 0;
}

</style> 