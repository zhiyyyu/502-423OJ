<template>
  <div id="app">
    <el-container>
      <el-header>
        <ojnavigation></ojnavigation>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
      <el-footer>
        <ojfooter></ojfooter>
      </el-footer>
    </el-container>

  </div>
</template>

<script>
import ojnavigation from "@/components/components/ojnavigation";
import ojfooter from "@/components/components/ojfooter";
export default {
  /*
  <!--路由连接时的内容界面-->
    <router-view v-if="!$route.meta.keepAlive"></router-view>
   */
  name: 'App',
  components: {
    ojnavigation,
    ojfooter,
  },
  data(){
    return{

    }
  },
  methods:{

  }
}
</script>

<style scoped>
body{
  background-color: whitesmoke;
}


</style>
