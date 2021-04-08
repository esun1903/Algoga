<template>
  <div id="register-problem">
    <header>
      <div>
        <input type="number" placeholder="Input Problem No" @input="matchingTitle">
        <input type="text" v-model='problemTitle' disabled placeholder="Problem Title">
        <select>
          <option value="" selected hidden>Select Your Language</option>
          <option value="3">C</option>
          <option value="4">C++</option>
          <option value="1">JAVA</option>
          <option value="2">PYTHON</option>        
        </select><br>
      </div>
      <div class='algo-category'>
        <button @click="testCheck($event,idx)" v-for="(algoName,idx) in algoSolvedCategory" :key='idx'>
          {{algoName}}
        </button>     
        <button @click='categBtnAdd'>
          <p v-if='addCateg'>+</p>
          <input type="text" class='input_underline' v-model='newCateg' @keydown.enter="categBtnAdd" v-else>          
        </button>           
      </div>

    </header>
    <section>
      <div>
        <div class="code-mirror">
          <codemirror id = "codemirror" v-model='data.code' :options="codeMirrorOptions"/>
        </div>
        
        <div class='edit-mark' >
          <div>
            <div>
              <div class="circle circle-red" ></div>
              <div class="circle circle-yellow"></div>
              <div class="circle circle-green"></div>
            </div>

            <button @click="previewMark" class='status-btn'>{{editBtnText}}</button>
          </div>
          <textarea id="" v-model="data.explanation" v-if="editBtnText === 'Preview'"  >

          </textarea>
          <div v-html="compileMarkdown"  v-else></div>
        </div>
      </div>
    
    </section>
    <footer id='register-footer'>
      <button @click='registerProblem' class='regist-btn'>CREATE</button>
      <label for="hiddenCheck">
        <input type="checkbox" id="hiddenCheck">
        <div></div>        
        <button class='regist-btn-private' @click='changPrivate'>
          {{hiddenStatus}}
          <!-- <span v-if ='hiddenBool'>
            <i class='fas fa-lock-open'></i>
          </span>
          <span v-else>            
            <i class='fas fa-lock'></i>
          </span> -->
          
        </button>
      </label>
    </footer>
  </div>
</template>

<script>
import {codemirror} from "vue-codemirror"
import "codemirror/lib/codemirror.css"
import "codemirror/mode/javascript/javascript.js"
import "codemirror/theme/material.css"

import marked from "marked"
import axios from "axios"

// v1/codeBoardRegiste // post
const SERVER_URL = 'http://j4a302.p.ssafy.io'


