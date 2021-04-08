<template>
  <div id='list'>
    <MainNavbar />
    <!-- 검색 -->
    <div id='search'>
      <form v-on:submit.prevent>
        <select v-model="findType" name="findType" id="findtype">
          <option selected value="Title">Title</option>
          <option value="No">No</option>
          <option value="Type">Type</option>
        </select>
      </form>
      <form v-on:submit.prevent>
        <input @keypress.enter="searchKeyword" v-model="findInput" id='keyword' type="text" maxlength="30">
      </form>
      <button @click='searchKeyword' id='searchIcon'  class='searchBtn'><i class="fas fa-search"></i></button>
      <button @click='filter' :class='{btnClicked : filtered}' id='filterIcon' class='searchBtn'><i class="fas fa-sort-amount-down"></i></button>
      <button class='searchBtn' id='rmCondition' v-show="showBtn">
        <span @click='rmCondition'>조건 초기화</span>
      </button>
    </div>
    <!-- 타입 버튼 필터링 -->
    <div id='filterByType'>
      <button
        @click='btnPress(idx)'
        class='typeIcon'
        v-for="(type, idx) in types" :key="idx"
        :class="{btnPressed :typesClicked[idx]}">
        {{type}}
      </button>
    </div>
    <!-- 세부 필터링 -->
    <transition name='slide'>
      <div v-show="filtered" id='filterSection'>
        <p>Filter</p>
        <div id='filterClose' @click='filter'>
          <span>
              <i class="fas fa-times"></i>
          </span>
        </div>
        <!-- 레벨 -->
        <div class='filterContent'>
          <p>Level</p>
          <div>
            <button class='manulBtn' :class='{manulBtnUnable : selectedLv == 0 }' @click='levelChange(1)'><span>-</span></button>
              <span>{{selectedLv}}</span>
            <button :class='{manulBtnUnable : selectedLv == 9 }' class='manulBtn' @click='levelChange(2)'><span>+</span></button>
          </div>
        </div>
        <!-- 타입 -->
        <div class='filterContent'>
          <p>Type</p>
          <label v-for="(type, idx) in types" :key='idx' >
            <input v-model="selectedType[idx]" class='checkbox' :value='type' type="checkbox">
            {{type}}
          </label>
        </div>
        <!-- 정답률 -->
        <div class='filterContent'>
          <p>Answer Rate(min)</p>
          <input v-model="selectedCr" list="tickmarks" id='answerRateBar' type="range">
          <datalist id="tickmarks">
            <option value="0" label="0%"></option>
            <option value="10" label="10%"></option>
            <option value="20" label="20%"></option>
            <option value="30" label="30%"></option>
            <option value="40" label="40%"></option>
            <option value="50" label="50%"></option>
            <option value="60" label="60%"></option>
            <option value="70" label="70%"></option>
            <option value="80" label="80%"></option>
            <option value="90" label="90%"></option>
            <option value="100" label="100%"></option>
        </datalist>
        </div>
        <!-- 리뷰 언어 -->
        <div class='filterContent'>
          <p>Reviews Language</p>
          <label v-for="(lang, idx) in pLang" :key='idx' >
            <input v-model="selectedPl[idx]" class='checkbox' :value='lang' type="checkbox">
            {{lang}}
          </label>
        </div>
        <button @click='applyFilter()' id='setFilter'>Apply</button>
      </div>
    </transition>
    <!-- 알고리즘 문제 목록 -->
    <table>
      <thead>
        <tr>
          <th>No.</th>
          <th :class='{sorted : levelSort !== 0}' class="sort-area" @click='lvChange'>Level <span class='sort-icon' id='lvString'></span></th>
          <th>Type</th>
          <th>Title</th>
          <th>Submission</th>
          <th :class='{sorted : answerRateSort !== 0}' class="sort-area" @click='arChange'>Answer rate <span class='sort-icon' id='answerRateSort'></span></th>
          <th>Reviews</th>
        </tr>
      </thead>
      <tbody>
        <ListOneLine
          v-for="(algo, idx) in algoListParsed"
          :key='idx'
          :algo = algo
          
          class='algo'
        />
      </tbody>
    </table>
    <!-- 페이지네이션 -->
    <div id='pagination'>
      <div class='pagination'>
        <span @click='changeBlock(1,blockStart)' v-show='blockStart > 5'>&laquo;</span>
        <span @click='changePage(blockStart)' :class='{active : currentPage===blockStart}'>{{blockStart}}</span>
        <span @click='changePage(blockStart+1)' v-show="blockStart+1 <= lastBlock" :class='{active : currentPage===blockStart+1}'>{{blockStart+1}}</span>
        <span @click='changePage(blockStart+2)' v-show="blockStart+2 <= lastBlock" :class='{active : currentPage===blockStart+2}'>{{blockStart+2}}</span>
        <span @click='changePage(blockStart+3)' v-show="blockStart+3 <= lastBlock" :class='{active : currentPage===blockStart+3}'>{{blockStart+3}}</span>
        <span @click='changePage(blockStart+4)' v-show="blockStart+4 <= lastBlock" :class='{active : currentPage===blockStart+4}'>{{blockStart+4}}</span>
        <span @click='changeBlock(2, blockStart)' v-show='blockStart +5<=lastBlock'>&raquo;</span>
      </div>
    </div>
  </div>
