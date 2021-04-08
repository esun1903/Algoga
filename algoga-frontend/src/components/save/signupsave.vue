<template>
  <div id="signusave">
    <div>
      <header> 
        <h1>SIGNUP</h1>
        <div @click="closed" class='close-btn'>
          <i class="far fa-times-circle"></i>
        </div>
      </header>

      <div>
        <label for="">Email Address</label><br>
        <input type="text" v-model="data.email">
      </div>
      <div>
        <label for="">Password</label><br>
        <input type="text" v-model='data.password'>
      </div>
      <div>
        <label for="">Confirm Password</label><br>
        <input type="text" v-model='passwordConfirm'>
      </div>
      <div>
        <label for="">Nickname</label><br>
        <input type="text" v-model='data.nickname'>
      </div>
      <div>
        <label for="">BOJ</label><br>
        <input type="text" v-model='data.bake_id'>
      </div>
      <div>
        <label for="">Email</label><br>
        <input type="text">
      </div>
      <div>
        <button @click='signUp'>SIGNUP BTN</button>
      </div> 
    </div>

    <div @click="closed" class='sign-up-close-div'></div>


  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://j4a302.p.ssafy.io'


export default {
  name:"Signupsave",
  data:function(){
    return {
      data:{
        email:'',
        password:'',
        bake_id:'',
        nickname:'',
        profile_image:'profile image test null',
        register_date: "2021-03-25T11:22:05.954Z",
      },
      passwordConfirm:'',
    }
  },
  methods:{
    closed:function(){
      this.$emit("closed")
    },
    signUp:function(){
      axios.post(`${SERVER_URL}apps/v1/signUp`,this.data,{
        headers:{
          "Content-Type":'application/json'
        }
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  mounted(){
    // inputbox class 적용
    const inputBox = document.querySelectorAll('#signup input')
    const labels = document.querySelectorAll('#signup label')
    inputBox.forEach(box=>{box.classList.add('sign-up-inputBox')})
    labels.forEach(label => {label.classList.add('sign-up-label')})


  }


}
</script>

<style>
#signupsave > div:nth-child(1) {
  position:fixed;
  top:50%; left:50%;
  transform:translate(-50%,-50%);
  width: 800px;  height: 600px;
  background-color: white;  
  padding:10px;
  z-index: 10000;   
  border-radius: 10px;
}

#signupsave > div:nth-child(1) > header {
  display: flex;
  align-items: center;
  justify-content: left;
  margin-bottom: 20px;
}

.close-btn {
  position:absolute;
  top:0; right:0;
  font-size: 1.5rem;
  color:grey;
  transition: 0.3s;
}
.close-btn:hover {
  color:red;
  cursor:pointer;
}

.sign-up-close-div {
  background-color: var(--shadow-color);
  position: fixed;
  top:0;left:0;
  width: 100%; height:100%;
  z-index: 9999;
}

.sign-up-inputBox {
  border:none; border-bottom: 1px solid grey ;outline:none;  
  width: 30%; height: 30px;
  margin: 10px 0 20px;
  transition: 0.3s;

}



</style>