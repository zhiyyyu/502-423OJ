<template>
  <el-card id="app" >
    <el-form id="form"
             :model="userform"
             :rules="rules"
             ref="loginRef"
             label-width="100px"
             class="demo-ruleForm">
      <!--用户名-->
      <el-form-item label="username" prop="username" >
        <el-input type="text"
                  v-model="userform.username">
        </el-input>
      </el-form-item>
      <!--密码-->
      <el-form-item label="password" prop="password" >
        <el-input type="password"
                  v-model="userform.password">
        </el-input>
      </el-form-item>
      <!--按钮-->
      <el-form-item>
        <el-button type="primary" @click="cancel">Cancel</el-button>
        <el-button type="primary" @click="login">Login</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script>
//

export default {
  name:"login",
  data() {
    return {
      //表单验证规则
      rules: {
        username: [{required: true, message: '邮箱不能为空', trigger: 'blur'}],
        password: [{required: true, message: '密码不能为空', trigger: 'blur'}]
      },
      checked: true,
      //用户登录表单
      userform: {
        username: "",
        password: ""
      },
    }
  },
  methods: {
    /**
     * 取消登录，将输入框的数据清零
     */
    cancel(){
      this.userform.username="";
      this.userform.password=""
      console.log("你点击了登录界面的Cancel按钮");
    },
    /**
     * 登录验证
     */
    login() {
      //控制台输出user-form中的数据
      console.log("["+this.userform.username+","+this.userform.password+"]");
      //前端检测数据是否合理
      if (!this.userform.username || !this.userform.password) {
        this.$message.error("Please enter your username and password");
      }else {
        //向后端传递数据
        this.$axios({
          method:"post",  //post方法
          url:"api/login/",  //后端接口路径
          data:this.userform  //传输的数据为用户表单
        }).then(response => {
          //控制台输出从后端收到的数据
          console.log(response.data);
          if(response.data.code === "10004"){
            console.log("用户名或密码错误");
            return false;
          }
        }).catch(error =>{
          console.log(error.toString())
        })
      }
      return true;


      // sessionStorage.removeItem('token')
      // this.$axios({
      //   method: 'post',
      //   url: '/api/login/',
      //   data: Qs.stringify(this.userform)
      // }).then(Response => {
      //   console.log(Response.data);
      //   if (Response.data.code === "10004") {
      //     this.userform.password = "";
      //     this.$message.error("登录时密码错误");
      //     return;
      //   }
      //
      //   if (Response.data.code === 0) {
      //     console.log(Response.data);
      //     //store保存token
      //     this.$store.commit('SET_TOKEN', Response.data.data.access)   //保存token用于拦截
      //     this.$store.commit('SET_USER', this.userform.username)
      //     sessionStorage.setItem("token", Response.data.data.access);
      //     sessionStorage.setItem("refreshToken", Response.data.data.refresh);
      //     sessionStorage.setItem("password", this.userform.password);
      //     sessionStorage.setItem("userId", Response.data.data.id);       //用户Id
      //     sessionStorage.setItem("avatar", Response.data.data.avatar);
      //     sessionStorage.setItem("TokenTime",new Date().getTime());     //记录Token创造时间
      //     this.$router.replace({path: '/'});
      //   }else{
      //     this.$message.error(Response.data.msg)
      //   }
      // }).catch(failResponse => {
      //       console.log(failResponse)
      //       this.$message.error("用户名或密码错误");
      // });
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