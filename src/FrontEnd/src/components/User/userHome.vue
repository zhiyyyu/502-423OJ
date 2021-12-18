<template>
  <div id="app">
    <el-card id="card">
      <el-header>
      <span style="font-size: xx-large">
        <strong>{{username}}</strong>
      </span>
        <divider></divider>
      </el-header>
      <el-main>
        <el-row class="row">
            <strong>Solved:{{userData.accepted_number}}</strong>
        </el-row>
        <el-row class="row">
          <strong>Submissions:{{userData.submission_number}}</strong>
        </el-row>
      </el-main>
    </el-card>
  </div>
</template>

<script>
import store from "@/store";
export default {
  name: "userhome",
  data(){
    return{
      username:store.state.userform.username,
      userData:{
        //解决了多少到问题
        accepted_number:0,
        //提交了多少到问题
        submission_number:0,
        //得分
      }
    }
  },
  /**
   * 页面加载完成后，请求数据
   */
  mounted() {
    console.log("开始获取数据");
    this.$axios({
      method:'get',
      url:'api/userprofile/',
      params:{
        //请求参数为用户的id,你可以自己更改请求参数
        username:store.state.userData.id
      }
    }).then(response=>{
      // if(response.data.code===0){
      //   console.log("userhome返回数据成功");
        this.userData=response.data.results[store.state.userData.id];
        console.log(this.userData);
      // }else{
      //   console.log("userhome的code不等于0，返回数据错误");
      // }
    }).catch(error=>{
      console.log(error);

    })
  }
}
</script>

<style scoped>
#app{
  text-align: center;
  height: 550px;
}
#card{
  height: 550px;
}
.row{
  margin: 20px 20px;
}

</style>