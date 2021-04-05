<template>
  <div id='code-board-detail'>
    <MainNavbar />
    <div class='code-board-body'>
      <h1>{{title}}</h1>
      {{data}}
      {{category}}
      <div class='code-board-detail-status'>
        
      </div>
      <CodeHighlighter :code='code' />
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
    }
  },
  async created(){
    const codeBoard_seq = this.$route.params.codeBoard_seq
    
    await axios.get(`${SERVER_URL}/apps/v1/codeBoardPage/${codeBoard_seq}`)
      .then(res => {
        this.code = res.data[0].code
        this.data = res.data[0]
        this.category = res.data[0].free_write.split('/')
        console.log(this.category)
      })
      .catch(err => {
        console.log(err)
      })

    await axios.get(`${SERVER_URL}/apps/v1/Problem/${this.data.problem_seq}`)
      .then(res=>{
        this.title = `${res.data.number}. ${res.data.name}`
      })
      .catch(err=>{
        console.log(err)
      })


    
  }
}
</script>

<style>
.code-board-body {  
  width:80%;
  margin: 0 auto;
}

.code-board-detail-status {
  height: 40px;
  background-color: red;
}

</style>