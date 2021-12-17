<template>
  <el-card id="app">
    <el-form :model="form"
             @keyup.native.enter="registerClick"
             label-width="70px">

      <el-form-item label="username">
        <el-input v-model="form.username"
                  autocomplete="off"
                  placeholder="username"></el-input>
      </el-form-item>

      <el-form-item label="nickname">
        <el-input v-model="form.nickname"
                  autocomplete="off"
                  placeholder="nickname"></el-input>
      </el-form-item>

      <el-form-item label="password">
        <el-input type="password"
                  v-model="form.password"
                  autocomplete="off"
                  placeholder="password"></el-input>
      </el-form-item>

      <el-form-item label="email">
        <el-input
            v-model="form.email"
            autocomplete="off"
            placeholder="email"></el-input>
      </el-form-item>

      <el-button type="primary" @click="registerClick">
        Resister
      </el-button>
    </el-form>
  </el-card>
</template>

<script>
import Qs from 'qs'

export default {
  name: "resister",
  data() {
    return {
      dialogRegisterVisible: false,
      form: {
        nickname:"",
        username: "",
        password: "",
        email: "",
      },
    };
  },
  methods: {
    registerClick() {
      if (
          !this.form.username ||
          !this.form.password ||
          !this.form.nickname ||
          !this.form.email
      ) {
        this.$message.error("字段不能为空！");
        return;
      }
      if (this.form.username.length < 6) {
        this.$message.error("用户名太短！");
        return;
      }
      if (this.form.nickname.length < 6) {
        this.$message.error("用户名太短！");
        return;
      }
      if (this.form.password.length < 6) {
        this.$message.error("密码太短！");
        return;
      }
      if (
          this.form.username.indexOf("|") >= 0 ||
          this.form.username.indexOf(".") >= 0 ||
          this.form.username.indexOf("#") >= 0
      ) {
        this.$message.error("用户名包含非法字符！");
        return;
      }
      let regEmail = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
      if (!regEmail.test(this.form.email)) {
        this.$message({
          message: '邮箱格式不正确',
          type: 'error'
        })
        return ;
      }

      sessionStorage.removeItem('token');

      this.$axios({
        method: 'post',
        url: "/api/register/",
        data: Qs.stringify(this.form)
      }).then(response => {
        console.log(response.data)
        if (response.data.code !== "0") {
          this.$message.error(response.data.msg);
          this.form.password = ""
          this.form.confirm = ""
          return
        } else {
          this.$message({
            message: "注册成功！",
            type: "success"
          });
        }
        this.dialogRegisterVisible = false;
        this.form.password = "";

      }).catch(error => {
        this.$message.error(
            "服务器错误！" + "(" + JSON.stringify(error.response.data) + ")"
        );
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


</style>