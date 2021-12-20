<template>
  <el-card style="text-align: center">
    <!--先做一个简单的模板-->
    <!--注册表单-->
    <div style="height: 550px; overflow-y: scroll" >
      <el-row>
        <el-col :span="8">
          <el-form id="form"
                   :model="userForm"
                   @keyup.native.enter="submitUserInfo">
            <!--用户名-->
            <el-form-item label="Username">
              <el-input v-model="userForm.username"
                        autocomplete="off"
                        placeholder="please input your username">
                <el-icon class="el-icon-user"></el-icon>
              </el-input>
            </el-form-item>
            <!--邮箱-->
            <el-form-item label="Email">
              <el-input type="email"
                        v-model="userForm.email"
                        autocomplete="off"
                        placeholder="please input your email">
                <el-icon class="el-icon-document"></el-icon>
              </el-input>
            </el-form-item>
            <!--密码-->
            <el-form-item label="Password">
              <el-input v-model="userForm.password"
                        autocomplete="off"
                        placeholder="please input your password">
                <el-icon class="el-icon-table-lamp"></el-icon>
              </el-input>
            </el-form-item>
            <el-form-item label="Motto">
              <el-input v-model="userForm.motto"
                        autocomplete="off"
                        placeholder="please input your motto">
                <el-icon class="el-icon-table-lamp"></el-icon>
              </el-input>
            </el-form-item>
            <el-form-item label="Nickname">
              <el-input v-model="userForm.nickname"
                        autocomplete="off"
                        placeholder="please input your nickname">
                <el-icon class="el-icon-table-lamp"></el-icon>
              </el-input>
            </el-form-item>

            <el-button type="primary" round @click="submitUserInfo">
              Update
            </el-button>
          </el-form>
        </el-col>
        <el-col :span="1">
          <br/>
        </el-col>
        <el-col :span="14" style="text-align: center" >
          <el-carousel :interval="4000" height="250px" autoplay type="card">
            <el-carousel-item >
              <h3 style="font-size: xx-large;color: cadetblue" >username</h3>
              <h3 style="font-size: x-large;color: black">{{userForm.user.username}}</h3>
            </el-carousel-item>
            <el-carousel-item >
              <h3 style="font-size: xx-large;color: cadetblue" >email</h3>
              <h3 style="font-size: x-large;color: black">{{ userForm.user.email }}</h3>
            </el-carousel-item>
            <el-carousel-item >
              <h3 style="font-size: xx-large;color: cadetblue" >nickname</h3>
              <h3 style="font-size: x-large;color: black">{{ userForm.nickname }}</h3>
            </el-carousel-item>
            <el-carousel-item >
              <h3 style="font-size: xx-large;color: cadetblue" >motto</h3>
              <h3 style="font-size: x-large;color: black">{{ userForm.motto}}</h3>
            </el-carousel-item>
          </el-carousel>
        </el-col>

      </el-row>
    </div>

  </el-card>
</template>

<script>
import store from "@/store";
export default {
  name: "userSetting",
  data(){
    return{
      username:store.state.userform.username,
      userForm:{
        
        nickname:"昵称",
        motto:"座右铭",
        user:{
          username:"用户名",
          email:"邮件",
          password:"密码",
        }
      },
      userToCard:[
        {title:"username",content:"张三"},
        {title:"email",content:"111@xxx.com"},
        {title:"nickname",content:"卷王"},
        {title:"motto",content:"我要卷死他们"},
      ],
      activeName2: 'first',
      tabPosition: 'top'
    }
  },
  mounted() {
    console.log("Setting页面加载时获取用户信息页面");
    this.getData();
  },
  methods:{
    /**
     * 提交用户修改的信息
     */
    submitUserInfo(){
      console.log("提交用户的update");
      this.$axios({
        method:"post",
        url:"/api/userprofile/",
        data:this.userForm
      }).then(response=>{
        console.log("前端收到数据"+response.data);
        //只需要返回成功修改与否即可
        this.$message.success(response.data.msg);
      }).catch(error=>{
        this.$message.error("服务器错误，获取数据失败");
        console.log("服务器错误！" + "(" + JSON.stringify(error) + ")");
      })
    },
    /**
     * 获取数据
     */
    getData(){
      console.log("获取用户信息");
      this.$axios({
        method:"get",
        url:"/api/userprofile/"+store.state.userData.id+"/",
      }).then(response=>{
        console.log("收到数据");
        //收到的数据结构与userForm一致
        this.userForm=response.data;
      }).catch(error=>{
        this.$message.error("服务器错误，获取数据失败");
        console.log("服务器错误！" + "(" + JSON.stringify(error) + ")");
      })

    }
  }
}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 100px;
  margin: 0;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

</style>