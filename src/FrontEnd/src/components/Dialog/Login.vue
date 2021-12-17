<template>
  <div id="Login">
    <el-dialog
        title="Login"
        v-model="dialogVisible"
        :visible.sync="dialogLoginVisible"
        :close-on-click-modal="false"
        center
        width="500px"
        @onchange="change"
        >
      <el-form
          :model="userLoginForm"
          @keyup.native.enter="loginClick"
          label-width="80px">

        <el-form-item label="username">
          <el-input
              v-model="userLoginForm.username"
              autocomplete="off"
              placeholder="不少于6个字符的用户名，必填">

          </el-input>
        </el-form-item>
        <el-form-item label="password">
          <el-input type="password"
                    v-model="userLoginForm.password"
                    autocomplete="off"
                    placeholder="不少于6个字符的密码，必填"></el-input>
        </el-form-item>

      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="loginCancel">Cancel</el-button>
        <el-button type="primary" @click="loginClick">Login</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>

export default {
  name: "Login",
  props:[
    'dialogVisible'
  ],
  data() {
    return {
      dialogLoginVisible: this.dialogVisible,
      userLoginForm: {
        username: "",
        password: ""
      },
    }
  },
  methods:{
    loginClick:function () {
      if(this.userLoginForm.username===""||this.userLoginForm.password===""){
        alert("请输入密码或账号");
        return ;
      }
      this.$axios({
        method:'put',
        url: '后台链接/',
        data:JSON.stringify(this.userLoginForm),
        headers: {"Content-Type": "application/json;charset=utf-8"}
      }).then(response => {
        console.log(response.data);
        if (response.data.code === 0) {
          console.log(Response.data);
          //store保存token
          this.$store.commit('SET_TOKEN', Response.data.data.access)   //保存token用于拦截
          this.$store.commit('SET_USER', this.userLoginForm.username)
          sessionStorage.setItem("token", Response.data.data.access);
          sessionStorage.setItem("refreshToken", Response.data.data.refresh);
          sessionStorage.setItem("password", this.userLoginForm.password);
          sessionStorage.setItem("userId", Response.data.data.id);       //用户Id
          sessionStorage.setItem("avatar", Response.data.data.avatar);
          sessionStorage.setItem("TokenTime",new Date().getTime());     //记录Token创造时间
          this.dialogLoginVisible=false;
          this.$router.replace(''); //登录到主页
        }
      }).catch(failResponse => {
        console.log(failResponse)
        this.$message.error("用户名或密码错误");
        alert("用户名或密码错误");
        this.dialogLoginVisible=true;
      }).finally(function () {

      })
    },
    loginCancel:function () {
      this.dialogLoginVisible=false;
    },
    change:function (value) {
      this.dialogLoginVisible=value;
    }
  }
}
</script>

<style scoped>

#login{
  border-radius: 5px;
}

#loginButton{
  text-align: center;
}
</style>