</template>

<script>
import MainNavbar from '@/components/Main/MainNavbar'
import _ from "lodash"
import ListOneLine from '@/components/Algo/ListOneLine'

export default {
    name : 'List',
    components : {
        MainNavbar,
        ListOneLine,
    },
    data : function(){
      return{
        currentPage : 1,
        types : [
          'Math',
          'Simulation',
          'String',
          'Sort',
          'Greedy',
          'Search',
          'DP'
        ],
        typesClicked : [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
        ],
        typeDetail : [
          ['사칙연산','정수론','유클리디언','정수론','조합론','기하학','수치해석','누적 합','선형대수학'],
          ['구현','시뮬레이션','부르트포스'],
          ['문자열'],
          ['정렬','분할정복'],
          ['그리디','그리디 알고리즘'],
          ['이분 탐색'],
          ['다이나믹 프로그래밍']
        ]
        ,
        filtered : false,
        detailFilter : {
          level : 0,
          answeRate: 0,
          reviewNum : 0,
        },
        algoList : [],
        algoPerPage : 17,
        pageCount : 5,
        blockStart : 1,
        lastBlock : 0,
        algoListAll : [],
        algoListParsed : [],
        levelSort : 0,
        answerRateSort :0,
        pLang : [
          'Java',
          'Python',
          'C','C++','C#',
          'JavaScript',
          'Ruby',
          'Kotlin','Swift','Go','PHP'
        ],
        selectedLv : 0,
        selectedCr : 0,
        selectedPl : new Array(11).fill(false),
        selectedType : new Array(7).fill(false),
        findInput : '',
        findType : 'Title',
        isFiltered : false,
        isSearched : false,
      }
    },
    methods: {
      btnPress : function(idx){
        // 리스트 변경
        // 1. selected
        if(this.typesClicked[idx] === false){
          this.algoList = this.algoListAll.filter(algo => {
            return this.typeDetail[idx].some(type => algo.algorithms.indexOf(type) != -1)
          })
        }else{
          this.algoList = this.algoListAll.filter(algo => {
            return this.typeDetail[idx].some(type => algo.algorithms.indexOf(type) === -1)
          })
        }
        this.lastBlock = Math.ceil(this.algoList.length / this.algoPerPage)
        this.changePage(1)
        this.typesClicked.splice(idx,1,!this.typesClicked[idx])
      },
      filter : function(){
        this.filtered = !this.filtered
      },
      levelChange : function(string){
        if(string === 1){
          if(this.selectedLv != 0){
            this.selectedLv -=1
          }
        }else{
          if(this.selectedLv != 9){
            this.selectedLv +=1
          }
        }
      },
      revieNumChange : function(string){
        if(string === 1){
          if(this.detailFilter.reviewNum != 0){
            this.detailFilter.reviewNum -=5
          }
        }else{
          if(this.detailFilter.reviewNum != 100){
            this.detailFilter.reviewNum +=5
          }
        }
      },
      applyFilter : function(){
        this.typesClicked = new Array(7).fill(false)
        let merged = []
        for(let i = 0; i < this.selectedType.length; i ++){
          if(this.selectedType[i]=== true){
            merged = merged.concat(this.typeDetail[i])
          }
        }
        let language_list = []
        for(let i = 0; i < this.selectedPl.length; i ++){
          if(this.selectedPl[i]===true){
            language_list.push(this.pLang[i])
          }
        }
        const that = this
        this.algoList = this.algoListAll.filter(function(algo){
          return algo.level === that.selectedLv
          && merged.some(type => algo.algorithms.indexOf(type) != -1)
          && algo.correct_rate >= that.selectedCr
          && language_list.some(lan => algo.language.indexOf(lan) != -1)
        })
        this.lastBlock = Math.ceil(this.algoList.length / this.algoPerPage)
        this.changePage(1)
        this.filtered = !this.filtered
        this.isFiltered = !this.isFiltered
      },
      changePage : function(newP){
        this.currentPage = newP
        this.algoListParsed = this.algoList.slice(this.algoPerPage*(newP-1),this.algoPerPage*newP)
      },
      changeBlock : function(n,newB){
        if(n ===1){
          this.blockStart = newB -5
          this.changePage(newB -1)
        }else{
          this.blockStart = newB +5
          this.changePage(newB +5)
        }
      },
      lvChange : function(){
        let lvposition = document.querySelector('#lvString')
        if(this.levelSort ===0){
          this.levelSort +=1
          lvposition.innerHTML='<i class="fas fa-sort-up"></i>'
          if(this.answerRateSort ===0){
            this.algoList= _.orderBy(this.algoList, 'level')
          }else if(this.answerRateSort == 1){
            this.algoList= _.orderBy(this.algoList, ['correct_rate','level'],['asc','asc'])
          }else{
            this.algoList= _.orderBy(this.algoList, ['correct_rate','level'],['desc','asc'])
          }
        }else if(this.levelSort === 1){
          this.levelSort +=1
          lvposition.innerHTML='<i class="fas fa-sort-down"></i>'
          if(this.answerRateSort ===0){
            this.algoList= _.orderBy(this.algoList, 'level').reverse()
          }else if(this.answerRateSort === 1){
            this.algoList= _.orderBy(this.algoList, ['correct_rate','level'],['asc','desc'])
          }else{
            this.algoList= _.orderBy(this.algoList, ['correct_rate','level'],['desc','desc'])
          }
        }else{
          this.levelSort = 0
          lvposition.innerHTML=''
          if(this.answerRateSort ===0){
            this.algoList= _.orderBy(this.algoList, 'seq')
          }else if(this.answerRateSort === 1){
            this.algoList= _.orderBy(this.algoList,'correct_rate')
          }else{
            this.algoList= _.orderBy(this.algoList, 'correct_rate').reverse()
          }
        }
        this.changePage(1)
      },
      arChange : function(){
        let arposition = document.querySelector('#answerRateSort')
        if(this.answerRateSort ===0){
          this.answerRateSort +=1
          arposition.innerHTML='<i class="fas fa-sort-up"></i>'
          if(this.levelSort ===0){
            this.algoList= _.orderBy(this.algoList, 'correct_rate')
          }else if(this.levelSort === 1){
            this.algoList= _.orderBy(this.algoList, ['level','correct_rate'],['asc','asc'])
          }else{
            this.algoList= _.orderBy(this.algoList, ['level','correct_rate'],['desc','asc'])
          }
        }else if(this.answerRateSort === 1){
          this.answerRateSort +=1
          arposition.innerHTML='<i class="fas fa-sort-down"></i>'
          if(this.levelSort ===0){
            this.algoList= _.orderBy(this.algoList, 'level').reverse()
          }else if(this.levelSort === 1){
            this.algoList= _.orderBy(this.algoList, ['level','correct_rate'],['asc','desc'])
          }else{
            this.algoList= _.orderBy(this.algoList, ['level','correct_rate'],['desc','desc'])
          }
        }else{
          this.answerRateSort = 0
          arposition.innerHTML=''
          if(this.levelSort ===0){
            this.algoList= _.orderBy(this.algoList, 'seq')
          }else if(this.levelSort === 1){
            this.algoList= _.orderBy(this.algoList,'level')
          }else{
            this.algoList= _.orderBy(this.algoList, 'level').reverse()
          }
        }
        this.changePage(1)
      },
      searchKeyword : function(){
        if(this.findInput ===''){
          alert('검색어를 입력하세요')
        }
        else{
          if(this.findType ==='Title'){
            this.algoList = this.algoListAll.filter(algo =>{
              return algo.name.indexOf(this.findInput) != -1
            })
          }else if(this.findType ==='No'){
            this.algoList = this.algoListAll.filter(algo =>{
              return algo.seq == this.findInput
            })
          }else{
            this.algoList = this.algoListAll.filter(algo =>{
              return algo.algorithms.indexOf(this.findInput) != -1
            })
          }
          this.lastBlock = Math.ceil(this.algoList.length / this.algoPerPage)
          this.isSearched = true
          this.changePage(1)
        }
      },
      rmCondition : function(){
        this.algoList = this.algoListAll
        this.lastBlock = Math.ceil(this.algoList.length / this.algoPerPage)
        this.changePage(1)
        this.isFiltered = false
        this.typesClicked = new Array(7).fill(false)
        this.isSearched = false
        this.findType = 'Title'
        this.findInput =''
        
      }
    },
    created(){
      this.$store.dispatch('getAlgo')
      .then(() => {
        this.algoListAll =  this.$store.state.algoList
        this.algoList = this.algoListAll
        this.lastBlock = Math.ceil(this.algoList.length / this.algoPerPage)
        this.changePage(1)
        })
      .catch((err) => console.log(err))
    },
    computed : {
      showBtn : function(){
        return this.isFiltered | this.typesClicked.indexOf(true) != -1 | this.isSearched
      }
    }
}
</script>

