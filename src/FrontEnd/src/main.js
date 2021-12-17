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
/**
 * ElementUI 的 size 用于改变组件的默认尺寸，zIndex 设置弹框的初始 z-index（默认值：2000）
 */
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 全局引入vue-codemirror
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



//使用引入的模块
Vue.use(VueClipboard)
Vue.config.productionTip = false

Vue.use(ViewUI);
Vue.prototype.$md5 = md5

Vue.use(codemirror)
Vue.use(ElementUI);

Vue.prototype.$axios = axios    //全局注册，使用方法为:this.$axios
axios.defaults.baseURL = "http://localhost:8000/";
Vue.use(VueParticles)


Vue.config.productionTip = false



/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store,
  components: {App},
  template: '<App/>'
}).$mount('#app')


// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {

      if (to.meta.requireAuth) {
        // console.log(store.state.user.token)
        if (store.state.user.token) {   //如果存在token则直接跳转
          next()
        } else {
          next({            //否则跳回登录界面
            path: '/',
            query: {redirect: to.fullPath}
          })
        }
      } else {
        next()
      }
    }
)
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
            axios.post("http://localhost:8000/",
                {"refresh": sessionStorage.getItem("refreshToken")})
                .then(Response => {
                  isRefreshing = false;
                  store.commit('SET_TOKEN', Response.data.access)   //保存token用于拦截
                  sessionStorage.setItem("token", Response.data.access)
                  sessionStorage.setItem("TokenTime", new Date().getTime());//token刷新

                  onRrefreshed(Response.data.access);
                  /*执行onRefreshed函数后清空数组中保存的请求*/
                  refreshSubscribers = []
                }).catch(failResponse => {
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
    }
);

