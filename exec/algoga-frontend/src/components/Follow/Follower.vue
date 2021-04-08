<template>
  <div id="follow-comp">
    <div class="person-div" v-for="(person,idx) in follow" :key="idx">
      <div class='person-img'>
        <img :src="profileImage(person)" alt="" height='70px' width='70px'>
      </div>
      <div class='person-info'>
        <div>
          {{person.nickname}}
        </div>
        <div>
          <button @click='userMain(person)'><i class='fas fa-home'></i> Home</button>
          <button @click='changeFollow(person.seq)'>{{followStatus(person.seq)}}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'Follower',
  props:{
    follow:Array,
    status:Array,
  },
  data(){
    return {    
    }
  },
  methods:{
    userMain(person){
      this.$router.push({name:'Main',params:{nickname:person.email,userno:person.seq}})
    },
    changeFollow(user_seq){
      this.$emit('changeFollow',user_seq)
    }
  },
  computed:{
    profileImage(){
      return (person) => {        
        return `${person.profile_image}`
      }
    },
    followStatus(){
      return (idx)=>{
        if (this.status.includes(idx)){
          return 'Unfollow'
        }
        return 'Follow'
      }
    }
  },
  mounted(){    
  }
}
</script>

<style>
#follow-comp button:nth-child(1){
  background-color: rgba(83, 216, 30, 0.884);
}
#follow-comp button:nth-child(2){
  background-color: rgba(30, 42, 216, 0.644);
}

</style>