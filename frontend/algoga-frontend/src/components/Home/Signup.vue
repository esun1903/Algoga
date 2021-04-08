<template>
  <div id="signup">
    <div class="sign-up-page">
      <SignupHeader :nowIdx = 'nowIdx' />
      <SignupSection :nowIdx = 'nowIdx' @nextStage='nextStage'/>
    </div>
    <div class="sign-up-back" @click='closeSignup'></div>
  </div>
</template>

<script>
import SignupHeader from "@/components/Signup/SignupHeader"
import SignupSection from "@/components/Signup/SignupSection.vue"

export default {
  name: "Signup",
  components:{
    SignupHeader,
    SignupSection,
  },
  data:function(){
    return {
      nowIdx: 0,
    }
  },
  methods:{
    closeSignup:function(){      
      this.$emit("closed")
    },
    nextStage:function(idx){
      if (this.nowIdx === 10) {return}      
      this.nowIdx += idx      
    },
  },
  mounted(){
   
  },
  created(){
    const that = this
    window.addEventListener('keydown',function(event){
      if (event.key === 'Escape') {
        that.closeSignup()
      }
    })
  }


}
</script>

<style>

.sign-up-page {
  position:fixed;
  top:50%; left:50%;
  transform:translate(-50%,-50%);
  width: 800px;  height: 600px;
  background-color: white;  
  z-index: 10000;   
  border-radius: 10px;
  overflow: hidden;  
}

.sign-up-back {
  background-color: var(--shadow-color);
  position: fixed;
  top:0;left:0;
  width: 100%; height:100%;
  z-index: 9999;

}

</style>