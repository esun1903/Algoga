<template>
    <div id='login'>
        <div id='loginModal' class='modal'>
            <span @click='closeLoginModal' class='closeModal'>das</span>
            <p>This is Modal</p>
        </div>
        <div @click='closeLoginModal' id='modalBack'>
        </div>
    </div>
</template>

<script>
export default {
    name : 'Login',
    methods :{
        closeLoginModal : function(){
            console.log('dsad')
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
  width: 100%;
  height: 500px;
  background-color: rgba(0, 0, 0, 0.253);
  transform: translate(-50%,-50%);
}
#loginModal{
  background-color: #fefefe;
  padding: 20px;
  border: 1px solid #888;
  width: 50%;
}
.closeModal{
  color: #aaa;
  float: right;
}
.closeModal:hover,
.closeModal:focus{
  color: black;
  text-decoration: none;
  cursor: pointer;
}
#modalBack{
  display: block;
  background-color: black;
  z-index: 999;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
}
</style>