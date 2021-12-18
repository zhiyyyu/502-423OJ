import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    /**
     * 用vuex实现存储用户的token
     */
    state: {
        userData: {
            //测试一下
            access: "",      //sessionStorage.getItem('token')
            refresh:"",
            user_type:"",
            id:0
        },
        userform:{
            username:"",
            password:""
        },
    },
    /**
     * 将token存储到本地中*
     */
    mutations: {
        //将token保存到sessionStorage里，token表示登陆状态
        SET_TOKEN: (state, data) => {
            state.userData.access = data;
            sessionStorage.setItem('access', data);
            sessionStorage.setItem('refresh', data)
        },
        //获取用户名
        SET_USER: (state, data) => {
            // 把用户名存起来
            state.userform.username = data
            sessionStorage.setItem('username', data)
        },
        //登出
        LOGOUT: (state) => {
            // 登出的时候要清除token
            state.userData.access = null
            state.userData.username = null
            sessionStorage.removeItem('access')
            sessionStorage.removeItem('refresh')
        }
    }
})
