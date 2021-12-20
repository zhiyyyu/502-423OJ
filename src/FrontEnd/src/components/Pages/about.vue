<template>
  <div id="app">
    <el-card>
      <el-table :data="aboutTable">
        <el-table-column prop="time" label="time"></el-table-column>
        <el-table-column prop="msg" label="msg"></el-table-column>
      </el-table>
      <el-pagination
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="pageSize"
          layout="total, prev, pager, next, jumper"
          :total="totalAbout">
      </el-pagination>
    </el-card>

  </div>
</template>

<script>
export default {
  name: "about",
  data(){
    return{
      totalAbout:100,
      pageSize:10,
      currentPage:1,
      aboutTable:[
          {
          time:"2021.12.11",
          msg:"暂时没有相关光更新的消息",
        },
        {
          time:"2021.12.17",
          msg:"更新了About page",
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
        url: '/api/about/',
        //数据
        params: {
          size: pageSize,
          page: requestPage
        }
      }).then(response => {
        this.aboutTable = response.data;
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