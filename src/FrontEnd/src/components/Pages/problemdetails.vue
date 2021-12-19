<template>
  <el-container >
    <!--标题-->
    <el-header id="header" type="text" style="text-align: center" >
      <strong style="font-size: xxx-large">{{ problemData.title }}</strong>
    </el-header>
    <!--主界面-->
    <el-main id="main">
      <el-card id="main-card">
        <!--每行水平排列-->
        <el-row class="main-row">
          <span>Description：</span><br />
          <markdown-it-vue class="md-body" :content="problemData.body"></markdown-it-vue>
        </el-row>
        <el-row class="main-row">
          <span>Author：</span><br />
          <markdown-it-vue class="md-body" :content="problemData.author.username"></markdown-it-vue>
        </el-row>
        <!--暂时没有输入输出描述
        <el-row class="main-row">
          <span>Input：</span><br />
          <markdown-it-vue class="md-body" :content="problemData.problem.input_description"></markdown-it-vue>
        </el-row>
        <el-row class="main-row">
          <span>Output：</span><br />
          <markdown-it-vue class="md-body" :content="problemData.problem.output_description"></markdown-it-vue>
        </el-row>
        -->
        <el-row class="main-row">
          <span>Difficulty：</span><br />
          {{ problemData.difficulty }}
        </el-row>
        <el-row class="main-row">
          <span>Memory-Limit：</span><br />
          {{ problemData.memory_limit }}
        </el-row>
        <el-row class="main-row">
          <span>Time-Limit：</span><br />
          {{ problemData.time_limit }}
        </el-row>
      </el-card>
    </el-main>

    <!--页脚-->
    <el-footer id="footer">
      <el-card id="footer-card">
        <el-row class="footer-row">
          <!--重置代码按钮-->
          <el-button type="primary" round @click="reset" size="mini">
            reset
          </el-button>
          <!--语言选择下拉按钮-->
          <el-dropdown>
            <el-button type="primary" round size="mini">
              Language
              <i class="el-icon-arrow-down"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="choose_language_C">C</el-dropdown-item>
              <el-dropdown-item @click.native="choose_language_C_Plus">C++</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <!--目前的所选择的语言-->
          <span>Language: {{ language_choose }}</span>
          <divider></divider>
        </el-row >

        <el-row class="footer-row">
          <el-card>
            <codemirror v-model="sendInfo.code"
                        :options="cmdOptions"
                        @ready="codemirrorReady"
                        ref="codeMirror">
            </codemirror>
          </el-card>
        </el-row>
        <!--提交、返回按钮-->
        <el-row class="footer-row" style="text-align: center">
          <el-button icon="el-icon-check" type="primary" round @click="submitCode">Submit</el-button>
          <el-button type="primary" round @click="back">Back</el-button>
        </el-row>
      </el-card>
    </el-footer>
  </el-container>

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
      //问题的数据结构
      problemData: {
        ac_number:1,
        author:{
          data_joined:"time",
          id:1,
          last_join:"time",
          username:"张三"
        },
        body:"hello world",
        created:"time",
        difficulty: "Easy",
        id: 1,
        memory_limit: 1000,
        submission_number: 1,
        tags: ["g"],
        time_limit: 1000,
        title:"hello world",
        url:"http://locahost:8000/api/problemlist/1/",
      },
      //提交的数据结构
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
        problem:0,
        result:1,
        static_info:{
          id:1,
          space:0,
          time:200
        },
        user_id:0,
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
      sendInfo: {
        id:"",
        code: "",
        language: "C++",
      },
      language_choose: "C++",
      // submission_problem_id:"",
      // loading:false,
      // counter:0,
      // timeoutObj:"",
      // editable: "",
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
    console.log("mounted");
    this.problemData = JSON.parse(sessionStorage.getItem("problemID"));
    console.log(this.problemData);
    this.sendInfo.id = this.problemData.id;
    console.log("详情页面获取本地" + this.problemData);
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
    // getResult() {
    //   this.$axios({
    //     method: "get",
    //     url: "/api/submission/",
    //     data: {
    //       submission_id: this.submission_problem_id
    //     }
    //   }).then(response => {
    //         console.log(response.data);
    //         if (response.data.code === 0) {
    //           if (response.data.result === 6 || response.data.result === 7) {
    //             clearTimeout(this.timeoutObj);
    //             this.timeoutObj = setTimeout(this.getResult, 2000);
    //           } else {
    //             this.loading = false;
    //             //显示结果
    //             this.$message.info(this.showResult(response.data.result));
    //           }
    //         } else {
    //           this.$message.error("服务器错误");
    //         }
    //       }
    //   ).catch(error => {
    //     console.log(error.data);
    //   });
    // },
    /**
     * 处理结果，并返回相应结果
     * @param result
     * @returns {string}
     */
    showResult(result) {
      console.log("result: " + result);

      switch (result) {
        case 1:
          return "PENDING";
        case 2:
          return "JUDGING";
        case 3:
          return "AC";
        case 4:
          return "WA";
        case 5:
          return "RE";
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