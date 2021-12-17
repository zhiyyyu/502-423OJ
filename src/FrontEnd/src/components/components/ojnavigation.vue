<template>
  <div id="nav" v-if="$route.meta.keepAlive">
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

      <el-menu-item index="/about" v-if="Admin">
        <i class="el-icon-s-order"></i>
        <span>Admin</span>
      </el-menu-item>

      <el-button id="resister-button" type="primary" round v-on:click="resisterClick">
        Resister
      </el-button>
      <el-button id="login-button" type="primary" round v-on:click="loginClick">
        Login
      </el-button>

    </el-menu>
  </div>
</template>

<script>

export default {
  name: "nav",
  props:["isLoginForm","isResisterForm"],
  data() {
    return{
      load:false,
      loginForm:false,
      resisterForm:false
    }
  },
  methods:{
    //登录点击，弹出登录对话框组件
    loginClick:function () {
      this.$router.replace('/login');
      console.log("你点击了登录按钮");
    },
    //注册点击，弹出登录对话框组件
    resisterClick:function () {
      this.$router.replace('/register');
      console.log("你点击了注册按钮");
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

</style>