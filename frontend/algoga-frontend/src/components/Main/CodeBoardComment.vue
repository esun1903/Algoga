<template>
  <div id="code-board-comment">
    {{commentList}}
  </div>
</template>

<script>
export default {
  name:'CodeBoardComment',
  props: {
    commentList:Array,
  }
}
</script>

<style>
#code-board-comment {
  width: 80%;
  margin: 30px auto 10px;
}



</style>