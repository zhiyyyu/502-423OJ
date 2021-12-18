<template>
  <div id="nav" v-if="$route.meta['keepAlive']">
    <el-menu id="nav-menu"
             :default-active="$route.path"
             mode="horizontal"
             v-bind:router="true">
      <el-menu-item index="/">
        <i class="el-icon-s-home"></i>
        <span>Home</span>
      </el-menu-item>

      <el-menu-item index="/problemlist" >
        <i class="el-icon-document"></i>
        <span>ProblemList</span>
      </el-menu-item>

      <el-menu-item index="/status">
        <i class="el-icon-tickets"></i>
        <span>Status</span>
      </el-menu-item>

      <el-menu-item index="/rank">
        <i class="el-icon-star-on"></i>
        <span>Rank</span>
      </el-menu-item>

      <el-menu-item index="/about">
        <i class="el-icon-s-order"></i>
        <span>About</span>
      </el-menu-item>

      <!--按钮区-->
      <el-button id="resister-button"
                 type="primary"
                 round
                 v-if="isShowButton"
                 v-on:click="resisterClick">
        Resister
      </el-button>
      <el-button id="login-button"
                 type="primary"
                 round
                 v-if="isShowButton"
                 v-on:click="loginClick">
        Login
      </el-button>
      <!--用户信息按钮-->
      <el-dropdown  @command="handleCommand" id="user-button" v-if="isShowUserInfo">
        <el-button type="primary" round v-if="isShowUserInfo">
          {{user.username}}
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="Home">Home</el-dropdown-item>
          <el-dropdown-item command="Submission">Submission</el-dropdown-item>
          <el-dropdown-item command="Setting">Setting</el-dropdown-item>
          <el-dropdown-item command="Logout">Logout</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </el-menu>
    <div id="dialog">
      <logindialog ref="logindialog" v-on:colselogindialog="dealLogin"></logindialog>
      <resisterdialog ref="resisterdialog"></resisterdialog>
    </div>
  </div>
</template>

<script>
import logindialog from "@/components/Dialog/logindialog";
import resisterdialog from "@/components/Dialog/resisterdialog";
import store from "@/store";
export default {
  name: "oj-navigation",
  components:{
    logindialog,
    resisterdialog,
  },
  data() {
    return{
      isShowButton: false,
      isShowUserInfo: true,
      user:store.state.userform,
    }
  },
  created() {
    this.$refs.logindialog.close();
    this.$refs.resisterdialog.close();
    console.log("导航栏创建 token="+store.state.userData.access);
  },
  /**
   * 组件渲染完毕后，判断token是否存在，若存在则打开用户栏关闭登录注册按钮，否则反之
   */
  mounted() {
    console.log("导航栏加载完成 token="+store.state.userData.access);
    if(store.state.userData.access){
      console.log("设置");
      this.isShowButton= false;
      this.isShowUserInfo= true;
      document.getElementById("resister-button").style.display="none";
      document.getElementById("login-button").style.display="none";
      document.getElementById("user-button").style.display="block";
    }else{
      this.isShowButton= true;
      this.isShowUserInfo= false;
      document.getElementById("resister-button").style.display="block";
      document.getElementById("login-button").style.display="block";
      document.getElementById("user-button").style.display="none";
    }
  },
  methods:{
    //登录点击，弹出登录对话框组件
    loginClick:function () {
      this.$refs.logindialog.open();
      console.log("你点击了登录按钮");
    },
    //注册点击，弹出登录对话框组件
    resisterClick:function () {
      this.$refs.resisterdialog.open();
      console.log("你点击了注册按钮");
    },
    handleCommand(val){
      switch (val){
        case "Home":{
          this.goUserHome();
        }break;
        case "Submission":{
          this.goUserSubmission();
        }break;
        case "Setting":{
          this.goUserSetting();
        }break;
        default:{
          this.logout();
        }break;
      }
    },
    goUserHome(){
      this.$router.push('/userhome');
    },
    goUserSubmission(){
      this.$router.push('/usersubmission');
    },
    goUserSetting(){
      this.$router.push('/usersetting');
    },
    logout(){
      console.log(this.user.username+"用户已退出");
      store.state.userData.username="";
      store.state.userData.access="";
      this.isShowUserInfo=false;
      this.isShowButton=true;
      //退出后，回到主页
      this.$router.replace("/");
    },
    /**
     * 新增的函数
     * 用来处理登录后关闭对话框的操作以及隐藏登录注册按钮显示用户信息
     */
    dealLogin(){
      console.log("父组件nav接收到子组件logindialog的反馈");
      this.$refs.logindialog.close();
      this.isShowUserInfo=true;
      this.isShowButton=false;
    }
  }
}
</script>

<style scoped>
#nav {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
  position: relative;
  background-color: whitesmoke;
}
#resister-button{
  margin-top: 1%;
  margin-left: 1%;
  float: right;
}
#login-button{
  margin-top: 1%;
  margin-left: 1%;
  float: right;
}
#user-button{
  margin-top: 1%;
  margin-left: 1%;
  float: right;
}

</style>