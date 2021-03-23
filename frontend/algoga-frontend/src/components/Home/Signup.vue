<template>
  <div id="signup">
    <div>
      <header> 
        <h2>Signup</h2>
        <div @click="closed">
          <i class="far fa-times-circle"></i>
        </div>
      </header>

      <div>
        <label for="">Email Address</label><br>
        <input type="text">
      </div>
      <div>
        <label for="">Password</label><br>
        <input type="text">
      </div>
      <div>
        <label for="">Confirm Password</label><br>
        <input type="text">
      </div>
      <div>
        <label for="">Nickname</label><br>
        <input type="text">
      </div>
      <div>
        <label for="">BOJ</label><br>
        <input type="text">
      </div>
      <div>
        <label for="">Email</label><br>
        <input type="text">
      </div>
      <div>
        <button>SIGNUP BTN</button>
      </div>
    </div>

    <div @click="closed"></div>


  </div>
</template>

<script>
export default {
  name:"Signup",
  data:function(){
    return {

    }
  },
  methods:{
    closed:function(){
      this.$emit("closed")
    }
  }


}
</script>

<style>
#signup > div:nth-child(1) {
  position:fixed;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  width: 600px;
  height: 800px;
  background-color: white;  
  z-index: 1000;   
}

#signup > div:nth-child(1) > header {
  display: flex;
  align-items: center;
  justify-content: space-between;

}


#signup > div:nth-child(2) {
  background-color: var(--shadow-color);
  position: fixed;
  top:0;
  left:0;
  width: 100%;
  height:100%;
  z-index: 999;
}


</style>