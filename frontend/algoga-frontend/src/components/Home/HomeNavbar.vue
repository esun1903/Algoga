<template>
  <div id='home-navbar'>
    <nav>
      <div>

      </div>
      <div>
        <span>무엇이</span>
        <span>들어갈지</span>
        <span>정해봅시다</span>

      </div>
      <div>
        
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
  top: 0;
  width: 100vw;
  height: 80px;   
  background-color: var(--test-color);
}

#home-navbar > nav {
  display:flex;
  justify-content: space-between;
  align-items: center;
}

#home-navbar > nav > div:nth-child(1) {
  background-image: "../../assets/2.jpg";
}

</style>