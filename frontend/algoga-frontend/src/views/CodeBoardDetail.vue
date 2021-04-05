<template>
  <div id='code-board-detail'>
    <MainNavbar />
    <div class='code-board-content'>
      <h1>{{title}}</h1>
      <!-- {{data}}
      {{category}}
      {{userData}}
      {{registerDay}} -->
      <div class='code-board-detail-status'>
        <div>
          Created at {{registerDay[0]}} {{registerDay[1]}}
        </div>
        
      </div>
      <CodeHighlighter :code='code' />

      <div class="code-board-footer-info">
        <div>
          <div>
            <i class="far fa-comment-dots"></i>
            {{commentCnt}} comments
          </div>
          <div>
            <i class="far fa-heart"></i>
            {{likeCnt}} likes
          </div>
        </div>
        <button>
          Create Comment
        </button>
      </div>

    </div>

    <CodeBoardComment :commentList = 'commentList' />


  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import CodeHighlighter from "@/components/Main/CodeHighlighter"
import CodeBoardComment from "@/components/Main/CodeBoardComment"

import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'CodeBoardDetail',
  components:{
    MainNavbar,
    CodeHighlighter,
    CodeBoardComment
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
    }
  },
  async created(){
    const codeBoard_seq = this.$route.params.codeBoard_seq
    
    await axios.get(`${SERVER_URL}/apps/v1/codeBoardPage/${codeBoard_seq}`)
      .then(res => {
        this.code = res.data[0].code
        this.data = res.data[0]
        this.category = res.data[0].free_write.split('/')   
        this.registerDay.push(this.data.register_date.split('T')[0])
        this.registerDay.push(this.data.register_date.split('T')[1].split('+')[0])     
        this.likeCnt = this.data.like_cnt
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


    
  }
}
</script>

<style>
.code-board-content {  
  width:80%;
  margin: 0 auto;
}

.code-board-detail-status {
  height: 40px; 
}

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

</style>