<style>
#list{
  color : var(--font-color);
}
#search{
  margin: 60px 0 10px 0 ;
  text-align: center;
  position: relative;
}
/* 검색란 */
#findtype{
  position: absolute;
  left: 31%;
  top: 50%;
  transform: translate(0,-50%);
  border: none;
  font-size: 1rem;
}

#findtype:focus{
  border: none;
}
*:focus {
    outline: none;
}
#search > form > input{
  width: 30%;
  height: 35px;
  border-radius: 20px;
  margin-right: 20px;
  padding-left: 10%;
  font-size: 1rem;
  text-overflow: hidden;
}
@media (max-width : 782px) {
  #search > form > input{
    padding-left: 11%;
    width: 25%;
  }
}
#searchIcon{
  position: absolute;
  top: 50%;
  left: calc(70% - 50px);
  transform : translate(0%,-50%)
}
#search > form > input:focus{
  outline: none;
}
.searchBtn{
  background-color: white;
  border: none;
}
.searchBtn:hover{
  cursor: pointer;
  color: red;
}
.searchBtn:focus{
  border: none;
  outline: none;
}
#filterIcon{
  position: absolute;
  top: 50%;
  left: calc(70% + 3px);
  transform : translate(0%,-50%);
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
  padding: 6px 10px;
  border-radius: 20px;
}
#rmCondition{
  position: absolute;
  top: 50%;
  left: calc(70% + 50px);
  transform : translate(0%,-50%);
  text-align: center;
  border-radius: 20px;
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
  padding: 5px 10px;
}
#rmCondition > span{
  font-size: 1.1rem;
  font-weight: bold;
}
/* 타입별 필터 */
#filterByType{
  text-align: center;
  margin-bottom: 30px;
}
.typeIcon{
  height: 35px;
  padding: 0 12px;
  margin: 0 8px;
  background-color: white;
  border: 1px solid rgba(0, 0, 0, 0.301);
  color: black;
  border-radius: 15px;
  /* box-shadow: 0 2px 6px 0 var(--shadow-color); */
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 10%);
}
.typeIcon:focus{
  outline: none;
}
.typeIcon:hover{
  color: rgb(68, 34, 34);
  background-color:  rgba(210, 212, 216, 0.514);
  cursor: pointer;
}
.btnPressed{
  height: 35px;
  padding: 0 12px;
  margin: 0 8px;  
  border-radius: 15px;  
  color: black;
  background-color:  rgba(180, 180, 180, 0.514);
}
/* 세부 필터 */
#filterClose{
    margin: 0;
    color: rgba(37, 40, 47, 0.65);
    border-radius: 22px;
    float: right;
    margin-right: 10px;
    margin-top: 25px;
    position: absolute;
    top: 0;
    right: 5px;
}
#filterClose > span{
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    padding: 4px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
}
#filterClose:hover{
    cursor: pointer;
}
#filterClose:hover > span{
    background-color: rgba(202, 202, 202, 0.822);
    color: rgba(37, 40, 47, 0.411);
}

