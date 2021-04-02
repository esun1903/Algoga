<template>
    <div id='login'>
        <div class="login-page">
          <h2 :class="fadein">SignIn</h2>
          <div>
            <i :class='user'></i>
            <input type="text" v-model='idInput' @input="statusChange" placeholder="User email"><br>
          </div>
          <div>
            <i :class='pw'></i>
            <input type="password" v-model='passwordInput' @keydown.enter="Login" @input="statusChange" placeholder="Password"><br>
          </div>
          <div :class='shake' v-if='loginStatus===false'> 
            <p>{{mes}}</p>
          </div>
          <div v-else>
            <button @click='Login'>SignIn</button>
          </div>          
          <button @click='test'>testsets</button>
        </div>
        <div class="sign-up-back" @click='closeLoginModal'></div>
    </div>
</template>

<script>
// import axios from 'axios'
// import Cookies from "universal-cookie"

// const cookies = new Cookies()

const SERVER_URL = process.env.VUE_APP_SERVER_URL
// const SERVER_URL = 'http://j4a302.p.ssafy.io:8000'
// axios.defaults.withCredentials = true;
// axios.defaults.xsrfCookieName = 'csrftoken'
// axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name : 'Login',
  data : function(){
    return{
      idInput : '',
      passwordInput : '',
      fadein: "animate__animated animate__fadeIn center",
      user: 'fas fa-user',
      pw: 'fas fa-lock',
      shake:'animate__animated animate__headShake',
      loginStatus:true,
      mes:'',
    }
  },
  methods :{
    closeLoginModal : function(){
      this.$emit('closed')
    },
    Login:function(){      
      // axios.get(`${SERVER_URL}/apps/v1/login/${this.idInput}/${this.passwordInput}`,{},{
      //   headers:{
      //     "Content-Type":"application/json",
      //     "X-CSRFToken":cookies.get('csrftoken')
      //   },
      //   credentials:"same-origin",
      // })
      //   .then(res => { 
      //     if(res.status !== 200){
      //       alert('로그인실패')
      //       return;
      //     }                    
      //     // console.log(res)
      //     localStorage.setItem('email',res.data[0].email)
      //     localStorage.setItem('userNo',res.data[0].seq)
      //     this.$router.push({name:'Main',params:{nickname:this.idInput}})
          
      //   })
      //   .catch(err=>{alert(err)})
      // fetch(`${SERVER_URL}/apps/v1/login/${this.idInput}/${this.passwordInput}`)
      //   .then(res => {
      //     return res.json()
      //   })
      //   .then(res=>{
      //     console.log(JSON.stringify(res))
      //   })
     

      fetch(`${SERVER_URL}/apps/v1/login/${this.idInput}/${this.passwordInput}`,{
        credentials:'same-origin',
      })
        .then(res => {
          return res.json()
        })
        .then(res => {
          console.log(JSON.stringify(res))
          // this.$router.push({name:'Main',params:{nickname:this.idInput}})
        })

    },
    test:function(){
      fetch(`${SERVER_URL}/apps/v1/sessionCheck>`,{credentials:'same-origin'})
        .then(res=>{
          return res.json()
        })
        .then(res=>{
          console.log(JSON.stringify(res))
        })
        .catch(err=>{
          console.log(err,'error!!!!!!!!!!!!!!!!!!!!!!!!')
          this.teststring = err.data
        })
    },
    statusChange:function(){
      this.loginStatus =true
    }
  },
  created(){
    const that = this
    window.addEventListener('keydown',function(event){
      if (event.key === 'Escape') {
        that.closeLoginModal()
      }
    })
  }
}
</script>

<style>
.login-page {
  position:fixed;
  top:50%; left:50%;
  transform:translate(-50%,-50%);
  width: 300px;  height: 400px;
  background-color: white;  
  z-index: 10000;   
  border-radius: 10px;
  overflow: hidden;  
  padding:50px;
}

.login-page > div:nth-child(2), .login-page>div:nth-child(3) {
  display:flex; justify-content: left;align-items: center;
  }
.login-page > div:nth-child(4) {
  display: flex;
  width: 90%;
  justify-content: flex-end;
  font-size: 0.5em;
  color:red;
}
.center { text-align: center;}

#login input {
  width: 0; height: 25px;
  margin: 30px 0;
  border: none; border-bottom: 1px solid grey;
  animation: inputLoginAni 0.3s ease-in forwards;
  animation-delay: 0.5s;
  opacity: 0;
  outline:none;
  vertical-align: bottom;
}

#login button {
  margin-top: -25px;
  border:none; outline:none;
  padding: 10px 20px;
  border-radius: 10px;
  background-color: #00bfff;
  color:white;
  cursor:pointer;
  font-family: Hack;
  font-size: 0.8rem;
}
@keyframes inputLoginAni {
  to {
    width: 80%;
    opacity: 1;
  } 
}

#login svg {
  display:inline-block;  
  margin-right: 10px;
  
}
</style>