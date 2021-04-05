<template>
  <div id="log-study">
    <header>
            
    </header>
    
    <div>
      <div class="one-week" v-for = "(one_week_data,jdx) in week_data" :key="jdx">
        <div v-for = "(d,idx) in one_week_data" :key="idx">          
          <div class = "one-day" :class="{'one-day-no-border':d==='not_day','solved_1':d===1,'solved_2':d===2,'solved_3':d===3, 'solved_4':d>=4}" :title="message(jdx,idx)">            
          </div>
        </div>
      </div>
    </div>

    

  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name:"LogStudy",
  data: function(){
    return {
      check: [
      ],      
      allCodeBoard: [],
      data:[],
      week_data:[],
      first_day:-1,
      problemsData:[], // [problem_seq,codeboard_seq]
    }
  },
  methods: {
    getToday:function(){
      let today_origin = new Date()      
      let month = ''+(today_origin.getMonth()+1)
      let day = ''+today_origin.getDate()
      let year = today_origin.getFullYear()

      if (month.length<2) month = '0' +month
      if (day.length< 2 ) day = '0' + day
      return [year,month,day].join('-');
    },
    getDay:function(date){
      const week = new Array('Sun','Mon','Tue','Wed','Thu','Fri','Sat')
      const d = new Date(date).getDay()
      const startDateLabel = week[d]
      return [startDateLabel, d]
    },
    getDayDiff:function(s,e){
      let day1 = s instanceof Date ? s : new Date(s)
      let day2 = e instanceof Date ? e : new Date(e)

      day1 = new Date(day1.getFullYear(), day1.getMonth(),day1.getDate())
      day2 = new Date(day2.getFullYear(), day2.getMonth(),day2.getDate())

      let diff = Math.abs(day2.getTime() - day1.getTime());
      diff = Math.ceil(diff / (1000*3600*24))

      return diff+1
    },
    focusingLast:function(){
      const allDay = document.querySelectorAll('.one-day')
      console.log(allDay)
      console.log(allDay[allDay.legnth-1])
    }

  },
  computed:{
    message(){
      return (jdx,idx)=> {
        if (jdx === 40 && idx ===this.first_day) {
          return 'You create this account'
        } else if (jdx <40){
          return 'You did not create account'
        } else {  
          return `You solved ${this.week_data[jdx][idx]} problems.`
        }
      }
    }
  },
  mounted(){
    // mosue drag    
    const slider = document.querySelector("#log-study > div")
    let isMouseDown = false
    let startX, scrollLeft;

    slider.addEventListener('mousedown', (event) => {
      isMouseDown = true;
      startX = event.pageX - slider.offsetLeft
      scrollLeft = slider.scrollLeft

    })

    slider.addEventListener('mouseleave',() => {
      isMouseDown = false
    })

    slider.addEventListener('mouseup',() => {
      isMouseDown = false
    })

    slider.addEventListener('mousemove',(event) => {
      if (!isMouseDown) return
      event.preventDefault()
      const x = event.pageX - slider.offsetLeft
      const walk = (x-startX) * 1
      slider.scrollLeft = scrollLeft - walk
    })  

  }
  ,
  async created(){
    for (let i = 0; i<50;i++){
      this.check.push(i)
    }

    const userEmail = this.$route.params.nickname
    let codeBoardUser = []

    await axios.get(`${SERVER_URL}/apps/v1/codeBoardUser/${userEmail}`)
      .then(res => {
        codeBoardUser = res.data
      })
      .catch(err=>{
        console.log(err)
      })
    
    const registerDate = localStorage.getItem('register_date')
    const startDate = registerDate.split('T')[0] //startDate mean the date of creat id
    const registerDay = this.getDay(startDate) // 가입한날의 요일 -> 이 데이터는 잔디심는거의 시작점을 잡아주는 역할
    const today = this.getToday()
    const DateDiff = this.getDayDiff(startDate,today)

    this.data = new Array(DateDiff)
    this.problemsData = new Array(DateDiff)
    for (let i = 0; i<codeBoardUser.length; i++){         
      let dateOfBoard = codeBoardUser[i].register_date.split('T')[0]
      let dateIdx = this.getDayDiff(startDate,dateOfBoard)-1     
      let problemData = new Array()      
      let title = ''
      let number = -1

      await axios.get(`${SERVER_URL}/apps/v1/Problem/${codeBoardUser[i].problem_seq}`)
        .then(res=>{  
          title = res.data.name                  
          number = res.data.number 
          

        })


      problemData.push(codeBoardUser[i].seq,codeBoardUser[i].language,codeBoardUser[i].problem_seq,title,number)
      if (this.problemsData[dateIdx]) {
        this.problemsData[dateIdx].push(problemData)
      } else {
        this.problemsData[dateIdx] = new Array(1).fill(problemData)
      }

      if (this.data[dateIdx]) {
        this.data[dateIdx] += 1
      } else {
        this.data[dateIdx] = 1
        
      }

    
    }    

    for (let i = 0; i<DateDiff ; i++){     
      if (!this.data[i]) {
        this.data[i] = 0
      }
    }    


    for (let i = 0; i<40; i++) {
      let weekArray = new Array(7).fill(0)
      this.week_data.push(weekArray)
    }
    
    
    let register_week = new Array()
    let first_week_last_idx = -1
    for (let i = 0; i<registerDay[1];i++){
      register_week.push(0)
    }

    for (let i=0; i<7-registerDay[1];i++){
      register_week.push(this.data[i])
      first_week_last_idx = i
    }

    this.week_data.push(register_week) // 첫주 저장
    
    let current_idx = first_week_last_idx+1
    for (let i =0; i<parseInt((this.data.length-first_week_last_idx+1)/7)+1;i++){
      let save_list = []
      for (let j=0; j<7; j++){
        if (this.data.length > current_idx+j){
          save_list.push(this.data[current_idx+j])
        } else {
          save_list.push('not_day')
        }
      }
      current_idx += 7
      this.week_data.push(save_list)
    }
    

    this.first_day = registerDay[1]    
    this.$emit('userData',{'data1':this.data,'data2':this.problemsData})

    console.log(this.problemsData)

  },
}
</script>

<style>
#log-study {
  padding: 10px;  
  width: 100%;
  border: 1px solid black;   
}

#log-study > div {
  display: flex;
  width: 1000px;
  overflow:auto;
  /* border: 1px solid black; */
}


#log-study > div::-webkit-scrollbar {
  display:none;
}

.one-week {
  height: 194px;
  width: 25px;
  padding: 2px;
  margin: auto 0;
  display:flex;
  flex-direction: column;
  justify-content: space-around;
}

.one-day {
  width:19.6px;
  height:20px;
  /* border: 0.1px solid black; */
  border-radius: 5px;
  cursor:pointer;
  background-color: rgba(0,0,0,0.1);
}


.one-day-no-border {
  background-color: rgba(0,0,0,0);
}

.python {
  background-color: blue;
}

.cpp {
  background-color: grey;
}

.java {
  background-color: hotpink;
}

.solved_1 {
  background-color:chartreuse;
  opacity: 0.25;
}
.solved_2 {
  background-color:chartreuse;
  opacity: 0.5;
}
.solved_3 {
  background-color:chartreuse;
  opacity: 0.75;
}
.solved_4 {
  background-color:chartreuse;
  opacity: 1;
}




</style>