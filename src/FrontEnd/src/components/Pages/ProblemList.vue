<template>
  <div>
    <el-card>
      <el-row type="flex" justify="end" style="padding-bottom: 5px">
        <!-- 搜索框 -->
        <el-input v-model="input" placeholder="please input problem id" style="padding-right: 5px"></el-input>
        <!-- search按钮 -->
        <el-button type="primary" icon="el-icon-search" @click="handleSearch">search</el-button>
      </el-row>
      <el-row>
        <!-- 获取到的数据 -->
        <el-table :data="tableData" size="small"
                  height="500">
          <el-table-column prop="id" label="id" width="50px"/>
          <el-table-column prop="title" label="Title"/>
          <el-table-column prop="tags" label="Tags"/>
          <el-table-column prop="difficulty" label="Difficluty"/>
          <el-table-column prop="ac_rate" label="ACRate"/>
          <el-table-column label="operation" width="400" >
            <template slot-scope="scope">
              <el-button
                  size="mini"
                  @click="handleDetail(scope.$index, scope.row)">detail
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentpage"
            :page-sizes="[10]"
            :page-size="pagesize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="totalProblem"
        ></el-pagination>
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "ProblemList",
  data() {
    return {
      currentpage: 1,
      pagesize: 20,
      totalProblem: 1,
      input: "",
      tableData: ''
    }
  },
  methods: {
    //获取数据
    getData(limit, offset) {
      this.$axios({
        method: 'get',
        url: '/api/problemlist/',
        params: {
          size: limit,
          page: offset
        }
      }).then(response => {
        this.tableData = response.data;
        // if(response.data.detail !== ""){
        //   console.log(response.data);
        //   this.tableData = response.data.data;
        //   this.totalProblem = response.data.total;
        // }else{
        //   this.$message.error(response.data.detail)
        // }
        }).catch(error => {
        this.$message.error("服务器错误，获取数据失败");
        console.log("服务器错误！" + "(" + JSON.stringify(error) + ")");
      });
    },
    handleDetail(index, row) {
      console.log(index + " " + row);
      sessionStorage.setItem("ProblemInformation",JSON.stringify(row));
      //页面请求服务器该题的详情
      this.$router.push("/problemlist/"+index+"/");
    },
    handleSizeChange(val) {
      this.pagesize = val;
      this.getData(this.pagesize, this.currentpage);
    },
    handleCurrentChange(val) {
      this.currentpage = val;
      this.getData(this.pagesize, this.currentpage);
    },
    handleSearch(){
      this.$axios({
        method: 'get',
        url: '/api/problemlist/',
        params: {
          id:this.input
        }
      }).then(response=>{
        if(response.data.code===0){
          console.log(response.data.data);
          this.currentpage=1;
          this.totalProblem=1;
          this.tableData=[];
          this.tableData.push(response.data.data);
        }else{
          this.$message.error(response.data.msg);
        }}).catch(error=>{
        console.log(error)
        })
    }
  },
  mounted() {
    this.getData(this.pagesize, this.currentpage);
  }
}
</script>

<style scoped>

</style>