<template>
  <div id="log-study">
    <header>
      TITLE (ex. LOG of User's Study and Save)
    </header>
    
    <div>
      <div class="one-week" v-for = "(c,jdx) in check" :key="jdx">
        <div v-for = "(d,idx) in [1,2,3,4,5,'cpp','python']" :key="idx">          
          <div class = "one-day" :class="{'one-day-no-border':d<2&&jdx<10,'python':d==='python','cpp':d==='cpp'}" :title="message(d)">

          </div>
        </div>
      </div>
    </div>

    

  </div>
</template>

<script>
export default {
  name:"LogStudy",
  data: function(){
    return {
      check: [
      ],      
    }
  },
  methods: {

  },
  computed:{
    message(){
      return lang => {
        return `show message by using html title attribute and this lang is ${lang}`
      }
    }
  },
  created(){
    for (let i = 0; i<50;i++){
      this.check.push(i)
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