<template>
    <div id="font-effect">
        <h1 class='animate__animated animate__fadeIn' v-for="(string,idx) in char" :key='idx'>
            {{string}}            
        </h1>        
    </div>
</template>
<script>
export default {
    name:"FontEffect",
    props: {
        char:{String,Array},
    },
    mounted(){
        const h1 = document.querySelectorAll('#font-effect > h1')
        let delay_second = 0
        h1.forEach((h1_1)=>{
            delay_second += 1
            const delay_class = `animate__delay-${delay_second}s`
            h1_1.classList.add(delay_class)
        })
    }
}
</script>

<style>


</style>
