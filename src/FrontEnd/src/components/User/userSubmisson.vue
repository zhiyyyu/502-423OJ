<template>
  <div id="app">
    <el-card>
      <el-row style="text-align: center">
        <strong style="font-size: xx-large" >{{username}}</strong>
        <divider></divider>
      </el-row>
      <el-table :data="submissionTable">
        <el-table-column prop="submit_time" label="when"></el-table-column>
        <el-table-column prop="result" label="status"></el-table-column>
        <el-table-column prop="problem" label="id"></el-table-column>
        <el-table-column prop="static_info.time" label="time"></el-table-column>
        <el-table-column prop="static_info.memory" label="memory"></el-table-column>
        <el-table-column prop="language" label="language"></el-table-column>
      </el-table>
      <el-pagination
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="pageSize"
          layout="total, prev, pager, next, jumper"
          :total="totalSubmission">
      </el-pagination>
    </el-card>
  </div>
</template>

<script>
import store from "@/store";
export default {
  name: "userSubmisson",
  data(){
    return{
      username:store.state.userform.username,
      totalSubmission:100,
      currentPage:1,
      pageSize:10,
      submissionTable:[
        {
          when:"什么时候提交的",
          status:"题目解决状态",
          problem_id:"题目id",
          time:"空间消耗",
          memory:"时间消耗",
          language:"语言"
        },
        {
          when:"什么时候提交的",
          status:"题目解决状态",
          problem_id:"题目id",
          time:"空间消耗",
          memory:"时间消耗",
          language:"语言"
        }
      ]
    }
  },
  /**
   * 页面渲染完成后自动请求数据
   */
  mounted() {
    console.log("开始获取数据");
    this.getData(this.pageSize,this.currentPage);
  },
  methods:{
    handleCurrentChange(val){
      this.currentPage=val;
      this.getData(this.pageSize,this.currentPage);
    },
    getData(pageSize,requestPage){
      this.$axios({
        //方法
        method: 'get',
        //后端接口
        url: '/api/user_submissionlist/',
        //数据
        params: {
          size: pageSize,
          page: requestPage
        }
      }).then(response => {
        // if(response.data.code===0){
        //   //这里的数据结构还没有协商好
          this.submissionTable = response.data.results;
        // }else{
        //   console.log("接收数据错误");
        // }
      }).catch(error => {
        this.$message.error("服务器错误，获取数据失败");
        console.log("服务器错误！" + "(" + JSON.stringify(error) + ")");
      });
    }
  }
}
</script>

<style scoped>
#app{
  height: 550px;
}

</style>