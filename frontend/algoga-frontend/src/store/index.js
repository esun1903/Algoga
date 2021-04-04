import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import createPersistedState from 'vuex-persistedstate';
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        algoList: [],
    },
    mutations: {
        getAlgo: function(state, data) {
            this.state.algoList = data;
        },
    },
    actions: {
        getAlgo: function(context) {
            if (this.state.algoList.length === 0) {
                axios
                    .get(`${SERVER_URL}/apps/v1/allProblem`)
                    .then((res) => {
                        context.commit('getAlgo', res.data);
                    })
                    .catch((err) => {
                        console.log(err);
                    });
            } else {
                context.commit('getAlgo', this.state.algoList);
            }
        },
    },
    getters: {},
    plugins: [createPersistedState()],
});
