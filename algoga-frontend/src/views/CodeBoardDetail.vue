<template>
  <div id='code-board-detail-origin'>
    <MainNavbar />    
    <div class='code-board-content'>
      <h1>{{title}}</h1>      
      <div class='code-board-detail-status'>
        <div>
          <i class="far fa-user"></i>
          <span>{{userData.nickname}}</span>
          <i class="fas fa-sitemap"></i>
          <span>{{data.free_write}}</span>
          <i :class="langClass"></i>
          <span>{{data.language}}</span>
        </div>

        <div class='flex'>
          <i class="far fa-clock"></i>
          <span>{{registerDay[0]}} {{registerDay[1]}}</span>
          <div v-if='mine' class='flex'>
            <div @click='deleteBoard()'>
              <span><i class="far fa-trash-alt"></i> Delete</span>
            </div>
          </div>
          <div class='flex' v-else>
            <div @click='routeHome(userData.seq,userData.email)'>                
                <span><i class='fas fa-home'></i> Home</span> 
              </div>
          </div>
        </div>
      </div>

      <MarkDownViewer :explanation='this.data.explanation' />
      <CodeHighlighter :code='code' />

      <div class="code-board-footer-info">
        <div>
          <div>
            <i class="far fa-comment-dots"></i>
            {{commentCnt}} comments
          </div>
          <div @click='like'>
            <span v-if='iLiked'>
              <i class="fas fa-heart"></i>
            </span>
            <i v-else>
              <i class="far fa-heart"></i>
            </i>
            {{likeCnt}} likes
          </div>
        </div>
        <button @click='createActivate = !createActivate'>
          Create Comment
        </button>
      </div>

    </div>
    <transition name="slide-fade">
      <div v-show="createActivate" class='commentInput'>
        <input type="text" placeholder="Create Comment..." v-model='commentInput' @keydown.enter="createComment">
        <button @click='createComment'>Create</button>
      </div>        
      
    </transition>

    <CodeBoardComment :commentList = 'commentList' @deleteComment='deleteComment' />


  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import CodeHighlighter from "@/components/Main/CodeHighlighter"
import MarkDownViewer from "@/components/Main/MarkDownViewer"
import CodeBoardComment from "@/components/Main/CodeBoardComment"

import axios from 'axios'

const SERVER_URL = 'http://j4a302.p.ssafy.io'
// 

