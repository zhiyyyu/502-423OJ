<template>
  <div id="app">
    <!--题目列表-->
    <el-card>
      <!--搜索栏，水平排列-->
      <el-row type="flex" justify="end">
        <el-col :span="16" style="text-align: center">
          <span><b>Problem List</b></span>
        </el-col>
        <el-col :span="6">
          <el-input v-model="searchInput" placeholder="please input problem id" size="mini"></el-input>
        </el-col>
        <el-col :span="2">
          <el-button type="primary" icon="el-icon-search" @click="searchProblem" size="mini">search</el-button>
        </el-col>
      </el-row>
      <!--题目栏-->
      <el-row>
        <!--题目表格-->
        <el-table :data="problemTable"
                  size="small"
                  height="500px">
          <!--题目表格标题-->
          <el-table-column prop="id" label="id"/>
          <el-table-column prop="title" label="Title"/>
          <el-table-column prop="tags" label="Tags"/>
          <el-table-column prop="difficulty" label="Difficulty"/>
          <el-table-column label="operation" >
            <!--组件通过插槽slot传递数据-->
            <template slot-scope="scope">
              <el-button
                  size="mini"
                  @click="handleDetail(scope.$index, scope.row)">detail
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <!--分页器-->
        <el-pagination
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-size="pageSize"
            layout="total, prev, pager, next, jumper"
            :total="totalProblem">
        </el-pagination>
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "problem-list",
  data() {
    return {
      //当前页
      currentPage: 1,
      //页大小（即题目容量）
      pageSize: 10,
      //题目数量
      totalProblem: 30,
      //搜索输入
      searchInput: "",
      //问题Table
      problemTable:[
          //问题的数据结果
          {
        ac_number:1,
        author:{
          data_joined:"time",
          id:1,
          last_join:"time",
          username:"张三"
        },
        body:"hello word",
        created:"time",
        difficulty: "Easy",
        id: 1,
        memory_limit: 1,
        submission_number: 1,
        tags: ["g"],
        time_limit: 1000,
        title:"helloword",
        url:"http://locahost:8000/api/problemlist/1/",
      },
        {
        ac_number:1,
        author:{
          data_joined:"time",
          id:1,
          last_join:"time",
          username:"张四"
        },
        body:"hello word",
        created:"time",
        difficulty: "Easy",
        id: 2,
        memory_limit: 1,
        submission_number: 1,
        tags: ["g"],
        time_limit: 10,
        title:"helloword",
        url:"http://locahost:8000/api/problemlist/1/",
      }],
      //用来接收对方来的数据
      data:null
    }
  },
  methods: {
    /**
     * 从后端获取数据
     * @param limit 题目条数
     * @param offset  偏移量
     */
    getData(limit, offset) {
      this.$axios({
        //方法
        method: 'get',
        //后端接口
        url: '/api/problemlist/',
        //数据
        params: {
          size: limit,
          page: offset
        }
      }).then(response => {

        this.data = response.data;
        //问题table列表接受results列表
        this.problemTable=this.data.results;
      }).catch(error => {
        this.$message.error("服务器错误，获取数据失败");
        console.log("服务器错误！" + "(" + JSON.stringify(error) + ")");
      });
    },
    /**
     *
     * @param index
     * @param row
     */
    handleDetail(index, row) {
      console.log("index="+index+", row="+row);
      //存储json数据
      sessionStorage.setItem("problemID",JSON.stringify(row));
      console.log("进入详情页面前存储题目"+sessionStorage.getItem("problemID"));
      //进入该题界面
      this.$router.push("/problemlist/"+index+"/");
    },
    /**
     * 处理当前为第几页
     * @param val
     */
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getData(this.pageSize, this.currentPage);
    },
    /**
     * 搜索题目
     */
    searchProblem(){
      //正则表达式检测输入是否规范
      let testId = /[0-9]/;
      if(!testId.test(this.searchInput)){
        this.$message.error("请输入正确的题目id");
        return;
      }
      //控制台打印数据
      console.log("你搜索的题目id为="+this.searchInput);
      let data=sessionStorage.getItem(this.searchInput.toString());
      console.log(data);
      if(data!==null){
        console.log("在本地存储找到了题目");
        this.currentPage=1;
        this.totalProblem=1;
        console.log(data)
        this.problemTable=[JSON.parse(data)];
        console.log(JSON.parse(data));
        return;
      }
      //否则向后端请求数据
      this.$axios({
        method: 'get',
        url: '/api/problemlist/',
        params: {
          id:this.searchInput
        }
      }).then(response=>{
        //获取数据成功
        if(response.data.code===0){
          console.log(response.data);
          this.currentPage=1;
          this.totalProblem=1;
          this.problemTable=[response.data];
        }else{
          this.$message.error("problem does not exist...");
        }
      }).catch(error=>{
          console.log(error);
        this.$message.error("服务器错误");
      })
    }
  },
  /**
   * 页面加载时自动运行获取一页的数据
   */
  mounted() {
    this.getData(this.pageSize, this.currentPage);
    console.log("将数据存储在本地");
    for(let i=0; i<this.problemTable.length; i++){
      sessionStorage.setItem(this.problemTable[i].id.toString(),JSON.stringify(this.problemTable[i]));
    }
  }
}
</script>

<style scoped>
#app{
  height: 550px;
}

</style>