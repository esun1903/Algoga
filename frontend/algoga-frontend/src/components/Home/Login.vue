<template>
    <div id='login'>
        <div id='loginModal' class='modal'>
            <div class='modalTitle'>
                <h1>LOGIN</h1>
                <div @click='closeLoginModal'><i class="closeModal far fa-times-circle"></i></div>
            </div>
            <div class='loginForm'>
                <div>
                    <label for="userEmail">Email</label>
                    <input v-model="idInput" placeholder="UserEmail" id='userEmail' type="text">
                </div>
                <div>
                    <label for="password">Password</label>
                    <input v-model="passwordInput" placeholder="Password" id='password' type="password">
                </div>
                <div>
                    <label for="remember">Remember</label>
                    <input id='remember' type="checkbox">
                </div>
                <div>
                    <button>Login</button>
                </div>
            </div>
        </div>
        <div @click='closeLoginModal' id='modalBack'>
        </div>
    </div>
</template>

<script>
export default {
    name : 'Login',
    data : function(){
      return{
        idInput : '',
        passwordInput : '',
      }
    },
    methods :{
        closeLoginModal : function(){
            this.$emit('closed')
        },
    }
}
</script>

<style>
.modal{
  display: block;
  position: fixed;
  z-index: 10000;
  left: 50%;
  top: 50%;
  height: 500px;
  transform: translate(-50%,-50%);
}
#loginModal{
  background-color: #fefefe;
  border: 1px solid #888;
  width: 50%;
}
.closeModal{
  position: absolute;
  color: black;
  top: 15px;
  right: 20px;
  font-size: 20px;
}
.closeModal:hover,
.closeModal:focus{
  color: red;
  text-decoration: none;
  cursor: pointer;
}
#modalBack{
  display: block;
  background-color: var(--shadow-color);
  z-index: 999;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
}
.modalTitle{
    border-bottom: 1px solid var(--shadow-color);
}
.modalTitle > h1{
    margin: 20px 0 20px 0;
    text-align: center;
}
.loginForm{
    padding: 40px 80px;
}
</style>