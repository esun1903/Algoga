<template>
  <div id='home-navbar'>
    <nav>
      <div>
        <img src="../../assets/2.jpg" alt="" height="60px">        
        <div>
          <div>first link</div>
          <div>second link</div>
          <div>third link</div>
        </div>
      </div>
      <div>
        <a href="#">Signin</a>
        <a href="#">SignUp</a>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
    name : 'HomeNavbar'
}
</script>

<style>

#home-navbar {    
  position:sticky;
  top: 0px;
  width: 80vw;
  height: 60px;   
  margin:10px auto 0 auto;
  box-shadow: 0px 2px 5px var(--shadow-color);
  background-color: var(--back-color);  
  border-radius: 5px;  
}


#home-navbar > nav {
  display:flex;
  justify-content: space-between;
  align-items: center;
}

#home-navbar > nav > div:nth-child(1) {
  background-image: url("../../assets/2.jpg");
  background-repeat: no-repeat;
  display:flex;
}

#home-navbar > nav >div:nth-child(1) > div {  
  display:flex;
  background-color: var(--back-color);
  align-items: center;  
}

#home-navbar > nav >div:nth-child(1) > div > div {
  padding-left: 40px;
  
}

#home-navbar > nav > div:nth-child(2) > a{  
  color:var(--font-color);
  text-decoration: none;
  padding-right: 20px;
}



</style>