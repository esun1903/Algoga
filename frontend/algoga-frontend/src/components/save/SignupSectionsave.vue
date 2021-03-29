<template>
  <div id="signup-section">
    <div v-if="selectedIdx===-1">
      <h1 class='susection animate__animated animate__fadeIn'>ALGOGA</h1>
      <span class='susection animate__animated animate__zoomIn'>회원가입을 통해 알고리즘을 학습해보세요!</span>
    </div>
    <div v-else-if="selectedIdx === 0">
      <EmailForm />
    </div>
    <div v-else-if="selectedIdx === 1">
      <label for=""><i class="fas fa-key"></i>Password</label><br>
      <input type="text" v-model='userData.password'><br>
      <label for=""><i class="fas fa-key"></i>Confirm Password</label><br>
      <input type="text" v-model='passwordConfirm'>
    </div>
    <div v-else-if="selectedIdx === 2">
      <label for=""><i class="fas fa-user"></i>Nickname</label><br>
      <input type="text" v-model='userData.nickname'>
    </div>
    <div v-else-if="selectedIdx === 3">
      <label for="">/&lt;&gt; BOJ</label><br>
      <input type="text" v-model='userData.bake_id'>
    </div>
    <div v-else>
      <h1 class='susection animate__animated animate__fadeIn'>기입한 정보를 토대로 회원가입 마치시겠습니까?</h1>
    </div>
  </div>
</template>
<script>
import EmailForm from "@/components/Signup/EmailForm"

export default {
  name:'SingupSection',
  components:{
    EmailForm
  },
  data:function(){
    return {
      userData:{
        email:'',
        password:'',
        bake_id:'',
        nickname:'',
        profile_image:'profile image test null',
        register_date: "2021-03-25T11:22:05.954Z",
      },
      passwordConfirm:'',
      check:{
        email:false,
        password:false,
        passwordConfirm:false,
        bake_id:false,
        nickname:false,
      },
      message:{
        email:'이메일 형식을 확인해주세요'
      }
    }
  },
  props: {
    selectedIdx:Number,
  },
  methods:{
    

  },
}
</script>

<style scope>
.susection.animate__animtaed.animate_fadeIn {--animation-delay: .5s;}
.susection.animate__animtaed.animate_zoomIn {--animation-delay: .5s;}

#signup-section {position:relative;padding:20px; width:calc(100%-10px); height:100%;}
#signup-section > div {margin:0 auto; width:80%;}

#signup-section input {
  height: 2.5em;
  width: 20%;
  outline: none;
  border: none;
  border-bottom: 3px solid rgb(197, 185, 185);
  animation: suInputAni ease-in forwards 0.3s;
  margin-top: 10px;
  margin-bottom: 30px;
  background-color: rgba(0,0,0,0);
  transition:.3s;
}

#signup-section input:focus {
  border-color: blue;  
}

.signup-checked {
  border-color:greenyellow;
}
.text-false {
  color:red;
}
.text-true {
  color:green;

}


#signup-section > div {
  position:absolute;
  top:20%; left:50%;
  transform:translate(-50%,0%);
}
#signup-section > div > div {margin-top: 20px;}


@keyframes suInputAni {
  to {
    width: 70%;
  }
}





</style>