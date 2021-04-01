<template>
  <div id="user-form">
    <div>
      <label for=""><i class='fas fa-user'></i> Nickname</label><br>
      <input v-model='data.nickname' type="text" placeholder="닉네임을 입력해주세요" @input='nicknameInput' @keypress.enter='nextStage(2)'>
      <p :class="{'check-ok':check.nickname,'check-no':!check.nickname}">{{mes.nickname}}</p>
      <br>
    </div>
    <div class='signup-btn-div'>
      <button @click='nextStage(-2)'>PREV</button>
      <button @click='nextStage(2)' :class="{'btn-check-ok':check.nickname}">Finish</button>
    </div>
  </div>
</template>



<script>
export default {
  name:'UserForm',
  data:function(){
    return {
      data:{
        nickname:''
      },
      check:{
        nickname:false
      },
      mes:{
        nickname:'',
      }
    }
  },
  methods:{
    nextStage:function(idx){
      if (this.check.nicknmae === false && idx >0) {return}
      this.$emit('nextStage',idx,this.data)
    },
    nicknameInput:function(event){
      const input = event.target.value
      if (!input) { 
        this.check.nickname = false
        this.mes.nickname = ""

        return }

      this.check.nickname = true
      this.mes.nickname= '입력완료'

    }
  }
}
</script>

