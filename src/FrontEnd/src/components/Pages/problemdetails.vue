<template>
  <div id="app">
    <!--将描述区和写代码区左右分割-->
    <el-row>
      <!--各占据一半-->
      <el-col :span="12">
        <el-card>
          <div style="height: 600px;">
            <el-tabs :tab-position="tabPosition" style="height: 100px;">
              <el-tab-pane label="describe">
                <!--题目描述-->
                <div>
                  <!--每行水平排列-->
                  <!--标题-->
                  <el-row class="main-row">
                    <strong style="font-size: x-large">{{ problemDetail.title }}</strong>
                  </el-row>
                  <el-row class="main-row">
                    <span>Description：</span><br />
                    <markdown-it-vue class="md-body" :content="problemDetail.body"></markdown-it-vue>
                  </el-row>
                  <el-row class="main-row">
                    <span>Difficulty：</span><br />
                    {{ problemDetail.difficulty }}
                  </el-row>
                  <el-row class="main-row">
                    <span>Memory-Limit：</span><br />
                    {{ problemDetail.memory_limit }}
                  </el-row>
                  <el-row class="main-row">
                    <span>Time-Limit：</span><br />
                    {{ problemDetail.time_limit }}
                  </el-row>
                </div>
              </el-tab-pane>
              <el-tab-pane label="comment">
                <!--评论-->
                <div>
                  {{problemDetail.comments}}
                </div>
              </el-tab-pane>
            </el-tabs>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
       <el-card>
         <div style="height: 600px">
           <el-row class="footer-row">
             <!--重置代码按钮-->
             <el-button round @click="reset">
               reset
             </el-button>
             <!--语言选择下拉按钮-->
             <el-dropdown>
               <el-button round>
                 {{language_choose}}
                 <i class="el-icon-arrow-down"></i>
               </el-button>
               <el-dropdown-menu slot="dropdown">
                 <el-dropdown-item @click.native="choose_language_C">C</el-dropdown-item>
                 <el-dropdown-item @click.native="choose_language_C_Plus">C++</el-dropdown-item>
               </el-dropdown-menu>
             </el-dropdown>
             <el-button round :loading="loading" :type="type">
               {{status}}
             </el-button>
           </el-row >
           <divider></divider>
           <el-row class="footer-row">
             <codemirror v-model="sendInfo.code"
                         :options="cmdOptions"
                         @ready="codemirrorReady"
                         ref="codeMirror">
             </codemirror>
           </el-row>
           <divider></divider>
           <!--提交、返回按钮-->
           <el-row class="footer-row">
             <el-button icon="el-icon-check" round @click="submitCode">Submit</el-button>
             <el-button  round @click="back">Back</el-button>
           </el-row>
         </div>
       </el-card>
      </el-col>
    </el-row>
  </div>

</template>

<script>
import MarkdownItVue from 'markdown-it-vue'
import 'markdown-it-vue/dist/markdown-it-vue.css'
import { codemirror } from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'
require("codemirror/lib/codemirror.css");
require("codemirror/theme/base16-light.css");
require("codemirror/mode/clike/clike");
require("codemirror/mode/python/python")
require("codemirror/addon/edit/matchbrackets.js")

