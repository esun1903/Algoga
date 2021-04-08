<template>
  <div id="user-info-update">
    <div class='user-update'>
      <input type="file" @change='saveFile'>
      <button @click='update'>update</button>
    </div>
    <div class="back" @click='close'></div>
  </div>
</template>

<script>
import axios from "axios"

const SERVER_URL = 'http://j4a302.p.ssafy.io'

export default {
  name:'UserInfoUpdate',
  data(){
    return {
      userPic:''
    }
  },
  methods:{
    close(){
      this.$emit('closeUpdate')
    },
    saveFile:function(e){
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
          this.userPic = ''
          return;
      }
      this.userPic = files[0]      
      console.log(this.userPic)
    },
    update:function(){
      let dataForm = new FormData()
      const keys = ['email','password','baek_id','nickname','level','profile_image']
      const data = ['ldh297@naver.com','dkfrhrk1!','ldh297','dodo','0',this.userPic]
      for (let i=0;i<6;i++) {
        dataForm.append(`${keys[i]}`,data[i])
      }
      const email = localStorage.getItem('email')
      axios.put(`${SERVER_URL}/apps/v1/userInfoUpdate/${email}`,dataForm)
        .then(res => {
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    }

  },
  created(){
    const that = this
    window.addEventListener('keydown',function(event){
      if (event.key === 'Escape') {
        that.close()
      }
    })
  }
}
</script>

<style>
.user-update {
  position:fixed;
  top:50%; left:50%;
  transform:translate(-50%,-50%);
  width: 600px; height:700px;
  padding:50px;
  background-color: white;
  z-index: 1001;
  border-radius: 10px;
}


.back {
  position:fixed;
  width: 100vw; height:100vh;
  top:0;left:0;
  z-index: 1000;
  background-color: rgba(0,0,0,0.5);
}



</style>