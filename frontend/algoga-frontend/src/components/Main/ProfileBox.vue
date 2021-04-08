<template>
  <div id="profile-box">
    <div class='profile-img-box'>
      <img :src="profileImg" alt="">
    </div>
    <div class='profile-content-box'>
      <div class='profile-nick-box'>
        <span>
          {{data.nickname}}
        </span>
        <div>
          <div v-if='mine' class='profile-setting' @click='profileUpdate'>
            <i class="fas fa-cog"></i>
          </div>
          <button v-else>Follow</button>
        </div>
      </div>
      <div>
        <div class='profile-bottom'>
          <div>
            <span>Follower:{{follower}} </span>
          </div>          
          <div>
            <span> Following:{{following}}</span>
          </div>
          
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from "axios"

const SERVER_URL = 'http://j4a302.p.ssafy.io'


export default {
  name:'ProfileBox',
  data(){
    return {
      data:[],
      follower:0,
      following:0,
      updateStatus:true,
    }
  },
  methods:{
    loadData:function(){
      const userNo = this.$route.params.userno
      axios.get(`${SERVER_URL}/apps/v1/userInfo/${userNo}`)
        .then(res=>{
          this.data = res.data
        })
        .catch(err=>{console.log(err)})
      },
    followerCheck:function(){
      const userNo = this.$route.params.userno
      axios.get(`${SERVER_URL}/apps/v1/followerList/${userNo}`)
        .then(res=>{
          this.follower = res.data.length
        })
        .catch(err=>console.log(err))
    },
    followingCheck:function(){
      const userNo = this.$route.params.userno
      axios.get(`${SERVER_URL}/apps/v1/followingList/${userNo}`)
        .then(res=>{
          console.log(res,'/???')
          this.follower = res.data.length
        })
        .catch(err=>console.log(err))
    },
    profileUpdate:function(){
      this.$emit('profileUpdate')
    }

  },
  computed:{
    profileImg(){
      console.log(this.data)
      return `${this.data.profile_image}`
    },
    mine(){
      const userNo = localStorage.getItem('userNo')
      const profileNo = this.$route.params.userno
      if (userNo === profileNo) {return true}
      return false
    }
  },
  created(){
    this.loadData()
  },
  watch:{
    $route(to,from){
      if (to.path!==from.path){
        this.loadData()
      }
    }
  }

}
</script>

<style>
#profile-box{
  width:100%;  
  display:flex;
  align-items: stretch;

}

.profile-img-box {
  width: 100px; height:100px;
  overflow: hidden; border-radius: 50%;
  margin: 0 30px 0 20px;
}

#profile-box img {
  width: 100px; height: 100px;
}

.profile-content-box {  
  width:calc(90% - 200px);
  display: flex; flex-direction: column; justify-content: space-around;
}

.profile-nick-box {
  display: flex; justify-content: space-between;
}

.profile-setting {
  cursor:pointer
}

.profile-bottom {
  display:flex; justify-content: space-between;
  font-size: 0.7rem;  
}

@media screen and (max-width:1100px) {
  #profile-box{    
    justify-content: left;
    
  }
  .profile-img-box {
    width: 150px; height:150px;    
    margin: 0;
  }
    #profile-box img {
    width: 150px; height: 150px;
  }
  .profile-content-box {  
    width:calc(40% - 100px);    
  }
  
  .profile-nick-box {
    display: flex; justify-content: space-between;
  }

  .profile-setting {
    cursor:pointer
  }

  .profile-bottom {
    justify-content:left;
  }

      
}


</style>