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

    <Follower  v-if='followerActive' :followerList='followerList' />
    <Following v-else :followingList='followingList' />


  </div>
</template>

<script>
import MainNavbar from '@/components/Main/MainNavbar'
import Follower from '@/components/Follow/Follower'
import Following from '@/components/Follow/Following'

import axios from "axios"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'Follow',
  components:{
    MainNavbar,
    Follower, 
    Following
  },
  data(){
    return {
      followerActive:true,
      backColor1:  'black',
      backColor2: 'red',
      followerList:[],
      followingList:[],
      followers:[],
      followings:[],
    }
  },
  methods:{
    toggle(bool){
      console.log(bool)
      this.followerActive = bool
      if (bool) {
        this.backColor1 = 'red'
        this.backColor2 = 'grey'
        return 
      }
      this.backColor1 = 'grey'
      this.backColor2 = 'red'
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

    for (let i = 0; i<this.followers.length; i++) {
      let user_seq = this.followers[i].user_follower_seq
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
      console.log(this.followings)
      axios.get(`${SERVER_URL}/apps/v1/userInfo/${user_seq}`)
        .then(res=>{
          console.log(res.data)
          this.followingList.push(res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    }

  }
}
</script>

<style>
.follow-toggle {
  width: 80%;
  margin:0 auto;
  display:flex; justify-content: space-between;
}

.follow-toggle > button {
  font-family: Hack,Avenir, Helvetica, Arial;
  width:49%; height: 50px; border-radius: 10px;
  outline: none; border:none; 
  cursor:pointer;
  font-size: 1em;
  transition: .3s;
}

#follow-comp {
  width: 80%;
  margin:50px auto 0;
}

.person-div {
  width: 100%;  
  margin: 0 auto 20px;  
  border-bottom:1px solid black ;
  padding-bottom:20px;
}

</style>