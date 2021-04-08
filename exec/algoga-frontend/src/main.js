import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import Codemirror from 'vue-codemirror';
import 'codemirror/lib/codemirror.css';
import AOS from 'aos';
import 'aos/dist/aos.css';

import VueCodeHighlight from "vue-code-highlight"

Vue.config.productionTip = false;

Vue.use(Codemirror);
Vue.use(VueCodeHighlight)

new Vue({
    created() {
        AOS.init();
    },
    store,
    router,
    render: (h) => h(App),
}).$mount('#app');
