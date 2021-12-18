<template>
  <!--登录对话框-->
  <el-dialog id="dialog"
             :visible.sync="dialogVisible"
             center="center"
             title="Login">
    <!--登录表单-->
    <el-form id="form"
             @keyup.native.enter="login"
             :rules="rules"
             :model="userform">
      <!--用户名-->
      <el-form-item label="Username" prop="username">
        <el-input type="text"
                  v-model="userform.username"
                  placeholder="please input your username">
        </el-input>
      </el-form-item>
      <!--密码-->
      <el-form-item label="Password" prop="password">
        <el-input type="password"
                  v-model="userform.password"
                  placeholder="please input your password">
        </el-input>
      </el-form-item>
    </el-form>
    <!--按钮-->
    <footer id="footer">
      <el-button type="primary" @click="login">Login</el-button>
      <el-button type="primary" @click="cancel">Cancel</el-button>
    </footer>
  </el-dialog>
</template>

<script>
import store from "@/store";
export default {
  name:"login-dialog",
  data() {
    return {
      //trigger失去焦点时触发表单验证
      rules:{
        username: [{required: true, message: 'empty username', trigger: 'blur'}],
        password: [{required: true, message: 'empty password', trigger: 'blur'}]
      },
      //检测登录状态
      checked: true,
      //用户登录表单
      userform: {
        username: "",
        password: ""
      },
      //是否显示对话框
      dialogVisible:false
    }
  },
  methods: {
    /**
     * ref方法：打开login对话框
     */
    open(){
      this.dialogVisible=true;
    },
    /**
     * close方法：打开login对话框
     */
    close(){
      this.dialogVisible=false;
    },
    /**
     * 取消登录，将输入框的数据清零
     */
    cancel(){
      this.userform.username="";
      this.userform.password=""
      this.dialogVisible=false;
      console.log("你点击了登录界面的Cancel按钮");
    },

    /**
     * 刚刚测试用的
     */
    // login(){
    //   store.state.userData.access="login";
    //   store.state.local.userform=this.userform;
    //   console.log("你点了登录进来");
    //   console.log("token = "+store.state.userData.access);
    //   this.$emit("colselogindialog",true);
    //   this.$router.replace("/");
    // }

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
          if(response.data.code===0){
            //将用户的数据存储在本地
            store.state.userData=response.data.data;
            //存储用户用户名和密码
            store.state.userform=this.userform;
            //子组件通知父组件nav关闭登录对话框以及登录注册按钮并显示用户按钮
            console.log("通知父组件nav");
            this.$emit("colselogindialog",true);
            //进入后，直接回到主界面，并通知导航栏关闭登录注册按钮，显示个人信息下拉框
            this.$router.push('/');
            return  true;
          }else if(response.data.code === "10004"){
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
#dialog{
  text-align: center;

}
#form{
  width: border-box;
}
#footer{
  text-align: center;
}


</style>