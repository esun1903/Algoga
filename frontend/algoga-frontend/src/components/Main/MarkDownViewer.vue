<template>
  <div id="markdown-viewer" v-html="compileMarkdown" >

  </div>
</template>

<script>
import marked from "marked"

export default {
  name:'MarkDownViewer',
  props:{
    explanation:String
  },
  computed:{
    compileMarkdown:function(){
      if (!this.explanation){return ;}
      return marked(this.explanation,{sanitize:true})
    }
  },
}
</script>

<style>

</style>