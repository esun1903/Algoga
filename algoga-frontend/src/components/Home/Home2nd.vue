<template>
  <div id="home-2nd">
    <div>
      <div>        
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name:"Home2nd",
  data:function(){
    return {
    }
  },
  methods:{
    

  },
  mounted(){
   
  },
  created(){
  
  }

}
</script>
<style>

#home-2nd {  
  min-height: 500px;  
  
}
#home-2nd > div:nth-child(1) {
  overflow: hidden;
  position:relative;
  min-height: 500px;  
}
#home-2nd > div:nth-child(1)::before {
  position:absolute;
  content: '';
  width:150%;height:100%;
  top: 20%;
  background-color: black;
  z-index: 0;
  transform: rotate(-5deg);
  
}
#home-2nd > div:nth-child(1) > div:nth-child(1) {
  position:absolute;
  top:45%;
  width:100%;
  height:100%;
  background-color: black;
}

</style>