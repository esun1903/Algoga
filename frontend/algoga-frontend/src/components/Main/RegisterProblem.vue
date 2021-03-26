<template>
  <div id="register-problem">
    <header>
      <div>
        <input type="text" placeholder="Input Problem No or Title">
        <select>
          <option value="" selected hidden>Select Your Language</option>
          <option value="cpp">C++</option>
          <option value="java">JAVA</option>
          <option value="python">PYTHON</option>        
        </select><br>
      </div>
      <div class='algo-category'>
        <button @click="testCheck($event,idx)" v-for="(algoName,idx) in algoSolvedCategory" :key='idx'>
          {{algoName}}
        </button>
        <!-- 여기 인풋은 등록하면 버튼으로 추가 되게할 예정 -->
        <input type="text">
      </div>

    </header>
    <section>
      <div>
        <div class="code-mirror">
          <codemirror id = "codemirror" v-model="inputCode" :options="codeMirrorOptions"/>
        </div>
        
        <div class='edit-mark' >
          <div>
            <div>
              <div class="circle circle-red" ></div>
              <div class="circle circle-yellow"></div>
              <div class="circle circle-green"></div>
            </div>

            <button @click="previewMark">{{editBtnText}}</button>
          </div>
          <textarea id="" v-model="inputComment" v-if="editBtnText === 'Preview'" >

          </textarea>
          <div v-html="compileMarkdown"  v-else ></div>
        </div>
      </div>
    
    </section>
    <footer id='register-footer'>
      <label for="hiddenCheck">
        <input type="checkbox" id="hiddenCheck">
        <div></div>
        <span>{{hiddenStatus}}</span>        
      </label>
      <button>등록</button>
    </footer>
  </div>
</template>

<script>
import {codemirror} from "vue-codemirror"
import "codemirror/lib/codemirror.css"
import "codemirror/mode/javascript/javascript.js"
import "codemirror/theme/material.css"

import marked from "marked"

import _ from "lodash"

export default {
  name:'RegisterProblem',
  components:{
    codemirror,    
  },
  methods:{
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
      event.target.style.color = 'black'
      event.target.style.backgroundColor = "red"
    },    
    
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
      inputCode: "SELECT YOUT LANGUAGE!",
      inputComment: "",
      editBtnText:"Preview",
      ctrlCheck:false,
      algoSolvedCategory: ['DP','DFS','BFS','GREEDY','MATH','GRAPH']      ,
      btnClicked: [],
      hiddenStatus: "Public",

    }
  },
  computed:{
    compileMarkdown:function(){
      return marked(this.inputComment,{sanitize:true})
    }
  },
  mounted() {
    // select addEventListener 
    const select = document.querySelector('#register-problem > header >div> select')
    const that = this
    select.addEventListener("change",function(){      
      if (select.value === "cpp") {
        that.inputCode = '#include <iostream> \n\nint main() {\n\tstd::cout << "Welcome Algoga";\n\treturn 0;\n}'
      } else if (select.value === "java") {
        that.inputCode = 'public class Algoga {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Welcome, Algoga");\n\t}\n}'
      } else if (select.value === "python") {
        that.inputCode = 'def main(): \n	print("Welcome Algoga") \n\n\nif __name__ =="__main__": \n\tmain()'
      }
      
    })

    const inputBox = document.querySelector("#register-problem > header > div:nth-child(1) > input")
    // const inputwidth = document.querySelector("#register-problem > header > div").clientWidth - document.querySelector("#register-problem > header > div > select").clientWidth - 15
    const inputHeight =  document.querySelector("#register-problem>header>div:nth-child(1)>select").clientHeight
    const lineColor = ['red','blue','yellow','black','white']
    // inputBox.style.width = `${inputwidth}px`
    inputBox.style.height = `${inputHeight}px`    
    inputBox.addEventListener('focusin',function(){
      inputBox.style.width = "75%"
      inputBox.style.borderBottom = "1px solid red"
    })
    inputBox.addEventListener('focusout',function(){
      if (inputBox.value){return}
      inputBox.style.width = "25%"
      inputBox.style.borderBottom = "1px solid black"
    })
    inputBox.addEventListener('keypress',function(){
      const color = _.random(5)
      inputBox.style.borderBottom = `1px solid ${lineColor[color]}`
    })

    // 공개 비공개 버튼의 활성화에 따른 것
    const hiddenBox = document.querySelector('#register-footer > label > input')
    const hiddenLabel = document.querySelector('#register-footer>label')
    hiddenBox.addEventListener('click',function(){
      if (hiddenBox.checked) {

        that.hiddenStatus = "Private"
        hiddenLabel.style.textAlign = "left"
      } else {
        that.hiddenStatus = "Public"
        hiddenLabel.style.textAlign = "right"
      }
    })


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
#register-problem > header >div:nth-child(1) > input {
  width: 20%;
  height: 100%;
  outline:none;
  border: none;
  border-bottom: 1px solid black;
  font-size: 1rem;  
  transition: 0.3s;
}
#register-problem > header >div:nth-child(1)> select{  
  padding: 10px 0;
  width: 24%;
  font-family: Hack, monospace;    
  font-size: 1rem;
  border-radius: 0 15px 0 15px;
  outline:none;
  border:none;
  text-align-last: center;
  color:white;
  background-color: rgb(63, 156, 86);
  cursor:pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  text-indent: 1px;
  text-overflow: '';
  transition: 0.3s;
}

#register-problem > header >div:nth-child(1)> select:hover { border-radius: 15px;}

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

#register-problem > section > div > div:nth-child(2) > textarea {
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
  background-color: bisque;
 
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
  display: flex-end;
  align-items: center;
}

#register-footer > label {
  display:inline-block;
  position:relative;
  cursor:pointer;
  width:100px;
  margin: 0 10px;
  border:1px solid black;
  border-radius: 10px;
  height: 32px;
}

#register-footer > label > input {
  display: none;
}
#register-footer > label > div {
  position:absolute;
  width: 30px;
  height: 30px;
  border-radius: 10px;
  
  background-color: aqua;
  transform:translateY(-50%);
  top: 50%;
  left:0;
  transition: 0.3s;
}


#register-footer > label >input:checked + div {
  left: 100%;
  transform: translate(-100%,-50%);
  
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