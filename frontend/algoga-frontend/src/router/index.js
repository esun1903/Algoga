import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home';
import Main from '@/views/Main';
import Register from '@/views/Register';
import List from '@/views/List';
import Problem from '@/views/Problem';
import CodeBoardDetail from '@/views/CodeBoardDetail';
import Mycode from '@/views/Mycode';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/main/:nickname',
        name: 'Main',
        component: Main,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
    },
    {
        path: '/list',
        name: 'List',
        component: List,
    },
    {
        path: '/mycode',
        name: 'Mycode',
        component: Mycode,
    },
    {
        path: '/codeBoardDetail/:codeBoard_seq',
        name: 'CodeBoardDetail',
        component: CodeBoardDetail,
    },
    {
        path: '/problem/:no',
        name: 'Problem',
        component: Problem,
        props: (route) => ({
            no: route.seq,
            ...route.params,
        }),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
