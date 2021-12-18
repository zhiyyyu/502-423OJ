import Vue from 'vue'
import Router from 'vue-router'
import Vuex from "vuex"
import store from "@/store";
//import axios from "axios";

//注册
Vue.use(Router)
Vue.use(Vuex)

//实例化
const router = new Router({
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
                keepAlive: true,

            }
        },
        {
            path:'/problemlist/:id',
            name:"problemdetails",
            component:(resolve) => require(["../components/Pages/problemdetails"],resolve),
            meta:{
                keepAlive: true,
                requireAuth: true
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
        },
        {
            path:'/rank',
            name:'rank',
            component:(resolve)=>require(["../components/Pages/rank"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/userhome',
            name:'userhome',
            component:(resolve)=>require(["../components/User/userHome"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/usersubmission',
            name:'usersubmission',
            component:(resolve)=>require(["../components/User/userSubmisson"],resolve),
            meta:{
                keepAlive: true
            }
        },
        {
            path:'/usersetting',
            name:'usersetting',
            component:(resolve)=>require(["../components/User/userSetting"],resolve),
            meta:{
                keepAlive: true
            }
        },
    ]
})

// /**
//  * 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
//  */
router.beforeEach((to, from, next) => {
    if (to.meta['requireAuth']) {
        console.log(to.fullPath);
        console.log("该页面需要用户登录后才能操作，需要权限");
        if (store.state.userData.access) {   //如果存在token则直接跳转
            console.log("用户已登录可以进行下一步");
            next()
        } else {
            console.log("用户未登录，取消当前导航");
            alert("你需要登录后才能进行操作");
            next(false)
        }
    } else {
        console.log("该页面没用权限管理");
        next()
    }
})
// /**
//  * 添加请求拦截器，在请求头中加token
//  */
// axios.interceptors.request.use(
//     config => {
//         console.log("请求拦截器config");
//         if(sessionStorage.getItem('access')){
//             config.headers.token=sessionStorage.getItem('access');
//         }else{
//             //否则用永久token请求新的临时token
//             config.headers.token=sessionStorage.getItem('refresh');
//         }
//         return config;
//     },
//     error => {
//         console.log("请求拦截器error");
//         return Promise.reject(error);
//     }
// );

export default router;

