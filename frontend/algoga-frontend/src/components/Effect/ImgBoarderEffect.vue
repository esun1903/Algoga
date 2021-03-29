<template>
  <div id="img-boarder-effect">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
  </div>
</template>

<script>
export default {
  name: "ImgBoarderEffect"
}
</script>

<style>
#img-boarder-effect {
  position:absolute;
  width:100%;height: 100%;
  top:0;left:0;  
  overflow:hidden;
  }
#img-boarder-effect > span:nth-child(1) {
  position:absolute; 
  top:0; left:0;
  width: 100%; height: 5px;  
  transform:translateX(-100%);
  background: linear-gradient(45deg,rgba(0,0,0,.5),red);
  animation: animationBorder1 linear infinite 0.5s;
  
}

#img-boarder-effect > span:nth-child(2){
  position:absolute;
  top:0;right:0px;
  width: 5px; height: 100%;  
  background: linear-gradient(45deg,rgba(0,0,0,.5),red);
  transform:translateY(-100%);
  animation: animationBorder2 linear infinite .5s;
  animation-delay: 1s;
}
#img-boarder-effect > span:nth-child(3){
  position:absolute;
  bottom:0;right:0;
  width:100%;height:5px;  
  transform:translateX(100%);
  animation: animationBorder1 linear infinite .5s;
  animation-delay: 2s;
  background: linear-gradient(45deg,red,rgba(0,0,0,.5))
}
#img-boarder-effect > span:nth-child(4){
  position:absolute;
  bottom:0;left:0;  
  width: 5px; height: 100%;
  background: linear-gradient(45deg,red,rgba(0,0,0,.5));
  transform:translateY(100%);
  animation: animationBorder2 linear infinite .5s;
  animation-delay: 3s;
}

@keyframes animationBorder1 {
  to {
    transform:translateX(100%)
  }
}
@keyframes animationBorder2 {
  to {
    transform:translateY(100%)
  }
}





</style>
