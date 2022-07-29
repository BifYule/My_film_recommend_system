import Vue from 'vue'
import VueRouter from 'vue-router'

import Homepage from '@/views/Homepage' //主页
import Login from "@/views/Login" //登陆
import Register from "@/views/Register"; //注册
import Home from '@/views/Home'
import Detailpage from '../views/Detailpage'
import Film_analysis from '../views/Film_analysis'
import Classification from '../views/Classification'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'login',
        component: Login
    },
    {
        path: '/Register',
        name: 'Register',
        component: Register
    }, {
        path: '/Homepage',
        name: 'Homepage',
        component: Homepage
    }, {
        path: '/Home',
        name: 'Home',
        component: Home
    },{
        path:'/Detailpage',
        name:'Detailpage',
        component: Detailpage
    },
    {
        path:'/Film_analysis',
        name:'Film_analysis',
        component: Film_analysis
    },
    {
        path:'/Classification',
        name:'Classification',
        component: Classification
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