/* 세부필터 슬라이드 */
.slide-enter-active {
  -moz-transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  -o-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -moz-transition-timing-function: ease-in;
  -webkit-transition-timing-function: ease-in;
  -o-transition-timing-function: ease-in;
  transition-timing-function: ease-in;
}

.slide-leave-active {
  -moz-transition-duration: 0.3s;
  -webkit-transition-duration: 0.3s;
  -o-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -moz-transition-timing-function: ease-out;
  -webkit-transition-timing-function: ease-out;
  -o-transition-timing-function: ease-out;
  transition-timing-function: ease-out;
}

.slide-enter-to, .slide-leave {
  max-height: 480px;
  overflow: hidden;
}

.slide-enter, .slide-leave-to {
  overflow: hidden;
  max-height: 0;
}
#filterSection{
  text-align: center;
  width: 40%;
  margin: 0px auto 40px auto;
  border-radius: 10px;
  box-shadow: 0 2px 6px 0 rgb(0 0 0 / 40%);
  padding: 2% 4%;
  position: relative;
}
#filterSection > p:nth-child(1){
  text-align: center;
  font-size : 1.8rem;
  box-shadow : 0 1px 0 0 rgb(37 40 47 / 10%) ;
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.filterContent{
  margin: 20px 0;
}
.filterContent > p {
  text-align: left;
  font-size: 1.3rem;
  margin-top: 10px;
  margin-bottom: 10px;
}
.filterContent > label{
  cursor: pointer;
}
.manulBtn{
  width: 30px;
  height: 30px;
  background: white;
  border: 1px solid rgb(113, 113, 113);
  border-radius: 50%;
  text-align: center;
  margin: 0 10px;
}
.manulBtnUnable{
  border: 1px solid rgba(176, 176, 176, 0.856);
}
.manulBtnUnable > span{
  color : rgb(176, 176, 176) !important;
}
.manulBtnUnable:hover{
  border: 1px solid rgb(176, 176, 176, 0.856) !important;
}
.manulBtn + span{
  font-size: 1.5rem;
}
.manulBtn:focus{
  outline: none;
}
.manulBtn:hover{
  margin-bottom: auto;
  border: 1px solid black;
  cursor: pointer;
}
.manulBtn:hover > span{
  color: black;
}
.manulBtn>span{
  font-size: 20px;
  margin: auto 0;
  width: 24px;
  height: 24px;
  color: rgba(113, 113, 113);
}
.checkbox{
  width: 15px;
  height: 15px;
}
.checkbox:hover{
  cursor: pointer;
}
.level label {
    display: block;
    text-align: center;
}
#answerRateBar{
  width: 100%;
}
datalist {
    width: 106%;
    text-align: left;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
}
datalist option {
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
        -ms-flex-positive: 11;
            flex-grow: 1;
    -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
            flex-basis: 0;
}
input[type=range]::-webkit-slider-runnable-track{
  width: 100%;
  height: 8.8px;
  cursor: pointer;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: #ffffff;
  border-radius: 1.3px;
  border: 0.2px solid #010101;
  }
