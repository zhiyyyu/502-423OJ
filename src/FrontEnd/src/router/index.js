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
            name: 'home',
            component: (resolve) => require(["../components/Pages/home"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/problemlist',
            name:'problemlist',
            component:(resolve) => require(["../components/Pages/problemlist"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/problemlist/:id',
            name:"problemdetails",
            component:(resolve) => require(["../components/Pages/problemdetails"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/about',
            name:'about',
            component:(resolve) => require(["../components/Pages/about"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/status',
            name:'status',
            component:(resolve)=>require(["../components/Pages/status"],resolve),
            meta:{
                keepAlive: true
            }
        }

        // {
        //     path:'/login',
        //     name:'logindialog.vue',
        //     component:(resolve) => require(["../components/Pages/login"],resolve),
        //     meta:{
        //         keepAlive: true
        //     }
        // },
        // {
        //     path:'/resister',
        //     name:'resister',
        //     component:(resolve) => require(["../components/Pages/resister"],resolve),
        //     meta:{
        //         keepAlive: true
        //     }
        // }
    ]
})