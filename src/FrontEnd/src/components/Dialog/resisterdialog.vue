<template>
  <!--对话框-->
  <el-dialog id="logindialog"
             :visible.sync="dialogVisible"
             center="center"
             title="Resister">
    <!--注册表单-->
    <el-form id="form"
             :model="resisterform"
             :rules="rules"
             @keyup.native.enter="registerClick">
      <!--用户名-->
      <el-form-item label="Username" prop="username">
        <el-input v-model="resisterform.username"
                  autocomplete="off"
                  placeholder="please input your username">
          <el-icon class="el-icon-user"></el-icon>
        </el-input>
      </el-form-item>
      <!--邮箱-->
      <el-form-item label="Email" prop="email">
        <el-input type="email"
            v-model="resisterform.email"
            autocomplete="off"
            placeholder="please input your email">
          <el-icon class="el-icon-document"></el-icon>
        </el-input>
      </el-form-item>
      <!--密码-->
      <el-form-item label="Password" prop="password">
        <el-input type="password"
                  v-model="resisterform.password"
                  autocomplete="off"
                  placeholder="please input your password">
          <el-icon class="el-icon-table-lamp"></el-icon>
        </el-input>
      </el-form-item>
      <!--再次输入密码-->
      <el-form-item label="Password Again" prop="passwordagain">
        <el-input v-model="resisterform.passwordagain"
                  autocomplete="off"
                  placeholder="please input your password again">
          <el-icon class="el-icon-table-lamp"></el-icon>
        </el-input>
      </el-form-item>
      <!--准备做一个验证码功能，插眼-->
    </el-form>
    <!--注册按钮区-->
    <footer>
      <el-button type="primary" @click="registerClick">
        Resister
      </el-button>
      <el-button type="primary" @click="close">
        Cancel
      </el-button>
    </footer>

  </el-dialog>
</template>

<script>
export default {
  name: "resister-dialog",
  data() {
    return {
      dialogVisible: false,
      //后端传来的数据
      // dataForm:{
      //   code:"",
      //   data:{
      //     username: "",
      //     password: "",
      //     passwordagain:"",
      //     email: "",
      //   },
      //   msg:""
      // },
      resisterform: {
        username: "",
        password: "",
        passwordagain:"",
        email: "",
      },
      rules:{
        username: [{required: true, message: 'please input your username', trigger: 'blur'}],
        email: [{required: true, message: 'please input your email', trigger: 'blur'}],
        password: [{required: true, message: 'please input your password', trigger: 'blur'}],
        passwordagain: [{required: true, message: 'please input your passwordagain', trigger: 'blur'}]
      }
    };
  },
  methods: {
    /**
     * ref：打开对话框
     */
    open(){
      this.dialogVisible=true;
    },
    /**
     * ref：关闭对话框
     */
    close(){
      this.resisterform.username="";
      this.resisterform.email="";
      this.resisterform.password="";
      this.resisterform.passwordagain="";
      this.dialogVisible=false;
    },
    /**
     * 注册验证函数
     */
    registerClick() {
      if (!this.resisterform.username || !this.resisterform.password || !this.resisterform.passwordagain || !this.resisterform.email){
        this.$message.error("empty input!");
        return;
      }
      let checkEmail = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
      if (!checkEmail.test(this.resisterform.email)) {
        this.$message({message: '邮箱格式不正确', type: 'error'})
        return ;
      }
      this.$axios({
        method:"post",
        url:"/api/register/",
        data:this.resisterform
      }).then(response=>{
        if(response.data.code===0){
          console.log("恭喜用户注册成功");
          alert(response.data.msg);
        }else{
          console.log("注册失败");
        }
      }).catch(error=>{
        console.log("注册失败error="+error);
        this.$message.error("注册失败");
      })
      //还没有实现
      // sessionStorage.removeItem('token');
      //
      // this.$axios({
      //   method: 'post',
      //   url: "api/Register/",
      //   data: Qs.stringify(this.resisterform)
      // }).then(response => {
      //   console.log(response.data)
      //   if (response.data.code !== "0") {
      //     this.$message.error(response.data.msg);
      //     this.resisterform.password = ""
      //     this.resisterform.confirm = ""
      //     return
      //   } else {
      //     this.$message({
      //       message: "注册成功！",
      //       type: "success"
      //     });
      //   }
      //   this.dialogVisible = false;
      //   this.resisterform.password = "";
      //
      // }).catch(error => {
      //   this.$message.error(
      //       "服务器错误！" + "(" + JSON.stringify(error.response.data) + ")"
      //   );
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