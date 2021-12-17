import Vue from 'vue'
import Router from 'vue-router'
import Vuex from "vuex"

//注册
Vue.use(Router)
Vue.use(Vuex)


//实例化
export default new Router({
    routes: [
        {
            path: '/',
            name: 'Home',
            component: (resolve) => require(["../components/Pages/Home"],resolve),
            meta:{
                keepAlive: true
        }
        },
        {
            path:'/problemlist',
            name:'ProblemList',
            component:(resolve) => require(["../components/Pages/ProblemList"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/problemlist/:id',
            name:'ProblemDetail',
            component:(resolve) => require(["../components/Pages/ProblemDetail"], resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/login',
            name:'Login',
            component:(resolve) => require(["../components/Pages/Login"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/register',
            name:'Register',
            component:(resolve) => require(["../components/Pages/Resister"],resolve),
            meta:{
                keepAlive: true
            }
        }
    ]
})