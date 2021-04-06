<template>
  <div id="code-highlighter" >    
    <vue-code-highlight language='javascript'>
      {{code}}      
    </vue-code-highlight>
    <div v-highlight>      
    </div>
  </div>
</template>

<script>
// import CodeHighlight from "vue-code-highlight/src/CodeHighlight.vue"
import {component as VueCodeHighlight} from "vue-code-highlight"
import "vue-code-highlight/themes/prism-okaidia.css"

export default {
  name:'CodeHighlighter',
  components:{
    VueCodeHighlight
  },
  props:{
    code:String,
  }
}
</script>

<style>
#code-highlighter {  
  margin: 20px auto;
}

</style>