export default {
  name: "ProblemDetail",
  components: {
    MarkdownItVue,
    codemirror
  },
  data() {
    return {
      tabPosition:"top",
      //获取提交界面的题目ID
      submission_id:sessionStorage.getItem("ProblemID"),
      //详情页面的数据结构
      problemDetail:{
        ac_number:0,
        body:"<p>print hello world</p>" +
            "<p>input: none </p>" +
            "<p>output: hello word </p>\"",
        body_html:"",
        comments:[
          {id:0,content:"好简单呀"},
          {id:1,content:"你真厉害"}
        ],
        created:"xxxx",
        difficulty:"Easy",
        id:1,
        memory_limit:1000,
        submission_number:0,
        tags:["g"],
        time_limit:1000,
        title:"hello world",
        toc_html:"xxx",
        url:"xxx"
      },
      //表示代码正在提交
      loading:false,
      status:"WAIT",
      type:"",
      timeoutObj:"",


      // //老数据结构
      // //问题的数据结构
      // problemData: {
      //   ac_number:1,
      //   author:{
      //     data_joined:"time",
      //     id:1,
      //     last_join:"time",
      //     username:"张三"
      //   },
      //   body:"hello word",
      //   created:"time",
      //   difficulty: "Easy",
      //   id: 1,
      //   memory_limit: 1,
      //   submission_number: 1,
      //   tags: ["g"],
      //   time_limit: 100,
      //   title:"helloword",
      //   url:"http://locahost:8000/api/problemlist/1/",
      // },


      //接口接收到的数据结构
      submissionData:{
        code:"",
        create_time:"time",
        id:1,
        info:{
          error_code:1,
          id:1,
          score:100,
        },
        language:"",
        problem:{
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
          time_limit: 100,
          title:"helloword",
          url:"http://locahost:8000/api/problemlist/1/",
        },
        result:1,
        static_info:{
          id:1,
          space:0,
          time:200
        },
        user_id:0
      },

      // language_mode: 'text/x-c++src',
      cmdOptions: {
        tabSize: 4,                 //tab空格数
        mode: "text/x-c++src",      //c/c++语言代码高亮
        lineNumbers: true,          //显示行号
        line:true,
        theme: "base16-light",           //主题
        matchBrackets: true,        //括号匹配
      },
      //用户提交的代码
      sendInfo: {
        id:"",
        code: "",
        language: "C++",
      },
      language_choose: "C++",
    }
  },
  /**
   * 页面退出后自动销毁
   */
  // destroyed:function() {
  //   clearTimeout(this.timeoutObj);
  //   this.timeoutObj = '';
  //   console.log("销毁");
  // },
  /**
   * 页面渲染完成后执行该函数,该函数从sessionStorage中获取需要的题目
   */
  mounted:function(){
    console.log("向后端获取题目详情请求");
    this.problemDetail = JSON.parse(sessionStorage.getItem("problemID"));
    console.log(this.problemDetail);
    this.sendInfo.id = this.problemDetail.id;
  },
  methods: {
    /**
     * 设置codemirror的大小
     */
    codemirrorReady() {
      console.log("codemirror 设置成功");
      this.$refs.codeMirror.codemirror.setSize('100%', '400px')
    },
    /**
     * 重置代码
     */
    reset() {
      this.sendInfo.code = "";
      console.log("重置代码");
    },
    /**
     * 选择C语言
     */
    choose_language_C() {
      this.language_choose = "C"
      this.sendInfo.language = "C";
      console.log(this.sendInfo.language);
    },
    /**
     * 选择C++语言
     */
    choose_language_C_Plus() {
      this.language_choose = "C++";
      this.sendInfo.language = "C++";
      console.log(this.sendInfo.language);
    },
    /**
     * 返回上一页
     */
    back() {
      //返回上一页
      this.$router.go(-1);
    },
    /**
     * 从后端获取问题的解决情况
     */
    getResult() {
      console.log("向后端获取问题提交结果");
      this.$axios({
        method: "get",
        url: "/api/submission/",
        data: {submission_id:this.submission_id}
      }).then(response => {
        console.log("收到数据: "+response.data);
        this.status=this.showResult(response.data.result);
        this.dealStatus();
        if (response.data.result === 6 || response.data.result === 7) {
          console.log("还在判断中,请用户耐心等待,异步请求,2s后再请求一次数据");
          clearTimeout(this.timeoutObj);
          //2秒后继续访问结果
          this.status=this.showResult(response.data.result);
          this.dealStatus();
          this.timeoutObj = setTimeout(this.getResult, 2000);
        } else {
          this.loading = false;
          //显示结果(到时候想一个结果出来)
          //处理status
          this.status=this.showResult(response.data.result);
          this.dealStatus();
          //this.$message.info(this.showResult(response.data.result));
        }
      }).catch(error => {
        console.log("服务器发生了错误：【"+error+"】");
        this.$message.error("An error occurred on the server！Please try again...");
      });
    },
    /**
     * 处理结果，并返回相应结果
     * @param result
     * @returns {string}
     */
    showResult(result) {
      console.log("result: " + result);
      switch (result) {
        case -2:return "COMPILE_ERROR";
        case -1:return "WRONG_ANSWER";
        case 0:return "ACCEPTED";
        case 1:return "CPU_TIME_LIMIT_EXCEEDED";
        case 2:return "REAL_TIME_LIMIT_EXCEEDED";
        case 3:return "MEMORY_LIMIT_EXCEEDED";
        case 4:return "RUNTIME_ERROR";
        case 5:return "SYSTEM_ERROR ";
        case 6:return "PENDING";
        case 7:return "JUDGING";
        case 8:return "PARTIALLY_ACCEPTED";
        default:return "WAIT";
      }
    },
    /**
     * 提交代码
     */
    submitCode() {
      if (this.sendInfo.code === "") {
        alert("不能提交空数据");
        return;
      }
      //控制台打印提交的code
      console.log("你提交的代码如下：\n" + this.sendInfo, this.user_id);
      this.submissionData.code = this.sendInfo.code;
      this.submissionData.language = this.sendInfo.language;
      this.submissionData.problem = this.sendInfo.id;
      console.log(this.problemData);
      this.$message.info("正在检测中，请耐心等待");
      this.$axios({
        method: "post",
        url: "/api/submission/",
        data: this.submissionData
      }).then(response => {
        console.log(response.data.results);
        // if (response.data.code === 0) {
          //输出接收到的数据
          console.log(response.data);
          //以信息方式提示题目的Status
          this.$message.info(this.showResult(response.data.results));
          //setTimeout(this.getResult, 2000)
        // } else {
        //   this.$message.error("服务器出错");
        // }
      }).catch(error => {
        console.log(error);
      }).finally(final=>{
        console.log(final);
        //提交代码后转到状态页
        this.$router.push('/status');
      })
    }
  }
}
</script>

<style scoped>
span{
  font-size: larger;
  color: #2db7f5;
}
#main{
  margin: 10px;
  padding: 10px;
}
#main-card{
  margin: 0 50px;
  padding: 30px;
}
.main-row{
  margin: 20px 0;
}
#footer{
  margin: 10px;
  padding: 10px;
}
#footer-card{
  margin: 0 50px;
  padding: 30px;
}
.footer-row{
  margin: 20px 0;
}
</style>