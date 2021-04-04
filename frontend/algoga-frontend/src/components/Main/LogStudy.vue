<template>
  <div id="log-study">
    <header>
      TITLE (ex. LOG of User's Study and Save)
    </header>
    
    <div>
      <div class="one-week" v-for = "(c,jdx) in data" :key="jdx">
        <div v-for = "(d,idx) in [1,2,3,4,5,'cpp','python']" :key="idx">          
          <div class = "one-day" :class="{'one-day-no-border':d<2&&jdx<10,'python':d==='python','cpp':d==='cpp'}" :title="message(d)">

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
    }

  },
  computed:{
    message(){
      return lang => {
        return `show message by using html title attribute and this lang is ${lang}`
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
  },
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
    console.log(this.data)


    console.log(startDate,registerDay,today,DateDiff)

    for (let i = 0; i<codeBoardUser.length; i++){
      console.log(codeBoardUser[i])
      let dateOfBoard = codeBoardUser[i].register_date
      let dateIdx = this.getDayDiff(startDate,dateOfBoard)-1
      console.log(dateIdx)
      if (this.data[dateIdx]) {
        this.data[dateIdx] += 1
      } else {
        this.data[dateIdx] = 1
      }

    
    }
    console.log('okay the upper is done')

    for (let i = 0; i<DateDiff-1 ; i++){
      console.log(DateDiff[i])
      if (!this.data[i]) {
        this.data[i] = 0
      }
    }
    console.log(this.data)
    
    
    





    


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
  border: 1px solid black;
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
  border: 0.1px solid black;
  border-radius: 5px;
  cursor:pointer;
}


.one-day-no-border {
  border: none;
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




</style>