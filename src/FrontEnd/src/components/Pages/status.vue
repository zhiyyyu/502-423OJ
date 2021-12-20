<template>
  <div id="app">
    <el-card  id="card">
      <el-table :data="statusTable">
        <el-table-column prop="submit_time" label="submitTime"></el-table-column>
        <el-table-column prop="user_id" label="username"></el-table-column>
        <el-table-column prop="problem" label="problemId"></el-table-column>
        <el-table-column prop="result" label="status"></el-table-column>
        <el-table-column prop="static_info.time" label="time"></el-table-column>
        <el-table-column prop="static_info.memory" label="memory"></el-table-column>

      </el-table>
      <el-pagination
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="pageSize"
          layout="total, prev, pager, next, jumper"
          :total="totalStatus">
      </el-pagination>
    </el-card>

  </div>
</template>

<script>
export default {
  name: "status",
  data(){
    return {
      totalStatus:100,
      pageSize:10,
      currentPage:1,
      statusTable:[
        {
          submitTime:"2021-12-17 12:10:50",
          username:"法外狂徒张三",
          problemId:"1",
          status:"AC",
          time:"100ms",
          memory:"1M"
        },
        {
          submitTime:"2021-12-17 18:30:30",
          username:"老王",
          problemId:"1",
          status:"timeout",
          time:"1000ms",
          memory:"10M"
        }
      ]
    }
  },
  mounted() {
    this.getData(this.pageSize,this.currentPage);
  },
  methods:{
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getData(this.pageSize, this.currentPage);
    },
    getData(pageSize,requestPage){
      this.$axios({
        //方法
        method: 'get',
        //后端接口
        url: '/api/status/',
        //数据
        params: {
          size: pageSize,
          page: requestPage
        }
      }).then(response => {
        // if(response.data.code===0){
          //这里的数据结构还没有协商好
          this.totalStatus = response.data.count;
          this.statusTable = response.data.results;
          console.log(this.statusTable);
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