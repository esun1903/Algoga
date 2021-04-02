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
          <th :class='{sorted : levelSort !== 0}' class="sort-area" @click='lvChange'>Level <span class='sort-icon' id='lvString'></span></th>
          <th>Type</th>
          <th>Title</th>
          <th :class='{sorted : answerRateSort !== 0}' class="sort-area" @click='arChange'>Answer rate <span class='sort-icon' id='answerRateSort'></span></th>
          <th>Reviews</th>
        </tr>
      </thead>
      <tbody>
        <ListOneLine
          v-for="(algo, idx) in algoListParsed2"
          :key='idx'
          :algo = algo
          
          class='algo'
        />
        <!-- <tr  > -->
          <!-- <th><span>no.</span>{{algo.seq}}</th>
          <th><span>lv.</span>{{algo.level}}</th>
          <th>type</th>
          <th>{{algo.name}}</th>
          <th>{{algo.correct_rate | round}}%</th>
          <th>{{algo.correct_user}}</th> -->
        <!-- </tr> -->
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
// import axios from 'axios'
import _ from "lodash"
import ListOneLine from '@/components/Algo/ListOneLine'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name : 'List',
    components : {
        MainNavbar,
        ListOneLine,
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
        algoPerPage : 17,
        pageCount : 5,
        blockStart : 1,
        lastBlock : 0,
        algoListParsed : [],
        algoListParsed2 : [
      {'seq': 9250, 'number': 3018, 'name': '캠프파이어', 'correct_user': 164, 'submission_cnt': 480, 'correct_rate': 42, 'level': 6, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '128 MB', 'algorithms': '비트 집합', 'algorithm_ids': '152', 'review_count': 0},{'seq': 9251, 'number': 20501, 'name': 'Facebook', 'correct_user': 73, 'submission_cnt': 286, 'correct_rate': 40, 'level': 14, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '1024 MB', 'algorithms': '비트 집합', 'algorithm_ids': '152', 'review_count': 0},
      {'seq': 9252, 'number': 11588, 'name': 'GEPPETTO', 'correct_user': 46, 'submission_cnt': 60, 'correct_rate': 83, 'level': 9, 'avg_try': 1, 'time_limit': '1 초', 'memory_limit': '64 MB', 'algorithms': '비트 집합', 'algorithm_ids': '152', 'review_count': 0},
      {'seq': 9253, 'number': 17464, 'name': '알파벳 문자열', 'correct_user': 17, 'submission_cnt': 78, 'correct_rate': 27, 'level': 19, 'avg_try': 3, 'time_limit': '1 초', 'memory_limit': '256 MB', 'algorithms': '비트 집합', 'algorithm_ids': '152', 'review_count': 0},
      {'seq': 9254, 'number': 14851, 'name': '해밍 거리와 쿼리', 'correct_user': 7, 'submission_cnt': 66, 'correct_rate': 26, 'level': 18, 'avg_try': 3, 'time_limit': '6 초', 'memory_limit': '512 MB', 'algorithms': '비트 집합', 'algorithm_ids': '152', 'review_count': 0},{'seq': 9255, 'number': 19102, 'name': 'Array Challenge', 'correct_user': 3, 'submission_cnt': 7, 'correct_rate': 75, 'level': 21, 'avg_try': 1, 'time_limit': '1 초', 'memory_limit': '512 MB', 'algorithms': '벌래캠프–매시', 'algorithm_ids': '110', 'review_count': 0},
      {'seq': 9256, 'number': 18017, 'name': '총알의 속도', 'correct_user': 204, 'submission_cnt': 1404, 'correct_rate': 22, 'level': 0, 'avg_try': 4, 'time_limit': '0.5 초', 'memory_limit': '256 MB', 'algorithms': '물리학', 'algorithm_ids': '116', 'review_count': 0},
      {'seq': 9257, 'number': 16293, 'name': 'Appalling Architecture', 'correct_user': 27, 'submission_cnt': 58, 'correct_rate': 47, 'level': 6, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '512 MB', 'algorithms': '물리학', 'algorithm_ids': '116', 'review_count': 0},
      {'seq': 9258, 'number': 6545, 'name': 'Drink, on Ice', 'correct_user': 16, 'submission_cnt': 37, 'correct_rate': 50, 'level': 4, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '128 MB', 'algorithms': '물리학', 'algorithm_ids': '116', 'review_count': 0},
      {'seq': 9259, 'number': 12084, 'name': 'Captain Hammer (Small)', 'correct_user': 10, 'submission_cnt': 39, 'correct_rate': 50, 'level': 6, 'avg_try': 2, 'time_limit': '5 초', 'memory_limit': '512 MB', 'algorithms': '물리학', 'algorithm_ids': '116', 'review_count': 0},
      {'seq': 9260, 'number': 12288, 'name': 'Captain Hammer (Small)', 'correct_user': 10, 'submission_cnt': 42, 'correct_rate': 41, 'level': 6, 'avg_try': 2, 'time_limit': '5 초', 'memory_limit': '512 MB', 'algorithms': '물리학', 'algorithm_ids': '116', 'review_count': 0},
      {'seq': 9261, 'number': 12346, 'name': 'Captain Hammer (Small)', 'correct_user': 9, 'submission_cnt': 32, 'correct_rate': 50, 'level': 6, 'avg_try': 2, 'time_limit': '5 초', 'memory_limit': '512 MB', 'algorithms': '물리학', 'algorithm_ids': '116', 'review_count': 0},
      {'seq': 9262, 'number': 19470, 'name': 'Physics', 'correct_user': 4, 'submission_cnt': 4, 'correct_rate': 100, 'level': 14, 'avg_try': 1, 'time_limit': '1 초', 'memory_limit': '512 MB', 'algorithms': '물리학', 'algorithm_ids': '116', 'review_count': 0},
      {'seq': 9263, 'number': 10880, 'name': '내가 어디를 거쳐갔더라?', 'correct_user': 23, 'submission_cnt': 138, 'correct_rate': 20, 'level': 22, 'avg_try': 5, 'time_limit': '2 초', 'memory_limit': '256 MB', 'algorithms': '이중 연결 요소', 'algorithm_ids': '153', 'review_count': 0},
      {'seq': 9264, 'number': 4385, 'name': 'Interpreter', 'correct_user': 13, 'submission_cnt': 53, 'correct_rate': 44, 'level': 12, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '128 MB', 'algorithms': '인터프리터', 'algorithm_ids': '156', 'review_count': 0},
      {'seq': 9265, 'number': 12773, 'name': 'Road Times', 'correct_user': 9, 'submission_cnt': 35, 'correct_rate': 34, 'level': 25, 'avg_try': 2, 'time_limit': '5 초', 'memory_limit': '512 MB', 'algorithms': '선형 계획법', 'algorithm_ids': '103', 'review_count': 0},
      {'seq': 9266, 'number': 19043, 'name': 'Balance', 'correct_user': 7, 'submission_cnt': 9, 'correct_rate': 77, 'level': 22, 'avg_try': 1, 'time_limit': '1 초', 'memory_limit': '512 MB', 'algorithms': '선형 계획법,헝가리안', 'algorithm_ids': '103,36', 'review_count': 0},
      {'seq': 9267, 'number': 17854, 'name': 'Cheese, If You Please', 'correct_user': 5, 'submission_cnt': 17, 'correct_rate': 83, 'level': 24, 'avg_try': 1, 'time_limit': '2 초 (추가 시간 없음)', 'memory_limit': '512 MB', 'algorithms': '선형 계획법', 'algorithm_ids': '103', 'review_count': 0},
      {'seq': 9268, 'number': 9208, 'name': '링월드', 'correct_user': 17, 'submission_cnt': 64, 'correct_rate': 35, 'level': 23, 'avg_try': 2, 'time_limit': '2 초', 'memory_limit': '128 MB', 'algorithms': '홀의 결혼 정리', 'algorithm_ids': '34', 'review_count': 0},
      {'seq': 9269, 'number': 14216, 'name': '할 일 정하기 2', 'correct_user': 63, 'submission_cnt': 576, 'correct_rate': 26, 'level': 21, 'avg_try': 3, 'time_limit': '0.5 초', 'memory_limit': '512 MB', 'algorithms': '헝가리안', 'algorithm_ids': '36', 'review_count': 0},
      {'seq': 9270, 'number': 16812, 'name': 'Laser Cutter', 'correct_user': 5, 'submission_cnt': 7, 'correct_rate': 71, 'level': 21, 'avg_try': 1, 'time_limit': '5 초', 'memory_limit': '512 MB', 'algorithms': '헝가리안', 'algorithm_ids': '36', 'review_count': 0},
      {'seq': 9271, 'number': 17575, 'name': 'Kings', 'correct_user': 5, 'submission_cnt': 14, 'correct_rate': 35, 'level': 21, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '512 MB', 'algorithms': '헝가리안', 'algorithm_ids': '36', 'review_count': 0},
      {'seq': 9272, 'number': 15737, 'name': '일반 그래프 매칭', 'correct_user': 24, 'submission_cnt': 86, 'correct_rate': 47, 'level': 24, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '128 MB', 'algorithms': '일반적인 매칭', 'algorithm_ids': '15', 'review_count': 0},
      {'seq': 9273, 'number': 15741, 'name': '일반 그래프 최대 가중치 매칭', 'correct_user': 13, 'submission_cnt': 27, 'correct_rate': 81, 'level': 28, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512 MB', 'algorithms': '일반적인 매칭', 'algorithm_ids': '15', 'review_count': 0},
      {'seq': 9274, 'number': 16046, 'name': 'Rainbow Graph', 'correct_user': 9, 'submission_cnt': 19, 'correct_rate': 56, 'level': 27, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
      {'seq': 9275, 'number': 3836, 'name': 'Coin Collecting', 'correct_user': 8, 'submission_cnt': 43, 'correct_rate': 20, 'level': 27, 'avg_try': 4, 'time_limit': '2 초', 'memory_limit': '128 MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
      {'seq': 9276, 'number': 18517, 'name': 'Pick Your Own Nim', 'correct_user': 6, 'submission_cnt': 8, 'correct_rate': 75, 'level': 26, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512 MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
      {'seq': 9277, 'number': 18588, 'name': 'Milk Candy', 'correct_user': 5, 'submission_cnt': 5, 'correct_rate': 100, 'level': 26, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512 MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
      {'seq': 9266, 'number': 19043, 'name': 'Balance', 'correct_user': 7, 'submission_cnt': 9, 'correct_rate': 77, 'level': 22, 'avg_try': 1, 'time_limit': '1 초', 'memory_limit': '512 MB', 'algorithms': '선형 계획법,헝가리안', 'algorithm_ids': '103,36', 'review_count': 0},
      {'seq': 9267, 'number': 17854, 'name': 'Cheese, If You Please', 'correct_user': 5, 'submission_cnt': 17, 'correct_rate': 83, 'level': 24, 'avg_try': 1, 'time_limit': '2 초 (추가 시간 없음)', 'memory_limit': '512 MB', 'algorithms': '선형 계획법', 'algorithm_ids': '103', 'review_count': 0},
      {'seq': 9268, 'number': 9208, 'name': '링월드', 'correct_user': 17, 'submission_cnt': 64, 'correct_rate': 35, 'level': 23, 'avg_try': 2, 'time_limit': '2 초', 'memory_limit': '128 MB', 'algorithms': '홀의 결혼 정리', 'algorithm_ids': '34', 'review_count': 0},
      {'seq': 9269, 'number': 14216, 'name': '할 일 정하기 2', 'correct_user': 63, 'submission_cnt': 576, 'correct_rate': 26, 'level': 21, 'avg_try': 3, 'time_limit': '0.5 초', 'memory_limit': '512 MB', 'algorithms': '헝가리안', 'algorithm_ids': '36', 'review_count': 0},
      {'seq': 9270, 'number': 16812, 'name': 'Laser Cutter', 'correct_user': 5, 'submission_cnt': 7, 'correct_rate': 71, 'level': 21, 'avg_try': 1, 'time_limit': '5 초', 'memory_limit': '512 MB', 'algorithms': '헝가리안', 'algorithm_ids': '36', 'review_count': 0},
      {'seq': 9271, 'number': 17575, 'name': 'Kings', 'correct_user': 5, 'submission_cnt': 14, 'correct_rate': 35, 'level': 21, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '512 MB', 'algorithms': '헝가리안', 'algorithm_ids': '36', 'review_count': 0},
      {'seq': 9272, 'number': 15737, 'name': '일반 그래프 매칭', 'correct_user': 24, 'submission_cnt': 86, 'correct_rate': 47, 'level': 24, 'avg_try': 2, 'time_limit': '1 초', 'memory_limit': '128 MB', 'algorithms': '일반적인 매칭', 'algorithm_ids': '15', 'review_count': 0},
      {'seq': 9273, 'number': 15741, 'name': '일반 그래프 최대 가중치 매칭', 'correct_user': 13, 'submission_cnt': 27, 'correct_rate': 81, 'level': 28, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512 MB', 'algorithms': '일반적인 매칭', 'algorithm_ids': '15', 'review_count': 0},
      {'seq': 9274, 'number': 16046, 'name': 'Rainbow Graph', 'correct_user': 9, 'submission_cnt': 19, 'correct_rate': 56, 'level': 27, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
      {'seq': 9275, 'number': 3836, 'name': 'Coin Collecting', 'correct_user': 8, 'submission_cnt': 43, 'correct_rate': 20, 'level': 27, 'avg_try': 4, 'time_limit': '2 초', 'memory_limit': '128 MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
      {'seq': 9276, 'number': 18517, 'name': 'Pick Your Own Nim', 'correct_user': 6, 'submission_cnt': 8, 'correct_rate': 75, 'level': 26, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512 MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
      {'seq': 9277, 'number': 18588, 'name': 'Milk Candy', 'correct_user': 5, 'submission_cnt': 5, 'correct_rate': 100, 'level': 26, 'avg_try': 1, 'time_limit': '2 초', 'memory_limit': '512 MB', 'algorithms': '매트로이드', 'algorithm_ids': '104', 'review_count': 0},
        ],
        levelSort : 0,
        answerRateSort :0,
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
    },
    // created(){
    //   axios.get(`http://127.0.0.1:8000/apps/v1/allProblem`)
    //     .then(res =>{
    //       this.algoList = res.data
    //       this.lastBlock = Math.ceil(this.algoList.length / this.algoPerPage)
    //       this.changePage(1)
    //     })  
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },



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
  width: 8%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(4){
  width: 58%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(5){
  width: 12%;
  border-right: 1px solid rgba(0, 0, 0, 0.486);
}
table > thead > tr > th:nth-child(6){
  width: 10%;
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