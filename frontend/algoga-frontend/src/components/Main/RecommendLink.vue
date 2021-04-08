<template>
  <div @click='goLink()' id='recobox'>
    <div>
      <p id='recotitle'>No.{{algo.number}} {{bojTitle}}</p>
      <p id='recotype'>{{algo.algorithms}}</p>
      <p id='recolv'>{{bojDct}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name : 'RecommendPreview',
  data : function(){
    return{
      bojLink :'',
      bojTitle :'',
      bojDct : '',
    }
  },
  props : {
    algo : {
      type : Object,
    },
  },
  mounted(){
    this.bojLink = `https://www.acmicpc.net/problem/${this.algo.number}`
    this.bojTitle = this.algo.name
    this.bojDct = `Lv.${this.algo.level} / correct_rate : ${this.algo.correct_rate}%`
  },
  methods : {
    goLink : function(){
      this.$router.push({
        name : 'Problem',
        params : this.algo,
        query : {no : this.algo.seq}
      })
    }
  }
}
</script>

<style>
#recobox{
    box-shadow: 0 2px 6px 0 rgb(0 0 0 / 10%);
    border-radius: 10px;
    padding: 8px 20px;
    margin : 8px 20px 8px 0;
}
#recobox:hover{
    background-color: rgba(236, 236, 236, 0.568);
    cursor: pointer;
}
#recotitle{
    margin : 5px 0;
    padding-bottom: 5px;
    font-size: 0.8rem;
    font-weight: 500;
    text-overflow: ellipsis;
    max-width: 100%;
    white-space: nowrap;
    overflow: hidden;
    box-shadow: 0 1px 0 0 rgb(37 40 47 / 20%);
}
#recotype{
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    margin-bottom: 3px;
    font-size: 0.7rem;
}
#recolv{
  font-size: 0.6rem;
}
</style>