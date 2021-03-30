<template>
  <div id='list'>
    <MainNavbar />
    <!-- 검색 -->
    <div id='search'>
      <form>
        <input id='keyword' type="text" maxlength="30">
      </form>
      <button id='searchIcon'  class='searchBtn'><i class="fas fa-search"></i></button>
      <button @click='filter' :class='{btnClicked : filtered}' id='filterIcon' class='searchBtn'><i class="fas fa-sort-amount-down"></i></button>
    </div>
    <!-- 타입 버튼 필터링 -->
    <div id='filterByType'>
      <button
        @click='btnPress(type)'
        class='typeIcon'
        v-for="(idx, type) in types" :key="idx"
        :class="{btnPressed :types[type]}">
        {{type}}
      </button>
    </div>
    <!-- 세부 필터링 -->
    <transition name='slide'>
      <div v-show="filtered" id='filterSection'>
        <p>Filter</p>
        <!-- 레벨 -->
        <div class='filterContent'>
          <p>Level</p>
          <div>
            <button class='manulBtn' :class='{manulBtnUnable : detailFilter.level == 0 }' @click='levelChange(1)'><span>-</span></button>
            <span>{{detailFilter.level}}</span>
            <button :class='{manulBtnUnable : detailFilter.level == 9 }' class='manulBtn' @click='levelChange(2)'><span>+</span></button>
          </div>
        </div>
        <!-- 타입 -->
        <div class='filterContent'>
          <p>Type</p>
          <label v-for="(idx,type) in types" :key='idx' >
            <input class='checkbox' :value='type' type="checkbox">
            {{type}}
          </label>
        </div>
        <!-- 정답률 -->
        <div class='filterContent'>
          <p>Answer Rate(min)</p>
          <input list="tickmarks" id='answerRateBar' type="range">
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
        <!-- 리뷰 수 -->
        <div class='filterContent'>
          <p>Reviews Number(min)</p>
            <button class='manulBtn' :class='{manulBtnUnable : detailFilter.reviewNum == 0 }' @click='revieNumChange(1)'><span>-</span></button>
            <span>{{detailFilter.reviewNum}}</span>
            <button :class='{manulBtnUnable : detailFilter.reviewNum == 9 }' class='manulBtn' @click='revieNumChange(2)'><span>+</span></button>
        </div>
        <button @click='applyFilter' id='setFilter'>Apply</button>
      </div>
    </transition>
    <!-- 알고리즘 문제 목록 -->
    <table>
      <thead>
        <tr>
          <th>No.</th>
          <th>Lv</th>
          <th>Type</th>
          <th>Title</th>
          <th>Answer rate</th>
          <th>Reviews</th>
        </tr>
      </thead>
      <tbody>
        <tr class='algo' v-for="(algo, idx) in algoListParsed" :key='idx'>
          <th>{{algo.no}}</th>
          <th>{{algo.level}}</th>
          <th>{{algo.type}}</th>
          <th>{{algo.title}}</th>
          <th>{{algo.answerrate}}%</th>
          <th>{{algo.reviews}}</th>
        </tr>
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

export default {
    name : 'List',
    components : {
        MainNavbar,
    },
    data : function(){
      return{
        currentPage : 1,
        types : {
          'Math' : false,
          'Simulation' : false,
          'DfS' : false,
          'Bfs' : false,
          'Tree' : false,
          'Search' : false,
          'DP' : false
        },
        filtered : false,
        detailFilter : {
          level : 0,
          answeRate: 0,
          reviewNum : 0,
        },
        algoList : [],
        algoPerPage : 20,
        pageCount : 5,
        blockStart : 1,
        lastBlock : 0,
        algoListParsed : [],
      }
    },
    methods: {
      btnPress : function(idx){
        this.types[idx] = !this.types[idx]
      },
      filter : function(){
        this.filtered = !this.filtered
      },
      levelChange : function(string){
        if(string === 1){
          if(this.detailFilter.level != 0){
            this.detailFilter.level -=1
          }
        }else{
          if(this.detailFilter.level != 9){
            this.detailFilter.level +=1
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
        this.filtered = !this.filtered
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
      }
    },
    created(){

      const range = (start, stop, step) => Array.from({ length: (stop - start) / step + 1}, (_, i) => start + (i * step));
      let sample = range(0,100,1)

      sample.forEach(s => {
        var a = {
              'no' : s,
              'level' : 2,
              'type' : '트리',
              'title' : '동희야 점심 뭐 먹어'+String(s),
              'answerrate' : 100,
              'reviews' : 23
            }

        this.algoList.push(a)
        
      })
      this.lastBlock = Math.ceil(this.algoList.length / this.algoPerPage)
      this.changePage(1)
    },


}
</script>

<style>
#search{
  margin: 60px 0 10px 0 ;
  text-align: center;
  position: relative;
}
/* 검색란 */
#search > form > input{
  width: 40%;
  height: 35px;
  border-radius: 20px;
  margin-right: 20px;
  padding-left: 20px;
  font-size: 1rem;
  text-overflow: hidden;
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
}
/* 타입별 필터 */
#filterByType{
  text-align: center;
  margin-bottom: 40px;
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
  border: 1px solid rgba(0, 0, 0, 0.486);
  border-radius: 4px;
  border-collapse: collapse;
  box-shadow: 0 2px 2px 0 rgb(0 0 0 / 10%);
}
table > thead > tr{
  border-bottom: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(1){
  width: 4%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(2){
  width: 4%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(3){
  width: 8%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(4){
  width: 64%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(5){
  width: 12%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(6){
  width: 10%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
.algo{
  height: 30px;
  box-shadow : 0 1px 0 0 rgb(37 40 47 / 40%) ;
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
  background-color: #555755e7;
  color: white;
  border: 1px solid #555755;
}
.pagination span:hover:not(.active){
  background-color: #ddd;
}
.btnClicked{
  color: red;
}
</style>