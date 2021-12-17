<template>
  <el-card>
    <el-table :data="statusTable.results">
      <el-table-column prop="submit_time" label="submitTime"></el-table-column>
      <el-table-column prop="user_id" label="username"></el-table-column>
      <el-table-column prop="problem" label="problemId"></el-table-column>
      <el-table-column prop="result" label="status"></el-table-column>
      <el-table-column prop="static_info.time" label="time"></el-table-column>
      <el-table-column prop="static_info.memory" label="memory"></el-table-column>

    </el-table>
  </el-card>
</template>

<script>
export default {
  name: "status",
  data(){
    return {
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
  mounted:function(){
    console.log("mounted");
    this.$axios({
      //方法
      method: 'get',
      //后端接口
      url: '/api/submission_status/',
      //数据
      // params: {
      //   size: limit,
      //   page: offset
      // }
    }).then(response => {
      this.statusTable = response.data;
    }).catch(error => {
      this.$message.error("服务器错误，获取数据失败");
      console.log("服务器错误！" + "(" + JSON.stringify(error) + ")");
    });
  },
  methods: {

  },
}
</script>

<style scoped>

</style>