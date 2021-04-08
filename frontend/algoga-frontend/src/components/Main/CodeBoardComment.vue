<template>
  <div id="code-board-comment">
    <div v-for='(data,idx) in commentList' :key='idx'>
      <div class="comment-header">
        <div>
          <div class='comment-user-profile-img'>
            <img :src="profileImage(userData[idx])" alt="">
          </div>
        </div>        
        <div>
          <div v-if='userData[idx]'>            
            <span>{{userData[idx].nickname}}</span>
          </div>
          <div class='comment-status'>
            <div>
              <i class="far fa-clock"></i>
              {{createdAt(data.register_date)}}
            </div>
            <div v-if='mine(data,idx)'>
              <div @click='deleteComment(data)'>
                <i class="far fa-trash-alt"></i>
                <span>delete</span>
              </div>
            </div>
            <div v-else>
              <div @click='routeHome(data)'>
                <i class='fas fa-home'></i> 
                <span>Home</span> 
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="comment-content">
        {{data.text}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://j4a302.p.ssafy.io'



export default {
  name:'CodeBoardComment',
  props: {
    commentList:Array,
  },
  data:function(){
    return {
      userData:[{'nickname':'h'}]
    }
  },
  methods:{
    deleteComment:function(data,idx){
      axios.delete(`${SERVER_URL}/apps/v1/commentDelete/${data.seq}`)
        .then(()=>{
          this.$emit('deleteComment')
          this.commentList.splice(idx,1)

        })
        .catch((err)=>{
          alert(err)
        })
    },
    routeHome:function(data){
      axios.get(`${SERVER_URL}/apps/v1/userInfo/${data.user_seq}`)
        .then(res=>{
          this.$router.push({name:'Main',params:{nickname:res.data.email,userno:data.user_seq}})
        })
        .catch(err=>console.log(err))
    }
  },
  watch:{
    commentList:async function(){
      this.userData = []
      for (let i=0; i<this.commentList.length; i++) {
        await axios.get(`${SERVER_URL}/apps/v1/userInfo/${this.commentList[i].user_seq}`)
          .then(res=>{
            this.userData.push(res.data)
          })
          .catch(err=>{
            console.log(err)
          })
      }
    }
  },
computed:{
  createdAt(){
    return (time) =>{
      if (time === '방금전') {
        return time
      } 
      return time.split('T')[0] + ' ' + time.split('T')[1].split('+').[0]
    }
  },
  profileImage(){
    return (data) => {      
      return data.profile_image
    }
  },    
  mine(){
    return (data) => {      
      if (data.user_seq == localStorage.getItem('userNo')) {
        return true
      }
      return false
    }
  }
}

}


</script>

<style>
#code-board-comment {
  width: 80%;
  margin: 30px auto 10px;
}

#code-board-comment > div {
  border:1px solid rgba(204, 62, 62, 0.1);
  margin-bottom: 20px;
  border-radius: 10px;
  padding: 20px;
}

.comment-header {
  display:flex;
  align-items:stretch; 
  
  font-size: 0.8em;
}
.comment-header > div:nth-child(1) {
  display:flex;
  align-items: center;
}

.comment-header > div:nth-child(2) {
  display:flex;
  flex-direction: column;
  justify-content: center;
}

.comment-header > div:nth-child(2) > div:nth-child(1) {
  display:inline-block;
  width: calc(100vw * 0.8 - 100px);
  border-bottom: 1px solid rgba(204, 62, 62, 0.1);
  padding-bottom: 5px;
  margin-bottom: 2px;

}

.comment-content{  
  display:inline-block;
  padding:10px;
  border-radius: 10px;
  font-size: 1em;
  margin: 20px 0 10px;  
  max-width: calc(100% - 60px);

}

.comment-user-profile-img {
  border-radius: 10px;  
  width: 50px;
  height:50px;
  overflow: hidden;
  margin-right: 10px;
  border:1px solid rgba(204, 62, 62, 0.027);
  }

.comment-user-profile-img > img {
  width: 50px; height:50px;
}


.commentInput {
  width:80%;
  margin: 0 auto;
}

.commentInput>input {
  display:inline-block;
  width:80%;
  height:20px;
  outline:none; border:none;
  border-bottom: 1px solid rgba(204, 62, 62, 0.1);

}

.commentInput>button {
  width: 18%;
  border-radius: 10px;
  margin-left: 1%;
  background-color: rgba(204, 62, 62, 0.418);
  color:white;
  height:30px;  
  outline: none; border:none;
  cursor:pointer;
}

.comment-status {
  display:flex;
  justify-content: space-between;
}

.comment-status > div> div >svg {
  margin: 0 3px 0 10px;
}
.comment-status > div {
  display:flex;
}

.comment-status > div > div{
  cursor:pointer;
}
</style>