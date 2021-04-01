import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home';
import Main from '@/views/Main';
import Register from '@/views/Register';
import List from '@/views/List';

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
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
