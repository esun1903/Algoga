<template>
  <div id="home-2ndsave">
    <div data-aos='fade-up'>
      <h2>이런 분들에게 추천 드립니다.</h2>
    </div>
    <div>
      <div data-aos="fade-up">1</div>
      <div data-aos="fade-up"
     data-aos-anchor-placement="top-center"> 2</div>
      <div data-aos="fade-down"
     data-aos-easing="linear"
     data-aos-duration="1500">3</div>
    </div>

  </div>
</template>

<script>
export default {
  name:"Home2ndsave",
  data:function(){
    return {
    }
  },
  methods:{
    reSizing:function(){
      const divs = document.querySelectorAll('#home-2nd > div:nth-child(2) > div')
      if (screen.width > 1000 ){
        let i = 0
        divs.forEach((d)=>{          
          d.style.height = `${d.clientWidth}px`          
          if (i==1) {
            d.style.margin = "0 -2%"
            d.classList.add('second-circle')
          } else if (i == 0) {
            d.classList.add('first-circle')
          } else {
            d.classList.add('third-circle')
          }

          i += 1
        })
      }
    }

  },
  mounted(){
    this.reSizing()
  },
  created(){
    const that = this
    window.addEventListener('resize',function(){that.reSizing()})
  }

}
</script>

<style>
#home-2ndsave {
  width:100%;  
  text-align: center; 
  background-color: rgb(136, 135, 135);
  color:white;
  padding: 50px 0;
}



#home-2ndsave> div:nth-child(2) {
  display:flex;    
  justify-content: center;
  align-items: center;
  margin: 50px auto;
  max-width: 1200px;
  
}
#home-2ndsave > div:nth-child(2) > div {
  width: 30%;  
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.first-circle {
  
  background-color: hsla(0, 100%, 50%, 0.397);
}
.second-circle {
  
  background-color: rgba(255, 255, 0, 0.39);
}
.third-circle {  
  background-color: rgba(0, 128, 0, 0.404);
}


</style>