export default {
  name:'RegisterProblem',
  components:{
    codemirror,    
  },
  data:function(){ 
    return {
      codeMirrorOptions:{
        tabSize: 2,
        mode: "application/json",
        theme: "material",
        lineNumbers: true,
        line: true,
        lint: true,
        lineWrapping: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
      },   
      addCateg:true,
      newCateg:'',   
      editBtnText:"Preview",
      algoSolvedCategory: ['DP','DFS','BFS','GREEDY','MATH','GRAPH']      ,
      btnClicked: [],
      hiddenStatus: "PUBLIC",
      hiddenBool:true,
      ctrlCheck:false,
      data:{
        "code": "SELECT YOUT LANGUAGE!",
        "explanation": "# Write your explanation \n ## ctrl+/",
        "free_write": "",
        "public": 0,        
        "like_cnt": 0,
        "user_seq": 1,
        "problem_seq": 1,
        "language_seq": 1,
        "language":'',
      },
      problemTitle:''

    }
  },
  methods:{
    registerProblem:function(){
      const lang_name = ["","JAVA","PYTHON","C","C++"]


      if (this.btnClicked.length < 1) {
        alert('어떤 방식으로 풀었는지 알려주세요!')
        return
        }
      
      const lang = document.querySelector('#register-problem select').value
      this.data.user_seq = localStorage.getItem('userNo')
      if (!lang) {
        alert('언어를 선택해주세요')
        return
      }
      this.data.language_seq = lang
      this.data.language = lang_name[this.data.language_seq]




      this.categoryToString()

      axios.post(`${SERVER_URL}/apps/v1/codeBoardRegister`,this.data)
        .then(res => {
          if (res.status !== 201) {return}
          this.$router.push({name:'Main',params:{nickname:localStorage.getItem('email')}})
        })
        .catch(err => {
          console.log(err)
        })
    },
    categoryToString:function(){
      for (let i=0;i<this.btnClicked.length;i++){
        this.data.free_write += this.algoSolvedCategory[this.btnClicked[i]]
        if (i === this.btnClicked.length-1) {return}
        this.data.free_write += '/'
      }
      
    },
    previewMark:function(){
      if (this.editBtnText === 'Preview') {
        this.editBtnText = 'Edit'
      } else {
        this.editBtnText = 'Preview'
      }
    },
    Keydown:function(event){          
      if (event.key == "Control") {
        this.ctrlCheck = true
      } else if (event.key === '/' && this.ctrlCheck) {
        this.previewMark()
      } else {this.ctrlCheck = false}
      
    },
    Keyup:function(){
      this.ctrlCheck=false
    },
    testCheck:function(event,idx){      
      if (this.btnClicked.includes(idx)){
        event.target.style.backgroundColor='black'
        event.target.style.color = 'white'
        const removeIdx = this.btnClicked.indexOf(idx)
        this.btnClicked.splice(removeIdx,1)
        return
      } 
      this.btnClicked.push(idx)      
      event.target.style.backgroundColor = "#3121be8c"
    },    
    focusTextarea:function(){
      const textarea = document.querySelector('.edit-mark > textarea')
      textarea.select()
      
    },
    categBtnAdd:function(){
      if (this.addCateg) {
        this.addCateg = !this.addCateg;
        return
      } else if (!this.newCateg) {
        return
      }
      this.algoSolvedCategory.push(this.newCateg)
      this.newCateg = ""
      this.addCateg = true
    },
    changPrivate:function(){
      if (this.hiddenStatus === 'PUBLIC') {
        this.hiddenStatus = 'PRIVATE'
        this.hiddenBool = false
        this.data.public = 1
      } else {
        this.hiddenStatus = 'PUBLIC'
        this.hiddenBool=true
        this.data.public = 0
      }      
    },
    matchingTitle:function(event){
      const probNo = event.target.value
      axios.get(`${SERVER_URL}/apps/v1/searchNumberProblem/${probNo}`)
        .then(res=>{          
          this.problemTitle = res.data.name
          this.data.problem_seq = res.data.seq

        })
        .catch(()=>{
          this.problemTitle = ''
        })
    }
    
  },
  computed:{
    compileMarkdown:function(){
      return marked(this.data.explanation,{sanitize:true})
    }
  },
  mounted() {
    // select addEventListener 
    const select = document.querySelector('#register-problem > header >div> select')
    const that = this
    select.addEventListener("change",function(){      
      if (select.value === "4") {
        that.data.code = '#include <iostream> \n\nint main() {\n\tstd::cout << "Welcome Algoga";\n\treturn 0;\n}'
      } else if (select.value === "1") {
        that.data.code = 'public class Algoga {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Welcome, Algoga");\n\t}\n}'
      } else if (select.value === "2") {
        that.data.code = 'def main(): \n	print("Welcome Algoga") \n\n\nif __name__ =="__main__": \n\tmain()'
      }
      
    })

    const inputBox = document.querySelector("#register-problem > header > div:nth-child(1) > input:nth-child(1)")
    const inputBox2 = document.querySelector("#register-problem > header > div:nth-child(1) > input:nth-child(2)")
    // const inputwidth = document.querySelector("#register-problem > header > div").clientWidth - document.querySelector("#register-problem > header > div > select").clientWidth - 15
    const inputHeight =  document.querySelector("#register-problem>header>div:nth-child(1)>select").clientHeight
    // inputBox.style.width = `${inputwidth}px`
    inputBox.style.height = `${inputHeight}px`    
    inputBox2.style.height = `${inputHeight}px`    

  },
  created(){
    window.addEventListener("keydown",this.Keydown)
    window.addEventListener("keyup",this.Keyup)
    

  }

}
</script>

<style>

