<template>
  <div id='recommend'>
      <div class='recotype'>
        <img class='recoTypeImg' src="@/assets/goal.png" alt=""><span>1. To Higher Level</span>
      </div>
      <div
        v-for="(algo, idx) in toThree(recoByCorrect)"
        :key='idx'
      >
        <RecommendLink
            :algo = algo
        />
      </div>
      <div class='recotype'>
        <img class='recoTypeImg' src="@/assets/success.png" alt=""><span>2. Overcome the Failure</span>
      </div>
      <div
        v-for="(algo, idx2) in toThree(recoByInCorrect)"
        :key='idx2+3'
      >
        <RecommendLink
            :algo = algo
        />
      </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://j4a302.p.ssafy.io'
import RecommendLink from '@/components/Main/RecommendLink'

export default {
    name : 'Recommend',
    data : function(){
        return{
            recoByCorrect : [],
            recoByInCorrect : [],
        }
    },
    components : {
        RecommendLink
    },
    async mounted(){
        const userno = localStorage.getItem('userNo')
        await axios.get(`${SERVER_URL}/apps/v1/recommendByCorrect/${userno}`)
            .then(res => {
                this.recoByCorrect = res.data
            })
            .catch(err => {
                console.log(err)
            })
        await axios.get(`${SERVER_URL}/apps/v1/recommendByInCorrect/${userno}`)
            .then(res => {
                this.recoByInCorrect = res.data
            })
            .catch(err => {
                console.log(err)
            })
    },
    methods : {
        toThree : function(arr){
            if(arr.length >3){
                return arr.slice(0,3)
            }
            else{
                return arr
            }
        }
    }
}
</script>

<style>
.recotype{
    display: flex;
    align-items: center;
    padding: 10px 20px;
    border: 1.5px solid #c841607c;
    background-color: #fa7c9917;
    border-radius: 20px;
    margin-right: 20px;
    margin-top: 30px;

}
.recoTypeImg{
    width: 3rem;
    margin-right: 30px;
}
.recoTypeImg + span{
    font-weight: 600;
}
</style>