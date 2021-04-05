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

      </div>
    </div>


  </div>
</template>

<script>
import MainNavbar from "@/components/Main/MainNavbar"
import CodeHighlighter from "@/components/Main/CodeHighlighter"
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'CodeBoardDetail',
  components:{
    MainNavbar,
    CodeHighlighter,
  },
  data:function(){
    return {
      code:'',
      data:[],
      title:"",
      category:[],
      userData:[],
      registerDay:[],
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
        console.log(this.data.register_date)
        this.registerDay.push(this.data.register_date.split('T')[1].split('+')[0])     
        console.log(this.data.register_date.split('T')[1].split('+')[0])
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
  /* background-color: red; */
}

.code-board-footer-info{
  height: 40px;
  background-color: red;
}

</style>