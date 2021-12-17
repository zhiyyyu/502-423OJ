<template>
  <div>
    <!-- <el-dialog title="登陆"
               :visible.sync="dialogLoginVisible"
               :close-on-click-modal="false"
               center
               width="450px"> -->
      <el-form :model="loginForm" :rules="rules"
              class="login-container" label-position="left"
              label-width="0px" v-loading="loading">
        <h3 class="login_title">502-423OJ</h3>
        <el-form-item prop="username">
          <el-input type="text" v-model="loginForm.username"
                    auto-complete="off" placeholder="邮箱或用户名"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" v-model="loginForm.password"
                    auto-complete="off" placeholder="密码"></el-input>
        </el-form-item>

        <el-form-item style="width: 100%">
          <el-button type="primary" style="width: 40%;background: #505458;border: none" v-on:click="login">登录</el-button>
          <el-button type="primary" style="width: 40%;background: #505458;border: none" @click="register">注册</el-button>
        </el-form-item>

        <el-form-item>
          <el-link type="success" @click="verify">找回密码</el-link>
        </el-form-item>
        <Register ref="RegisterDialog"></Register>
        <Verify ref="VerifyDialog"></Verify>
      </el-form>
    <!-- </el-dialog> -->
  </div>
</template>

<script>
import Qs from 'qs'

export default {
  data() {
    return {
      dialogLoginVisible: true,
      rules: {
        username: [{required: true, message: '邮箱不能为空', trigger: 'blur'}],
        password: [{required: true, message: '密码不能为空', trigger: 'blur'}]
      },
      checked: true,
      loginForm: {
        username: "",
        password: ""
      },
    }
  },
  methods: {
    login() {
      if (!this.userform.username || !this.userform.password) {
        this.$message.error("字段不能为空！");
        return;
      }
      if (this.userform.username.length < 6) {
        this.$message.error("用户名太短！");
        return;
      }
      if (this.userform.password.length < 6) {
        this.$message.error("密码太短！");
        return;
      }

      sessionStorage.removeItem('token')
      this.$axios({
        method: 'post',
        url: '/api/login/',
        data: Qs.stringify(this.userform)
      }).then(Response => {
        console.log(Response.data);
        this.dialogLoginVisible = true;
        if (Response.data.code === "10004") {
          this.userform.password = "";
          this.$message.error("登录时密码错误");
          return;
        }

        if (Response.data.code === 0) {
          console.log(Response.data);
          //store保存token
          this.$store.commit('SET_TOKEN', Response.data.data.access)   //保存token用于拦截
          this.$store.commit('SET_USER', this.userform.username)
          sessionStorage.setItem("token", Response.data.data.access);
          sessionStorage.setItem("refreshToken", Response.data.data.refresh);
          sessionStorage.setItem("password", this.userform.password);
          sessionStorage.setItem("userId", Response.data.data.id);       //用户Id
          sessionStorage.setItem("avatar", Response.data.data.avatar);
          sessionStorage.setItem("TokenTime",new Date().getTime());     //记录Token创造时间
          this.$router.replace({path: '/'});
        }else{
          this.$message.error(Response.data.msg)
        }
      }).catch(failResponse => {
            console.log(failResponse)
            this.$message.error("用户名或密码错误");
      });
    }
  }
}
</script>

<style scoped>
  #app{
    margin: 100px 20%;
    padding-top: 30px;
    text-align: center;
  }

  .login-container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 90px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }

  .login_title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }

</style>