<template>
  <div id="start-form">
    <div style='text-align:center;'>      
      <h2 class='animate__animated animate__fadeIn'>{{char[0]}}</h2>      
      <h2 class='animate__animated animate__fadeIn animate__delay-1s'>잠시후 메인페이지로 이동합니다.</h2>      
      <h2 class='animate__animated animate__fadeIn animate__delay-2s'>THANK YOU!</h2>      
    </div>
  </div>
</template>



<script>

export default {
  name:'StartForm',
  components:{

  },
  data:function(){
    return {
      char:['환영합니다']
    }
  },
  created(){
    setTimeout(() => {
      this.$router.push('main')
    }, 3000);
  }
  
}
</script>