#register-problem {
  margin: 100px auto;  
  width: 80%;
  /* height: 100vh; */
  font-family: Hack, monospace;
  
}
#register-problem > header >div:nth-child(1) {
  margin-bottom: 10px;
}
#register-problem > header >div:nth-child(1) > input:nth-child(1) {
  width: 22%;
  height: 100%;
  outline:none;
  border: none;
  border-bottom: 1px solid black;
  font-size: 1rem;  
  transition: 0.3s;
  margin-right: 10px;
}

#register-problem > header >div:nth-child(1) > input:nth-child(2){
  width: 50%;
  outline:none;
  border: none;

  border-bottom: 1px solid black;
  font-size: 1rem;  
  transition: 0.3s;
}





#register-problem > header >div:nth-child(1)> select{  
  padding: 10px 0;
  width: 25%;
  font-family: Hack, monospace;    
  font-size: 1rem;
  border-radius: 15px;
  outline:none;
  border:none;
  text-align-last: center;
  color:var(--back-color);
  background-color: var(--font-color);
  cursor:pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  text-indent: 1px;
  text-overflow: '';
  transition: 0.3s;
}

#register-problem > header >div:nth-child(1)> select::-ms-expand{display:none;}

/* header > div:nth-child(2) */
.algo-category > button{
  margin: 10px;
  border-radius: 10px;
  padding: 10px;
  outline:none;
  border:none;
  background-color: black;
  color:white;
  transition: 0.3s;
  cursor:pointer;
}

.algo-category > button:hover {
  padding: 15px;
  margin: 5px;
}


#register-problem > section > div:nth-child(1) {
  display:flex;
  justify-content: space-between;
}

#register-problem > section > div:nth-child(1) > div {
  width: 49%;
  /* margin: 0 auto; */
  height: 500px;
}


#register-problem > section > div:nth-child(2) {
  width: 99%;
  margin: 10px auto;
}

#register-problem > footer {
  text-align: right;
}


.CodeMirror {
  height: 500px;
  font-family: Hack, monospace;
  font-size: 0.9rem;  
}
.edit-mark {
  background-color: 	#F0F8FF;
}
.edit-mark > textarea {
  width:100%;
  padding:0;
  height: 94%;
  font-family: Hack, monospace;
  font-size: 0.9rem;  
  resize:none;
  background-color: var(--back-color) ;
  color: var(--font-color);
  outline: none;
  border:none;
  background-color: 	#F0F8FF;
 
}


.edit-mark > div:nth-child(2) {
  /* border: 1px solid black; */
  height:95%;
  
  
}


.edit-mark  > div:nth-child(1){
  display:flex;
  justify-content: space-between;
  background-color: rgba(61, 61, 100, 0.808);
}

.edit-mark > div:nth-child(1) > div {
  display: flex;
  
}

#register-footer {
  margin-top: 20px;
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  
}

#register-footer > label {
  margin-right: 20px;
}

#register-footer > label > input {
  display: none;
}

.regist-btn {
  border:none;outline: none;
  width:100px;height:50px;
  border-radius: 10px;
  background-color: #FF6F61;  
  color:white;
  cursor:pointer;
  font-family: Hack;
}

.regist-btn-private {
  border:none;outline: none;
  width:100px;height:50px;
  border-radius: 10px;
  background-color: #DD4124;
  color:white;
  cursor:pointer;
  font-family: Hack;
}



.circle {
  width: 20px;
  height: 20px;
  border-radius: 100%;
  margin: 5px;
}

.circle-red {
  background-color: red;
}

.circle-green {
  background-color: green;
}

.circle-yellow {
  background-color: yellow;
}

.input_underline {
  border:none;
  outline: none;
  border-bottom: 1px solid white;
  background-color: black;
  color:white;
}

.status-btn {
  border:none;outline: none;
  color:white; background-color: rgba(0,0,0,0);
  cursor:pointer; font-weight: bold;
}



@media screen and (max-width:1100px) {
  
  #register-problem > section > div:nth-child(1) {
    display:block;
  }
  
  #register-problem > section > div:nth-child(1) > div {
    width: 100%;
    margin: 10px auto;
    height: 500px;
  }
}


</style>