<template>
  <div id="signup-header">    
    <div v-for="(index,idx) in [0,1,2,3,4,5,6,7,8,9,10]" :key="idx">
      <div v-if='index%2 === 0'>
        <i :class='icons[index/2]'></i>
      </div>
      <div v-else></div>
      
    </div>
    
  </div>
</template>

<script>
export default {
  name:"SignupHeader",
  props:{
    nowIdx:Number,
  },
  data:function(){
    return {
      icons:['far fa-envelope-open','fas fa-key','fas fa-code','fas fa-user','far fa-envelope-open','fas'],
      mes:['이메일','비밀번호','BOJ','닉네임','시작']
    }
  },
  methods:{
    idxChange: function(){
      const headers = document.querySelectorAll('#signup-header>div>div')
      let i = 0
      headers.forEach(target => {
        if (i===this.nowIdx) {
          target.style.backgroundColor='blue'
          target.style.color='white'
          } else if (i < this.nowIdx) {
            target.style.backgroundColor='green'
            target.style.color='white'
          } else {
            target.style.backgroundColor = ''
            target.style.color='black'
          }
        i += 1
      })
    }
  },
  watch:{
    nowIdx:function(){      
      this.idxChange()
    }
  },
  mounted(){
    this.idxChange()
  }
}
</script>

<style>
#signup-header {width:70%; height:10%;margin:20px auto;transition: .3s;display:flex;justify-content: space-between;align-items: center;text-align: center;}


#signup-header > div:nth-child(odd) > div {width:50px;height:50px;border-radius: 50%;display:flex;justify-content: center;align-items: center;border:1px solid grey;transition:.3s;}
#signup-header > div:nth-child(2n) > div {width:calc(300px / 6);height: 3px;background-color:grey;transition: .3s;}


</style>