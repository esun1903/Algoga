<template>
  <div id="history">
    
    <div>
      <div v-for="(data,idx) in dummy" :key="idx">
        <section style="display:flex; margin-left:-7px; margin-top:20px; align-items:center">
          <div style='width:10px; height:10px; background-color:black;border-radius:10px; border: 1px solid black;margin-right: 5px'></div>
          At {{data.data}} ... You solved {{data.solved}} .....
          <div>
            Show detail
          </div>
        </section>
        

      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:"History",
    methods:{

    },
    data:function(){
        return { 
            dummy: [
              {'data':'2021-03-23 Tue','solved':'3problems'},
              {'data':'2021-03-21 Sun','solved':'3problems'},
              {'data':'2021-03-20 Sat','solved':'3problems'},
            ]
        }
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
  background-color:  pink;
  margin-top: 20px;  
  width: 100%;
  padding: 10px;
  max-height: 200px;
  overflow: auto;  
  scroll-behavior: smooth;
}
#history::-webkit-scrollbar{
  display:none;
}

#history > div:nth-child(1) {
  text-align: left;
  margin-left:10px;
  border-left: 3px solid greenyellow;
  height: 1000px;
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

</style>