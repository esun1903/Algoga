<template>
  <div id="mycode-comp" @click='routTo(data.seq)'>
    <div class='mycode-comp-cover'></div>
    <div class='mycode-comp-header'>      
      <h3><i class='fas fa-lock' v-if='data.public'></i>{{problemTitle}}</h3>
      <div class='flex-right'>
        <div>
          <i class="fas fa-sitemap"></i><span>{{data.free_write}}</span>
        </div>   
        <div>
          <i :class="langIconClass(data.language_seq)"></i><span>{{data.language}}</span>
        </div>   
        <div>
          <i class="far fa-clock"></i>
          <span>{{clock}}</span>
        </div>
      </div>
    </div>

    
    <div class='mycode-plus'>      
      <i class="fas fa-plus"></i>
    </div>
  </div>
</template>

<script>
import axios from "axios"

const SERVER_URL = 'http://j4a302.p.ssafy.io'


export default {
  name:"MycodeComp",
  props:{
    data:Object,
    
  },
  data(){
    return {
      problemData:[],
      hovered:true,
      langIcon:['','fab fa-java','fab fa-python','fab fa-c','fab fa-c']
    }
  },
  computed:{
    problemTitle(){
      return this.problemData.number + '.'+ this.problemData.name
    },
    clock(){
      return this.data.register_date.split('T')[0]
    },
    langIconClass(){      
      return (idx) => {
        return this.langIcon[idx]
      }
    }
  },
  methods:{
    getProblemData(){
      axios.get(`${SERVER_URL}/apps/v1/Problem/${this.data.problem_seq}`)
        .then(res=>{          
          this.problemData = res.data
        })
        .catch(err=>{
          console.log(err)
        })      
    },
    codePlus(){
      this.hovered = !this.hovered      
    },
    routTo(seq){
      this.$router.push({name:'CodeBoardDetail',params:{codeBoard_seq:seq}})
    }
  },
  mounted(){
    this.getProblemData()
  }


}
</script>

<style>
#mycode-comp {  
  position:relative;
  width:80%;
  background-color: rgba(207, 207, 212, 0.329);
  margin: 5px 10% 20px;
  cursor:pointer;
  border-radius: 5px;
  padding:10px;
  transition: .3s;
  display: flex;
  justify-content: space-around;
  overflow: hidden;
}

#mycode-comp:hover {
  margin: 5px 0 20px 12%;
  color:white
}

.mycode-comp-header {
  
  position:relative;
  width:90%;
  display:flex;
  justify-content: space-between;
  color:var(--font-color)
}

#mycode-comp svg{margin-right: 10px;}

.flex-right{
  display:flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: .8em;
  align-items: flex-end;
}


.mycode-plus {
  display: flex;  
  justify-content: center;
  align-items: center;
  transition: .3s;
}

.mycode-comp-cover {
  position:absolute;
  top:0; left:-100%;
  width:100%; height:100%;
  transition:.3s;
  z-index:0;
  background-color: rgba(216, 74, 74, 0.473);
}

#mycode-comp:hover > .mycode-comp-cover {
  left:0;
}


</style>