input[type=range]:focus::-webkit-slider-runnable-track {
  background: #ffffff;
}
#setFilter{
  border : 1px solid rgb(134, 134, 134);
  background-color: white;
  font-size: 1rem;
  width: 20%;
  margin-top: 10px;
}
#setFilter:hover{
  background-color: rgb(223, 223, 223);
  color: black;
  cursor: pointer;
}

/* 문제 목록 */
table{
  margin : 0 10%;
  width: 80%;
  /* border: 1px solid rgba(0, 0, 0, 0.486); */
  border-collapse: collapse;
  box-shadow: 0px 0.5px 2px 0.5px rgb(0 0 0 / 100%);
}
table > thead > tr{
  height: 30px;
  font-size: 1.2rem;
}
.sorted{
  background-color: rgba(103, 169, 255, 0.253);
}
tbody > tr:nth-child(even){
  background-color: rgba(91, 143, 255, 0.048);
}
table > tbody > tr > th > span{
  font-size: 0.8rem;
}
table > thead > tr{
  border-bottom: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(1){
  width: 6%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(2){
  width: 6%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(3){
  width: 10%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(4){
  width: 50%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(5){
  width: 10%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(6){
  width: 10%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(7){
  width: 8%;
}
.algo{
  height: 35px;
  box-shadow : 0 1px 0 0 rgb(37 40 47 / 30%) ;
}
table > tbody > tr:nth-child(17){
  box-shadow: none;
}
.algo:hover{
  background-color: rgba(224, 221, 221, 0.247);
  cursor: pointer;
}
/* 페이지네이션 */
#pagination{
  text-align: center;
  margin-bottom: 30px;
  margin-top: 30px;
}
.pagination{
  display: inline-block;
}
.pagination span {
  color: black;
  float: left;
  padding: 8px 16px;
  text-decoration: none;
  transition: background-color .3s;
  border: 1px solid #ddd;
}

.pagination span.active {
  background-color: #051066;
  color: white;
  border: 1px solid #051066;
}
.pagination span:hover:not(.active){
  background-color: #ddd;
}
.btnClicked{
  color: red;
}
.sort-area{
  position: relative;
}
.sort-area:hover{
  cursor: pointer;
  background-color: rgba(103, 169, 255, 0.253);
}
.sort-icon{
  position: absolute;
  top: 50%;
  right: 1px;
  transform: translate(-50%, -50%);
  margin:auto 0;
  font-size : 1rem
}
</style>