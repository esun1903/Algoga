<template>
    <div id="mode-btn" >            
        <label for="mode-btn-checkbox">
            <input id="mode-btn-checkbox" type="checkbox">
            <div @click = "modeChange"> 
                <i class="fas fa-moon"></i>   
            </div>

        </label>
    </div>
</template>

<script>
export default {
    name:"ModeBtn",
    data:function(){
        return {
            mode:'light'
        }
    },
    methods:{
        modeChange:function(){
            if (this.mode ==='light') {
                this.mode = 'dark'
            } else {
                this.mode = 'light'
            }
        }
    },
    watch:{
        mode:function(){            
            const btn = document.querySelector('#mode-btn-checkbox+div')
            
            let iMoon = document.createElement('i')
            let iBulb = document.createElement('i')

            iMoon.classList.add('fas')
            iMoon.classList.add('fa-moon')
            iBulb.classList.add('far')
            iBulb.classList.add('fa-lightbulb')

            if (this.mode==='light') {
                document.documentElement.style.setProperty('--font-color', 'black');
                document.documentElement.style.setProperty('--back-color', 'white');
                document.documentElement.style.setProperty('--shadow-color', 'rgba(0,0,0,0.5)');
                document.documentElement.style.setProperty('--test-color', 'red');
                document.documentElement.style.setProperty('--font-color2', 'white');
                
                let removeI = document.querySelector('#mode-btn-checkbox+div > svg')                
                if (removeI) {
                    removeI.remove()
                }
                btn.appendChild(iMoon)


            } else {
                document.documentElement.style.setProperty('--font-color', 'white');
                document.documentElement.style.setProperty('--back-color', 'black');
                document.documentElement.style.setProperty('--shadow-color', 'white');
                document.documentElement.style.setProperty('--test-color', 'blue');
                document.documentElement.style.setProperty('--font-color2', 'white');
                let removeI = document.querySelector('#mode-btn-checkbox+div > svg')
                if (removeI) {
                    removeI.remove()
                }
                btn.appendChild(iBulb)
            }
        }
    }
    
}
</script>

<style>

#mode-btn {
    position:fixed;
    bottom: 50px;    
    right:100px;
    width: 55px;
    height: 50px;    
    border-radius: 50px;
    transition:1s;
    /* background-color: var(--font-color); */
    /* border:1px solid var(--shadow-color); */
    background-color: rgba(255,255,255,0.4);
}

#mode-btn-checkbox {
    visibility:hidden;
}

#mode-btn-checkbox+div{
    position:absolute;
    top:50%;
    left:0%;
    transform:translate(5%,-50%);
    width: 50px;
    height: 45px;
    border-radius: 100%;
    transition:1s;
    cursor:pointer;
    background-color: var(--font-color);    
    display:flex;
    justify-content: center;
    align-items: center;    
}

/* #mode-btn-checkbox:checked + div {
    left:100%;
    transform:translate(-100%,-50%)
}
#mode-btn-checkbox:checked + div:hover {
    background-color: black;
} */


.fa-moon, .fa-lightbulb  {
    transition: 0.3s;
    font-size: 1.5rem;
}
#mode-btn-checkbox + div > div:nth-child(1) {
    transform: rotate(-30deg);
}

#mode-btn-checkbox + div:hover .fa-moon { color:yellow}
#mode-btn-checkbox + div:hover .fa-lightbulb {color:yellow}



</style>