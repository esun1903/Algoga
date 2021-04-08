<template>
  <div id="user-info-update">
    <div class='user-update'>
      <div class='edit-header'>
        <h4>Edit status</h4>
      </div>      
      <div>
        <div class='edit-image'>
          <div class='edit-image-box'>
            <img :src="image" alt="">
          </div>    
          <div>
            <label for="profileImage">        
              <span>Edit profileImage</span>
              
            </label>
            
          </div>
        </div>  
        <div @click='update' class='update-btn'>
          Update
        </div>
      </div>
      <!-- <div class='edit-footer'>
        <button @click='update'>update</button>
        <button @click='update'>update</button>
      </div> -->


    </div>
    <div class="back" @click='close(false)'></div>
    <input id='profileImage' type="file" @change='saveFile'>
  </div>
</template>

<script>
import axios from "axios"

const SERVER_URL = 'http://j4a302.p.ssafy.io'

export default {
  name:'UserInfoUpdate',
  data(){
    return {
      userPic:'',
      userData:[],
      image:'',
    }
  },
  methods:{
    close(bool){
      this.$emit('closeUpdate',bool)
    },
    saveFile:function(e){
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
          this.userPic = ''
          return;
      }

      let reader = new FileReader()
      let that = this
      reader.onload=(e)=>{that.image = e.target.result}
      this.userPic = files[0]      
      reader.readAsDataURL(this.userPic)
    },
    update:function(){
      let dataForm = new FormData()
      const keys = ['email','password','baek_id','nickname','profile_image']
      const data = [this.userData.email,this.userData.password,this.userData.baek_id,this.userData.nickname,this.userPic]
      for (let i=0;i<6;i++) {
        dataForm.append(`${keys[i]}`,data[i])
      }
      const email = localStorage.getItem('email')
      axios.put(`${SERVER_URL}/apps/v1/userInfoUpdate/${email}`,dataForm)
        .then(() => {
          this.close(true)
        })
        .catch(err=>{
          console.log(err)
        })
    }

  },
  computed:{
  },
  created(){
    const that = this
    window.addEventListener('keydown',function(event){
      if (event.key === 'Escape') {
        that.close(false)
      }
    })

    axios.get(`${SERVER_URL}/apps/v1/userInfo/${localStorage.getItem('userNo')}`)
      .then(res=>{
        this.userData = res.data
        this.image = this.userData.profile_image
      })
      .catch(err=>{
        console.log(err)
      })

  }
}
</script>

<style>
.user-update {
  position:fixed;
  top:50%; left:50%;
  transform:translate(-50%,-50%);
  width: 350px; height:350px;  
  background-color: white;
  z-index: 1001;
  border-radius: 10px;
  overflow: hidden;
}

.edit-header h4{
  background-color: rgba(207, 83, 83, 0.5);  
  margin: 0;
  padding:15px;
  color:white;
}

.back {
  position:fixed;
  width: 100vw; height:100vh;
  top:0;left:0;
  z-index: 1000;
  background-color: rgba(0,0,0,0.5);
}

#profileImage{
  visibility: hidden;
}

.edit-image {    
  padding: 10px;
  font-size: 0.8em;
  
}

.edit-image-box {  
  width:120px; height: 120px;
  overflow: hidden;
  border-radius: 50%;
  margin: 10px auto 30px;
}

.edit-image img {
  width:120px; height: 120px;
}

.edit-image label:nth-child(1) {
  cursor:pointer;
  background-color:  rgba(172, 26, 26, 0.473);
  padding:10px;
  border-radius: 10px;  
  color:white; 
}

.update-btn {
  cursor:pointer;
  background-color:  rgba(26, 172, 26, 0.473);
  padding:10px;
  border-radius: 10px;  
  color:white; 
  width:38%;
  margin : 10px auto;
  text-align: center;
}


.edit-image-box+div {text-align: center;}

/* .edit-footer {
  display:flex;  
  justify-content: space-around;
  margin-top: ;
} */




</style>