<template>
  <div id='feed'>
    <div @click='closeFeed'>
      <span>
          <i class="fas fa-times"></i>
      </span>
    </div>
    <h3>알림</h3>
    <div v-for="(idx,user) in users" :key='idx' id='feed-content'> 
      <div>
        <img src="data:image/jpeg;base64,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" alt="">
      </div>
      <div>
        <div>{{user}}님이 OO을 했습니다.</div>
        <p id='feed-date'>1주전</p>
      </div>
      <div id ='feed-menu'>
        <span>
          <i class="fas fa-ellipsis-h"></i>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name : 'Feed',
    props :[
        'feedOpened' 
    ],
    methods : {
        closeFeed : function(){
                this.$emit('closeFeed')
            }
    },
    data : function(){
      return {
        users : [
          1,2
        ]
      }
    }
}
</script>

<style>
#feed{
    width: 350px;
    position: absolute;
    bottom: 0px;
    right: 0px;
    z-index: 100000;
    height: 100%;
    background-color: rgb(255, 255, 255);
    transition: all 1s;
    box-shadow: -1px 0 0 0 rgb(37 40 47 / 10%);
}
#feed > div:nth-child(1){
    margin: 0;
    color: rgba(37, 40, 47, 0.65);
    border-radius: 22px;
    float: right;
    margin-right: 10px;
    margin-top: 25px;
}
#feed > div:nth-child(1) > span{
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    padding: 4px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
}
#feed > div:nth-child(1):hover{
    cursor: pointer;
}
#feed > div:nth-child(1):hover > span{
    background-color: rgba(202, 202, 202, 0.822);
    color: rgba(37, 40, 47, 0.411);
}
#feed > h3{
  padding-bottom: 15px;
  margin: 30px 0 20px 15px;
  font-size: 1.8rem;
  box-shadow: 0 1px 0 0 rgb(37 40 47 / 10%);
}
#feed-content{
  display: flex;
  align-items: center;
  margin: 5px;
  border-radius: 10px;
  height: 70px;
  position: relative;
}
#feed-content:hover{
  cursor: pointer;
  background-color: rgba(236, 236, 236, 0.568);
}
#feed-content>div:nth-child(1){
  margin-left: 10px;
  margin-right: 10px;
}
#feed-content > div> img{
  width: 55px;
  height: 55px;
  border-radius: 50%;
}
#feed-content > div:nth-child(2) > div{
  height: 50%;
  font-size: 0.9rem;
}

#feed-date{
  font-size: 0.8rem;
  color: #1876f2;
}
#feed-content:hover > #feed-menu{
  display: inherit;
}
#feed-menu{
  display: none;
  position: absolute;
  top: 50%;
  right: 0px;
  transform : translate(-50%,-50%);
  border-radius: 50%;
  padding: 6px;
  background-color: rgb(255, 255, 255);
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 16%);
}
#feed-menu > span{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 25px;
  height: 25px;  
}
#feed-menu:hover{
  background-color: rgba(255, 255, 255, 0.568);
}
</style>