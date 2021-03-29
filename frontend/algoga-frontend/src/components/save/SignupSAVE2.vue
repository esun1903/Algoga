<template>
  <div id="sign-up-save2">
    <div class="sign-up-page">
      <div class="sign-up-left">
        <h1 style='color:white' @click='selectSignup(-1)'>Signup</h1>   
        <div>
          <div @click='selectSignup(0)'>
            <div>
              <i class="far fa-envelope-open"></i>
              <span>E-mail</span>     
              <transition>
                <i class="fas fa-check" v-show='false'></i>         
              </transition>
            </div>            
          </div>
          <div @click='selectSignup(1)'>
            <div>
              <i class="fas fa-key"></i>
              <span>Password</span>
            </div>
          </div>
          <div @click='selectSignup(2)'>
            <div>
              <i class="fas fa-user"></i>
              <span>Nickname</span>
            </div>
          </div>
          <div @click='selectSignup(3)'>
            <div>
              
              <span>/&lt;&gt; BOJ</span>
            </div>
          </div>
          <div @click='selectSignup(4)'>
            <div>
              
              <span>START ALGOGA!</span>
            </div>
          </div>
        </div>
      </div>
      <div class="sign-up-right">
        <SignupSection :selectedIdx = 'selectedIdx' @changState='changeState'/>
      </div>

    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import SignupSection from '@/components/Signup/SignupSection'

export default {
  name:'SignupSAV2',
  components:{
    SignupSection,
  },
  data:function(){
    return {
      selectedIdx: -1,
      check: {
        email:false,
        password:false,
        passwordConfirm:false,
        bake_id:false,
        nickname:false,
      }

    }
  },
  methods:{
    closed:function(){
      this.$emit("closed")
    },
    selectSignup:function(idx){
      this.selectedIdx = idx
      const rightBox = document.querySelector('.sign-up-right')
      const leftBoxDivs = document.querySelectorAll('.sign-up-left > div >div')
      const colors = ['','brown','red','blue','green']
      let i = 0
      let colorIdx = _.random(4,1)      
      document.documentElement.style.setProperty('--signup-line', `${colors[colorIdx]}`);
      rightBox.style.border=`5px solid ${colors[colorIdx]}`
      rightBox.style.borderLeft=`none`
      leftBoxDivs.forEach(target => {
        if (this.selectedIdx == i) {
          target.classList.add('selected')
          target.classList.remove('unSelected')
        } else {
          if (target.classList.contains('selected')) {
            target.classList.remove('selected')
            target.classList.add('unSelected')
          } 
          
        }
        i += 1
      })
    },
    changeState:function(data){
      data
    },

    
  },
  mounted(){
    const signUp = document.querySelector('#sign-up')
    const divBack = document.createElement('div')
    
    
    const leftBoxDivs = document.querySelectorAll('.sign-up-left > div >div')
    
    const that =this


    leftBoxDivs.forEach(t=>{t.classList.add('unSelected')})

    divBack.addEventListener('click',function(){
      that.closed()
    })
    
    divBack.classList = 'sign-up-back'
    signUp.appendChild(divBack)

      
    

    

  }
}
</script>

<style scope>
@keyframes selectAnimation {
  0% {
    border:1px solid var(--signup-line);
    border-right: none;
    border-top-left-radius: 0px;
    border-bottom-left-radius: 0px;
  }
  100% {
    border:5px solid var(--signup-line);
    border-right: none;
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
  }
}



.sign-up-left {
  width: 30%; height:100%;
  background-color: var(--signup-line);  
  text-align: center;  
  color:black;  
}

.sign-up-right {
  width: 70%; height:calc(100%-10px);
  background-color: ivory;  
  border: 5px solid var(--signup-line);  
  border-left: none;
  transition:.3s;

  
  /* background-color: ; */
}

.sign-up-left > div {  
  height:86.6%;
  display:flex; flex-direction: column;
  justify-content: space-between;  
  font-size: 1.2rem;  
}


.sign-up-left > div > div {
  display:flex;
  align-items: center;
  justify-content: space-around;
  background-color: ivory;  
  border-left: none;
  height:100%;
  cursor:pointer;
}

#sign-up svg {
  margin-right: 10px;
}

.unSelected {
  border-right: 5px solid var(--signup-line);
  transition: ease-in 0.2s;
}
.selected {  
  animation: selectAnimation 0.2s ease-out forwards;
  justify-content: right;
}




</style>