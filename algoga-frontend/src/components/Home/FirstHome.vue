<template>
  <div id="first-home">
    <div>
      <img src="../../assets/main.jpg" alt="">
      <div class="img-cover">
        <FontEffect :char="char"/>
        <!-- <ImgBoarderEffect /> -->
      </div>
    </div>
    <div>     
      <h1 class="animate__animated animate__fadeInUp animate__delay-1s">{{char2[0]}}</h1>
      <h3 class="animate__animated animate__fadeInUp animate__delay-1s">{{char2[1]}}</h3>
    </div>
    <div>
      <div data-aos='fade-right'></div>
      <div data-aos='fade-up'>
        <h2>알고가는 문제를 '잘' 추천해줍니다.</h2>
        <h4>나의 수준에 맞는 문제를 추천해줍니다. <br>자주 틀리는 유형의 문제를 추천해줍니다.</h4>
        
      </div>
    </div>
    <div>
      <div data-aos='fade-up'>
        <h2>알고가는 문제를 '잘' 정리해줍니다.</h2>
        <h4>풀었던 코드를 날짜별, 유형별로 정리 할 수 있습니다. <br> 이를 통해 알고리즘 노트를 작성해보세요. <br> 다른 사람의 코드를 보며 자유롭게 의견을 나누어 보세요.</h4> 
      </div>
      <div data-aos='fade-left'></div>
    </div>
  
  
  </div>
</template>

<script>
import FontEffect from "@/components/Effect/FontEffect"
// import ImgBoarderEffect from "@/components/Effect/ImgBoarderEffect"



export default {
  name:"FirstHome",
  components:{
    FontEffect,
    // ImgBoarderEffect,
  },
  methods:{
    resizing:function(){
      const firstHome = document.querySelector('#first-home')
      const screenHeight = window.innerHeight - firstHome.offsetTop
      const seconddiv = document.querySelector('#first-home > div:nth-child(2)')
      const imgCover = document.querySelector('.img-cover')
      const imgHeight = document.querySelector('#first-home > div > img').clientHeight
      const thirdDiv = document.querySelector('#first-home > div:nth-child(3)')
      const fourthDiv = document.querySelector('#first-home > div:nth-child(4)')

      if (imgHeight>500) {
        imgCover.style.height = '500px'
      } else {
        imgCover.style.height = `${imgHeight}px`
      }
      let secondHeight = 0
      if (screenHeight > 969) {
        // firstHome.style.height = '969px'
        secondHeight= 969 - imgCover.clientHeight
        
      } else {
        // firstHome.style.height = `${screenHeight}px`
        secondHeight= screenHeight -imgCover.clientHeight
      }
      seconddiv.style.height = `${secondHeight}px`
      thirdDiv.style.height = seconddiv.style.height
      fourthDiv.style.height = seconddiv.style.height
    }
  },
  data:function(){
    return {
      char:["당신을 위한 공식","ALGORITHM == ALGOGA"],
      char2:["알고가를 통해 학습해보세요!","알고가를 통해 문제를 추천받고, 정리할 수 있습니다."],
    }
  },
  mounted(){
    setTimeout(() => {
      this.resizing()    
    }, 1);
    
    const that = this
    window.addEventListener('resize',function(){      
      that.resizing()
    })
  },  
  created(){
  } 

}
</script>

<style>
#first-home {
  margin-top: 30px;    
  color:var(--font-color);
  text-align: center;
}
#first-home > div:nth-child(1):hover > img {width:101%;}

#first-home > div:nth-child(1) {
  position:relative;
  overflow: hidden;
  width:100%;
  min-height: 500px;  
  color:var(--font-color2);  
  background-color: var(--back-color);
  cursor:pointer;
}
#first-home > div > img {
  display:block;
  position:absolute;
  width:100%;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  transition: 0.3s;
}

.img-cover {
  position:absolute;
  top:0;
  left:0;
  width:100%;
  position:absolute;
  width:100%;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  /* height:100%; */
  background-color: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

#first-home > div:nth-child(2) {
  margin-top: 0px;
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-image: url('../../assets/first-back3.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
  overflow: auto;
  color:black;
  
} 

#first-home > div:nth-child(3) {
  display:flex;
  justify-content: space-around;
  text-align: right;
  align-items: center;
  background-color: #000340;
  color:white;  
} 
#first-home > div:nth-child(3) > div:nth-child(1) {
  background-image: url('../../assets/connection.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
  border:none;
  height: 100%;
  width:50%;
}

#first-home > div:nth-child(4) > div:nth-child(2) {
  background-image: url('../../assets/arrange.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
  border:none;
  height: 100%;
  width:50%;

}

#first-home > div:nth-child(4) {
  display:flex;
  justify-content: space-around;
  text-align: left;
  align-items: center;
  color:black;
} 



</style>