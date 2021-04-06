<template>
  <div id="history">
    
    <div>
      <div v-for="(data,idx) in datas" :key="idx">
        <section class='history-section'>
          <div class='pointer'></div>
          <div>
            {{data}}
          </div>
        </section>        
        <div class='detail-problem' v-if='dataHistory[idx]!==0'>
          <div v-for="(dataProb,jdx) in dataList[idx]" :key='jdx' @click='routerCodeBoardDetail(dataProb[0])'>
            <span>[BOJ] {{dataProb[4]}}. {{dataProb[3]}}  {{dataProb[1]}}</span>
          </div>
        </div>
        <div class='detail-problem' v-else>
          한문제도안풀음!@
        </div>
      </div>
    </div>        
  </div>
</template>

<script>
export default {
    name:"History",
    props:{
      dataHistory:[Array],
      dataList:[Array],
    },
    data:function(){
        return {
            datas:[],
        }
    },
    methods:{
      routerCodeBoardDetail:function(codeBoard_seq){
        this.$router.push({name:'CodeBoardDetail',params:{'codeBoard_seq':codeBoard_seq}})
      }
    },
    watch:{
      dataHistory:function(){              
        this.datas = []
        const reg_date = localStorage.getItem('register_date').split('T')[0]        
        let week = new Array('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')  
        let month_name = new Array('January','February','March','April','May','June','July','August','September','October','November','December')
        
        let register_date = new Date(reg_date)

        for (let i = 0; i<this.dataHistory.length;i++){
          let new_date = new Date()
          let string_date = ''
          new_date.setDate(register_date.getDate()+this.dataHistory.length-i-1)

          let year = new_date.getFullYear()
          let month = new_date.getMonth()
          let day = new_date.getDate()          
          
          var d = new Date(`${year}-${month+1}-${day}`).getDay()

          string_date = week[d]+' '+`${day}`+' ' +month_name[month]+' '+ year + ' '+', ' +`You solved ${this.dataHistory[i]} problems`
          this.datas.push(string_date)
        }
      },
    },
    mounted(){
      let slider = document.querySelector('#history')
      let isMouseDown = false
      let toTopBtn = false
      let startY, scrollUp

      slider.addEventListener('mousedown',(event) => {
        isMouseDown = true
        startY = event.pageY - slider.offsetTop
        scrollUp = slider.scrollTop        
      })

      slider.addEventListener('mouseleave',()=>{isMouseDown=false})
      slider.addEventListener('mouseup',()=>{isMouseDown=false})

      slider.addEventListener('mousemove',(event)=>{
        if (!isMouseDown) return
        event.preventDefault()
        const y = event.pageY - slider.offsetTop
        const walk = (y-startY) * 1
        
        slider.scrollTop = scrollUp - walk
      })

      slider.addEventListener('scroll',()=>{
        if (slider.scrollTop > 50 && !toTopBtn) {
          toTopBtn = true
          const topBtn = document.createElement('div')          
          const left = slider.offsetLeft + slider.clientWidth - 60
          const top =  slider.offsetTop + slider.clientHeight - 60
        
          topBtn.classList.add('topBtn')
          topBtn.textContent = "toTopBtn"
          topBtn.style.left = `${left}px`
          topBtn.style.top = `${top}px`
          topBtn.addEventListener('click',function(){
            slider.scrollTop = 0
          })
          slider.appendChild(topBtn)
          
        } else if (slider.scrollTop < 50 && document.querySelector('.topBtn') ) {
          toTopBtn = false
          document.querySelector('.topBtn').remove()
        }

        
      })
    },

}
</script>

<style>
#history {  
  position:relative;
  background-color:  white;
  margin-top: 20px;  
  width: 100%;
  padding: 10px;
  max-height: 500px;
  overflow: auto;  
  scroll-behavior: smooth;
}
#history::-webkit-scrollbar{
  display:none;
}

#history > div:nth-child(1) {
  text-align: left;
  margin-left:10px;
  border-left: 3px solid rgba(0,0,0,0.5);  
}


.history-section {
  display:flex; 
  margin-left:-6px; 
  margin-top:20px; 
  align-items:center
}

.topBtn {
  position:fixed;  
  width: 50px;
  height: 50px;
  border:1px solid black;
  border-radius: 100%;
  background-color: white;
  cursor:pointer;
}

.pointer {
  width:10px; 
  height:10px; 
  background-color:rgb(94, 185, 41);
  border-radius:10px;   
  margin-right: 5px
}


.detail-problem {
  width: 80%;
  padding: 10px 20px;
  /* height: 100px; */
  margin: 10px auto 30px;
  background-color: rgb(226, 223, 223);
}

.detail-problem span {
  display:inline-block;
  margin: 5px 0;
  cursor:pointer;  
}
.detail-problem span:hover{
  text-decoration-line: underline;
}


</style>