export default {
  name:'CodeBoardDetail',
  components:{
    MainNavbar,
    CodeHighlighter,
    CodeBoardComment,
    MarkDownViewer
  },
  data:function(){
    return {
      code:'',
      data:[],
      title:"",
      category:[],
      userData:[],
      registerDay:[],
      commentCnt:0,
      likeCnt:0,
      commentList:[],
      createActivate:false,
      commentInput:'',
      langClass:'',
      iLiked:false,
    }
  },
  methods:{
    createComment:function(){
      if (!this.commentInput) {return;}

      const commentData = {
        'text':this.commentInput,
        'user_seq':localStorage.getItem('userNo'),
        'code_board_seq':this.$route.params.codeBoard_seq
      }      
      axios.post(`${SERVER_URL}/apps/v1/commentRegister`,commentData)
        .then((res)=>{
          console.log(res)
          commentData['register_date'] = '방금전'
          this.commentList.push(commentData)
          this.commentCnt += 1
          this.commentInput =''
          this.createActivate = false
        })
        .catch(err=>{
          console.log(err)
          alert(err)
        })
    },
    deleteComment:function(){
      this.commentCnt -=1
    },
    deleteBoard:function(){
      axios.delete(`${SERVER_URL}/apps/v1/codeBoardDelete/${this.data.seq}`)
        .then(()=>{
          this.$router.push({name:'Main',params:{nickname:localStorage.getItem('email')}})
        })
        .catch(err=>{
          alert(err)
        })
    },
    like:function(){
      const codeBoard_seq = this.$route.params.codeBoard_seq
      const userNo = localStorage.getItem('userNo')

      axios.get(`${SERVER_URL}/apps/v1/codeBoardLike/${codeBoard_seq}/${userNo}`)
        .then(()=>{
          if (this.iLiked) {
            this.likeCnt -= 1
          } else {
            this.likeCnt += 1
          }
          this.iLiked = !this.iLiked
        })
        .catch(err=>{
          console.log(err)
        })
    },
    routeHome:function(no,email){
      this.$router.push({name:'Main',params:{nickname:email,userno:no}})
    }
  },
  computed:{
    mine:function(){
      if (localStorage.getItem('userNo') == this.data.user_seq ) {
        return true
      }
      return false
    }
  },
  async created(){
    const codeBoard_seq = this.$route.params.codeBoard_seq
    const userNo = localStorage.getItem('userNo')
    const langClassList = ['','fab fa-java','fab fa-python','fab fa-c','fab fa-cpp']
    await axios.get(`${SERVER_URL}/apps/v1/codeBoardPage/${codeBoard_seq}`)
      .then(res => {
        this.code = res.data[0].code
        this.data = res.data[0]
        this.category = res.data[0].free_write.split('/')   
        this.registerDay.push(this.data.register_date.split('T')[0])
        this.registerDay.push(this.data.register_date.split('T')[1].split('+')[0])     
        this.likeCnt = this.data.like_cnt        
        this.langClass = langClassList[this.data.language_seq]          

      })
      .catch(err => {
        console.log(err)
      })

    if (this.data.is_active && localStorage.getItem('userNo')!==this.data.user_seq) {
      alert('비공개게시물입니다.')
      this.$router.push({name:'Main',params:{nickname:localStorage.getItem('email')}})
    }

    await axios.get(`${SERVER_URL}/apps/v1/Problem/${this.data.problem_seq}`)
      .then(res=>{
        this.title = `${res.data.number}. ${res.data.name}`
      })
      .catch(err=>{
        console.log(err)
      })

    await axios.get(`${SERVER_URL}/apps/v1/userInfo/${this.data.user_seq}`)
      .then(res =>{
        this.userData = res.data
      })
      .catch(err=>{
        console.log(err)
      })
    await axios.get(`${SERVER_URL}/apps/v1/commentList/${codeBoard_seq}`)
      .then(res =>{
        this.commentCnt = res.data.length
        this.commentList = res.data        
      })
      .catch(()=>{
        this.commentCnt = 0
      })    

    axios.get(`${SERVER_URL}/apps/v1/codeBoardLike_User/${codeBoard_seq}`)
      .then(res=>{
        if (res.data.includes(Number(userNo))) {
          this.iLiked = true
        }        
      })
      .catch(err=>{
        console.log(err)
      })


  }
}
</script>

<style>
.code-board-content {  
  width:80%;
  margin: 0 auto;
}

.code-board-content > h1 {
  border-bottom: 1px solid black;
  padding-bottom: 10px;
}

.code-board-detail-status svg {
  margin-right: 5px;
}
.code-board-detail-status span {
  margin-right: 10px;

}

.code-board-detail-status {
  height: 40px; 
  font-size: 0.9em;
  margin-top: -10px;
  display:flex;
  justify-content: space-between;
}

.code-board-detail-status > div.flex > div > div {
  cursor:pointer
}



.flex {display: flex;}
.code-board-footer-info{
  display: flex;
  align-items: center;
  height: 40px;
  padding:5px 0px 5px 10px;
  
  /* border-radius: 10px; */
  margin: 20px 0;
  justify-content: space-between;
  border-bottom: 1px solid black;
  /* background-color: red; */
}

.code-board-footer-info > div:nth-child(1) {
  display:flex;
}
.code-board-footer-info > div:nth-child(1) > div {
  margin-right: 20px;
}

.code-board-footer-info button {
  display:block;
  width: 150px;
  height: 100%;
  outline: none; border:none;
  border-radius: 10px;
  background-color:deeppink;
  cursor:pointer;
  color:white;
  font-family: Hack;
}

.fa-heart{
  cursor:pointer;
}

</style>