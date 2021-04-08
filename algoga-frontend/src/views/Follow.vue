<template>
  <div id="follow">
    <MainNavbar />
    <div class='follow-toggle'>
      <button @click='toggle(true)' :style='{backgroundColor:backColor1}'>
        Follower
      </button>
      <button @click='toggle(false)' :style='{backgroundColor:backColor2}'>
        Following
      </button>
    </div>
    <Follower :follow='follow' :status='status' @changeFollow='changeFollow'/>
  </div>
</template>

<script>
import MainNavbar from '@/components/Main/MainNavbar'
import Follower from '@/components/Follow/Follower'


import axios from "axios"

const SERVER_URL = 'http://j4a302.p.ssafy.io'



export default {
  name:'Follow',
  components:{
    MainNavbar,
    Follower,     
  },
  data(){
    return {
      followerActive:true,
      backColor1:  'rgba(30, 42, 216, 0.644)',
      backColor2: 'grey',
      followerList:[],
      followingList:[],
      followers:[],
      followings:[],
      follow:[],
      status:[],
      followerIdx:[],
      followingIdx:[],
    }
  },
  methods:{
    toggle(bool){      
      this.followerActive = bool
      if (bool) {
        this.backColor1 = 'rgba(30, 42, 216, 0.644)'
        this.backColor2 = 'grey'
        this.follow = this.followerList
        
        return 
      }
      this.backColor1 = 'grey'
      this.backColor2 = 'red'
      this.follow = this.followingList    
    },
    changeFollow:function(idx){
      if (this.status.includes(idx)) {
        let removeIdx = this.status.indexOf(idx)
        this.status.splice(removeIdx,1)        
        this.unFollow(idx)
        return
      }
      this.status.push(idx)
      this.Follow(idx)
    },
    Follow:function(user_seq){      
      const myNo = localStorage.getItem('userNo')
      axios.get(`${SERVER_URL}/apps/v1/followUser/${myNo}/${user_seq}`)
        .then((res)=>{
          console.log(res)
        })
        .catch(err=>{console.log(err)})
    },
    unFollow:function(user_seq){
      const myNo = localStorage.getItem('userNo')
      axios.delete(`${SERVER_URL}/apps/v1/DeletefollowingUser/${myNo}/${user_seq}`)
        .then((res)=>{
          console.log(res)
        })
        .catch(err=>{console.log(err)})
    }

  },
  async created(){
    const userNo = localStorage.getItem('userNo')
    if (!userNo){
      this.$router.push({name:'Home'})
      return
    }


    await axios.get(`${SERVER_URL}/apps/v1/followerList/${userNo}`)
      .then(res=>{
        this.followers = res.data        
      })
      .catch(err=>{
        console.log(err)
      })
    await axios.get(`${SERVER_URL}/apps/v1/followingList/${userNo}`)
      .then(res=>{
        this.followings = res.data
      })
      .catch(err=>{
        console.log(err)
      })

    this.followerList = []
    this.followingList = []
    this.followingIdx = []
    this.followerIdx = []

    for (let i = 0; i<this.followers.length; i++) {
      let user_seq = this.followers[i].user_follower_seq
      this.followerIdx.push(user_seq)
      axios.get(`${SERVER_URL}/apps/v1/userInfo/${user_seq}`)
        .then(res=>{
          this.followerList.push(res.data)    
                
        })
        .catch(err=>{
          console.log(err)
        })
    }
    for (let i = 0; i<this.followings.length; i++) {
      let user_seq = this.followings[i].user_following_seq
      this.followingIdx.push(user_seq)      
      axios.get(`${SERVER_URL}/apps/v1/userInfo/${user_seq}`)
        .then(res=>{
          this.followingList.push(res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    }
    this.follow = this.followerList
    this.status = this.followingIdx

  }
}
</script>

<style>
.follow-toggle {
  width: 80%;
  margin:0 auto;
  display:flex; justify-content: space-between;
  /* border-top: 1px solid black;
  padding-top: 5px; */
}

.follow-toggle > button {
  font-family: Hack,Avenir, Helvetica, Arial;
  width:49%; height: 50px; border-radius: 10px;
  outline: none; border:none; 
  cursor:pointer;
  font-size: 1em;
  transition: .3s;
  color:white;
}

#follow-comp {
  width: 80%;
  margin:50px auto 0;  
  color:var(--font-color);
}

.person-div {
  width: 100%;  
  margin: 0 auto 20px;  
  border-bottom:1px solid var(--font-color) ;
  padding-bottom:20px;
  display:flex; 
  align-items: center; 
}


.person-img {
  display:block;
  width: 70px; height:70px;
  border-radius: 50%; overflow: hidden;
}

.person-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width:90%;
  margin:0 auto;
}

#follow-comp button {
  font-family: Hack,Avenir, Helvetica, Arial;
  width: 100px; height:40px;
  margin-right: 20px;
  cursor:pointer;
  font-weight: bold;
  color:white;
  border:none; outline: none;
  border-radius: 10px;
  background-color: blue;
}
#follow-comp button:nth-child(2) {
  width: 100px;
  margin-right: 0px;
  
}


</style>