<template>
  <div id='feed'>
    <div @click='closeFeed'>
      <span>
          <i class="fas fa-times"></i>
      </span>
    </div>
    <h3>알림</h3>
    <div v-for="(user, idx) in users" :key='idx' id='feed-content'> 
      <div>
        <img :src="profileImg(user.userProfile)" alt="">
      </div>
      <div>
        <div>{{user.usernickName}}님이 {{user.problem_seq}}번 문제를 게시했습니다.</div>
        <p id='feed-date'>{{user.language}}, {{user.register_date | dateChange}}</p>
      </div>
      <div id ='feed-menu'>
        <span @click='removeFeed(idx)'>
          <i class="far fa-trash-alt"></i>
        </span>
      </div>
    </div>      
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://j4a302.p.ssafy.io'

export default {
    name : 'Feed',
    props :[
        'feedOpened' 
    ],
    methods : {
        closeFeed : function(){
          this.$emit('closeFeed')
        },
        removeFeed : function(idx){
          this.users.splice(idx,1)
        }
    },
    data : function(){
      return {
        users : [],
        info : [],
      }
    },
    created(){
      const userNum = localStorage.getItem('userNo')
      axios.get(`${SERVER_URL}/apps/v1/getMyFeed/${userNum}`)
        .then(res => {
          this.users = res.data[0]
          this.info = res.data[1]
          this.users.forEach(user => {
            user.usernickName = this.info.filter(inf => {
              return inf.seq == user.user_seq
            })[0].nickname

            user.userProfile = this.info.filter(inf => {
              return inf.seq == user.user_seq
            })[0].profile_image
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
    filters : {
      dateChange : function(date){
          return date.split('T')[0]
      },
    },
    computed : {
      profileImg : function(){
        return (data)=> {
          return data
        }
      }
    }
}
</script>

<style>
#feed{
    width: 350px;
    position: fixed;
    bottom: 0px;
    right: 0px;
    z-index: 100000;
    height: 100%;
    background-color: rgb(255, 255, 255);
    transition: all 1s;
    box-shadow: -1px 0 0 0 rgb(37 40 47 / 10%);
    overflow: scroll;
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */    
}
#feed::-webkit-scrollbar {
  display: none;
}
#feed > div:nth-child(1){
    margin: 0;
    color: rgba(37, 40, 47, 0.65);
    border-radius: 22px;
    float: right;
    margin-right: 10px;
    margin-top: 25px;
}
#feed > div:nth-child(1) > span{
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    padding: 4px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
}
#feed > div:nth-child(1):hover{
    cursor: pointer;
}
#feed > div:nth-child(1):hover > span{
    background-color: rgba(202, 202, 202, 0.822);
    color: rgba(37, 40, 47, 0.411);
}
#feed > h3{
  padding-bottom: 15px;
  margin: 30px 0 20px 15px;
  font-size: 1.8rem;
  box-shadow: 0 1px 0 0 rgb(37 40 47 / 10%);
}
#feed-content{
  display: flex;
  align-items: center;
  margin: 5px;
  border-radius: 10px;
  height: 70px;
  position: relative;
}
#feed-content:hover{
  cursor: pointer;
  background-color: rgba(236, 236, 236, 0.568);
}
#feed-content>div:nth-child(1){
  margin-left: 10px;
  margin-right: 10px;
}
#feed-content > div> img{
  width: 55px;
  height: 55px;
  border-radius: 50%;
}
#feed-content > div:nth-child(2) > div{
  height: 50%;
  font-size: 0.9rem;
}

#feed-date{
  font-size: 0.8rem;
  color: #1876f2;
}
#feed-content:hover > #feed-menu{
  display: inherit;
}
#feed-menu{
  display: none;
  position: absolute;
  top: 50%;
  right: 0px;
  transform : translate(-50%,-50%);
  border-radius: 50%;
  padding: 6px;
  background-color: rgb(255, 255, 255);
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 16%);
}
#feed-menu > span{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 25px;
  height: 25px;  
}
#feed-menu:hover{
  background-color: rgba(255, 255, 255, 0.568);
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>