<template>
  <div id="boj-form">
    <div>
      <label for=""><i class='fas'></i> BOJ</label><br>
      <input v-model='data.boj' type="text" placeholder="BOJ아이디를 등록해주세요!" @input='bojInput'>
      <p :class="{'check-ok':check.boj,'check-no':!check.boj}">{{mes.boj}}</p>
      <br>
    </div>
    <div class='signup-btn-div'>
      <button @click='nextStage(-2)'>PREV</button>
      <button @click='nextStage(2)' :class="{'btn-check-ok':check.boj}">NEXT</button>
    </div>
  </div>
</template>



<script>
export default {
  name:'BojForm',
  data:function(){
    return {
      data:{
        boj:''
      },
      check:{
        boj:false
      },
      mes:{
        boj:'',
      }
    }
  },
  methods:{
    nextStage:function(idx){
      if (this.check.email === false) {return}
      this.$emit('nextStage',idx,this.data)
    },
    bojInput:function(event){
      const input = event.target.value
      if (!input) { 
        this.check.boj = false
        this.mes.boj = ""

        return }

      this.check.boj = true
      this.mes.boj= '입력완료'

    }
  }
}
</script>

