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
          <button class='btn-font follow-btn' :style="{backgroundColor:bgcolor}" @click='follow' v-else>{{followStatus}}</button>
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
      followStatus:'Follow',
      bgcolor:'rgba(30, 42, 216, 0.644)',
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
          for (let i=0; i<res.data.length; i++) {
            if (res.data[i].user_follower_seq == localStorage.getItem('userNo')) {
              this.followStatus = 'Unfollow'
              this.bgcolor = 'rgba(211, 19, 19, 0.5)'
            }
          }
        })
        .catch(err=>console.log(err))
    },
    followingCheck:function(){
      const userNo = this.$route.params.userno
      axios.get(`${SERVER_URL}/apps/v1/followingList/${userNo}`)
        .then(res=>{          
          this.following = res.data.length
          
        })
        .catch(err=>console.log(err))
    },
    profileUpdate:function(){
      this.$emit('profileUpdate')
    },
    changeFollowStatus:function(){
      if (this.followStatus === 'Follow') {
        this.followStatus = 'Unfollow'
        this.bgcolor = 'rgba(211, 19, 19, 0.5)'
        this.follower += 1
        this.Follow()
        return
      }
      this.followStatus = 'Follow'
      this.bgcolor = 'rgba(30, 42, 216, 0.644)'
      this.follower -= 1
      this.unFollow()
    },
    follow:function(){
      this.changeFollowStatus()
    },
    Follow:function(){      
      const myNo = localStorage.getItem('userNo')
      const user_seq = this.$route.params.userno
      axios.get(`${SERVER_URL}/apps/v1/followUser/${myNo}/${user_seq}`)
        .then((res)=>{
          console.log(res)
        })
        .catch(err=>{console.log(err)})
    },
    unFollow:function(){
      const myNo = localStorage.getItem('userNo')
      const user_seq = this.$route.params.userno
      axios.delete(`${SERVER_URL}/apps/v1/DeletefollowingUser/${myNo}/${user_seq}`)
        .then((res)=>{
          console.log(res)
        })
        .catch(err=>{console.log(err)})
    }
  },
  computed:{
    profileImg(){      
      return `${this.data.profile_image}`
    },
    mine(){
      const userNo = localStorage.getItem('userNo')
      const profileNo = this.$route.params.userno      
      if (userNo == profileNo) {return true}
      return false
    }
  },
  created(){
    this.loadData()
    this.followerCheck()
    this.followingCheck()
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

.follow-btn {
  background-color: rgba(30, 42, 216, 0.644);
  color:white;
  padding:5px;
  border:none;outline: none; border-radius: 5px;
  cursor:pointer;
}

@media screen and (max-width:1100px) {
  #profile-box{    
    justify-content: left;
    border-bottom: 1px solid rgba(0,0,0,0.2);
    padding-bottom: 30px;
    
  }
  .profile-img-box {
    width: 150px; height:150px;    
    margin: 0; margin-right: 50px;
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

  #profile-box span {
    margin-right: 10px;
  }


   
      
}


</style>