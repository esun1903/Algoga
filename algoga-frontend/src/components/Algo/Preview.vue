<template>
  <div @click='goLink()' id='preview'>
    <div id='img-box'>
      <img  src="https://d2gd6pc034wcta.cloudfront.net/images/logo@2x.png" alt="">
    </div>
    <div id='description-box'>
      <p id='linkTitle'>{{title}}</p>
      <p>{{description}}</p>
      <p>{{link}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name : 'Preview',
  data : function(){
    return{
      bojLink :'',
      bojTitle :'',
      bojDct : '',
    }
  },
  props : {
    link : {
      type : String,
    },
    title : {
      type : String,
    },
    description : {
      type : String,
    },
  },
  created(){
    this.bojLink = this.link
    this.bojTitle = this.title
    this.bojDct = this.description
  },
  methods : {
    goLink : function(){
      let openNew = window.open(this.link,'newWindow')
      openNew.focus();
    }
  }
}
</script>

<style>
#preview{
  display: flex;
  margin: 0 auto 40px;
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
  width: 70%;
  height: 20vh;
}
#preview:hover{
  cursor: pointer;
  box-shadow: 1px 1px 5px 1px #5050503b inset;
}
#img-box{
  width: 50%;
  text-align: center;
  position: relative;
}
#img-box > img{
  width: 60%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
#description-box{
  width: 50%;
}
#description-box  *{
  width: 100%;
}
#description-box > p:nth-child(1){
  margin-top : 5vh;
}

#linkTitle{
  font-size: 1.8rem;
}
/* 반응형 */
@media (max-width : 788px) {
  #preview{
    display: block;
    box-sizing: content-box;
    height: 50vh;
  }
  #img-box{
    width : 100%;
    height: 30vh;
  } 
  #description-box{
    width : 100%;
    height: 20vh;
  } 
  #img-box > img{
    width: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);    
  }
}
</style>