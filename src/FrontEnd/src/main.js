/**
 * 作用: 把后续你要写的 Vue 组件挂载到public目录下的 index.html 中
 * 前端的初始化配置，都可以写到这里
 */
import Vue from 'vue'
import App from './App.vue'
import router from  './router'
import store from './store'
//引入数据传递方式
import axios from 'axios'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 全局引入vue-codemirror
import VueCodeMirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'
import { codemirror } from 'vue-codemirror';
// 引入主题 可以从 codemirror/theme/ 下引入多个
import 'codemirror/theme/idea.css'
// 引入语言模式 可以从 codemirror/mode/ 下引入多个
import 'codemirror/mode/sql/sql.js';

//引入加密模式
import md5 from 'js-md5';
//引入ViewUI
import ViewUI from "view-design"
import 'view-design/dist/styles/iview.css'
//引入可复制模块
import VueClipboard from 'vue-clipboard2'
//引入组件滑动模式
import 'default-passive-events'
//引入粒子背景插件
import VueParticles from 'vue-particles'


Vue.use(VueCodeMirror)

//使用引入的模块
Vue.use(VueClipboard)
Vue.config.productionTip = false

Vue.use(ViewUI);
Vue.prototype.$md5 = md5

Vue.use(codemirror)
Vue.use(ElementUI);

//全局注册，使用方法为:this.$axios
Vue.prototype.$axios = axios;
axios.defaults.baseURL = "http://localhost:8000/";
Vue.use(VueParticles)

// eslint-disable-next-line no-unused-vars
let isRefreshing = false;
// 存储请求的数组
let refreshSubscribers = [];

/*将所有的请求都push到数组中*/
function subscribeTokenRefresh(cb) {
    refreshSubscribers.push(cb);
}

// 数组中的请求得到新的token之后执行，用新的token去请求数据
// eslint-disable-next-line no-unused-vars
function onRrefreshed(token) {
    refreshSubscribers.map(cb => cb(token));
}

// eslint-disable-next-line no-unused-vars
function isExpired() {
    let time = sessionStorage.getItem("TokenTime");
    let nowTime = new Date().getTime();
    let stamp = nowTime - time;
    let minutes = parseInt((stamp % (1000 * 60 * 60)) / (1000 * 60));
    return minutes >= 4 ? true : false;
}


axios.interceptors.request.use(
    config => {
        // 判断是否存在token，如果存在的话，则每个http header都加上token
        let token = sessionStorage.getItem('token')
        if (config.url.indexOf('/api/token/refresh/') >= 0) {
            return config
        }
        if (!Object.prototype.hasOwnProperty.call(config.headers, "Authorization") && token) {
            if (!isExpired()) {
                config.headers.Authorization = "JWT " + token;
            } else {
                if (!isRefreshing) {
                    isRefreshing = true;
                    axios.post("后台链接",
                        {"refresh": sessionStorage.getItem("refreshToken")})
                        .then(Response => {
                            isRefreshing = false;
                            store.commit('SET_TOKEN', Response.data.access)   //保存token用于拦截
                            sessionStorage.setItem("token", Response.data.access)
                            sessionStorage.setItem("TokenTime", new Date().getTime());//token刷新

                            onRrefreshed(Response.data.access);
                            /*执行onRefreshed函数后清空数组中保存的请求*/
                            refreshSubscribers = []
                        })
                        .catch(failResponse => {
                            console.log(failResponse);
                        });
                }

                let retry = new Promise((resolve) => {
                    /*(token) => {...}这个函数就是回调函数*/
                    subscribeTokenRefresh((token) => {
                        config.headers.Authorization = "JWT " + token;
                        resolve(config)
                    })
                });
                return retry;
            }

        }
        return config;
    },
);


new Vue({
    el: '#app',
    render: h => h(App),
    router,
    store,
    components: {App},
    template: '<App/>'
}).$mount('#app')


