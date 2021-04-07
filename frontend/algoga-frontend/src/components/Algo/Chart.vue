<template>
    <GChart
        type = "ColumnChart"
        :data = data2
        :options = options2
    />
</template>

<script>
import { GChart } from 'vue-google-charts'
export default {
    name : 'Chart',
    components : {
        GChart
    },
    data : function(){
        return{
            ctype2 : '',
            data2 : [],
            options2 : {}
        }
    },
    props : {
        ctype : {
            type : String
        },
        data : {
            type : Array
        },
        options : {
            type : Object
        },
    },
    mounted(){
        this.ctype2 = this.ctype
        this.data2 = this.data
        this.options2 = this.options
    }
}
</script>

<style>

</style>