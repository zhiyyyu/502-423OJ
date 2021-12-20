<template>
  <div id="app">
    <el-card>
      <el-table :data="rankTable">
        <el-table-column prop="user" label="rank"></el-table-column>
        <el-table-column prop="submission_number" label="submission_number"></el-table-column>
        <el-table-column prop="accepted_number" label="ac-number"></el-table-column>
      </el-table>
      <el-pagination
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="pageSize"
          layout="total, prev, pager, next, jumper"
          :total="totalRank">
      </el-pagination>
    </el-card>

  </div>
</template>

<script>
export default {
  name: "rank",
  data(){
    return{
      totalRank:100,
      pageSize:10,
      currentPage:1,
      rankTable:[{
        rank:1,
        username:"123",
        ac_number:100
      },
        {
          rank:2,
          username:"456",
          ac_number:33
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
        url: '/api/rank/',
        //数据
        params: {
          size: pageSize,
          page: requestPage
        }
      }).then(response => {
          this.rankTable = response.data.results;
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