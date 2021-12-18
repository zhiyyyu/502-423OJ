<template>
  <div id="app">
    <el-card>
      <!--先做一个简单的模板-->
      <!--注册表单-->
      <el-row style="text-align: center">
        <strong style="font-size: xx-large" >{{username}}</strong>
        <divider></divider>
      </el-row>
      <el-row>
        <el-form id="form"
                 :model="userForm"
                 :rules="rules"
                 @keyup.native.enter="submitUserInfo">
          <!--用户名-->
          <el-form-item label="Username" prop="username">
            <el-input v-model="userForm.username"
                      autocomplete="off"
                      placeholder="please input your username">
              <el-icon class="el-icon-user"></el-icon>
            </el-input>
          </el-form-item>
          <!--邮箱-->
          <el-form-item label="Email" prop="email">
            <el-input type="email"
                      v-model="userForm.email"
                      autocomplete="off"
                      placeholder="please input your email">
              <el-icon class="el-icon-document"></el-icon>
            </el-input>
          </el-form-item>
          <!--密码-->
          <el-form-item label="Password" prop="password">
            <el-input type="password"
                      v-model="userForm.password"
                      autocomplete="off"
                      placeholder="please input your password">
              <el-icon class="el-icon-table-lamp"></el-icon>
            </el-input>
          </el-form-item>
          <!--再次输入密码-->
          <el-form-item label="Password Again" prop="passwordagain">
            <el-input v-model="userForm.passwordagain"
                      autocomplete="off"
                      placeholder="please input your password again">
              <el-icon class="el-icon-table-lamp"></el-icon>
            </el-input>
          </el-form-item>
          <el-button type="primary" round @click="submitUserInfo">
            Change
          </el-button>
        </el-form>
      </el-row>
    </el-card>
  </div>
</template>

<script>
import store from "@/store";
export default {
  name: "userSetting",
  data(){
    return{
      username:store.state.userform.username,
      userForm:{
        username:"",
        email:"",
        password:"",
        passwordagain:"",
      },
      rules:{
        username: [{required: true, message: 'please input your username', trigger: 'blur'}],
        email: [{required: true, message: 'please input your email', trigger: 'blur'}],
        password: [{required: true, message: 'please input your password', trigger: 'blur'}],
        passwordagain: [{required: true, message: 'please input your passwordagain', trigger: 'blur'}]
      }
    }
  },
  mounted() {
    console.log("暂时没想好");
  },
  methods:{
    submitUserInfo(){
      console.log("修改数据");
    }

  }
}
</script>

<style scoped>
#app{
  height: 550px;
}

</style>