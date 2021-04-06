<template>
  <div>
    <GChart
      type="PieChart"
      :data="chartdata"
      :options="options"
    />
  </div>  
</template>
<script>
import { GChart } from 'vue-google-charts'


export default {
  components : {
    GChart
  },
  props: {
    chartdata: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
}
</script>

<style>

</style>