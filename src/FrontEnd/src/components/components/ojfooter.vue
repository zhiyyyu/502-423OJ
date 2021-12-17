<template>
  <el-card id="footer" >
    {{msg}}
  </el-card>
</template>

<script>
export default {
  name: "oj-footer",
  data(){
    return{
      msg:"producer:yjl email:xxx@xxx.com"
    }
  }
}
</script>

<style scoped>
#footer{
  text-align: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: small;
  color: black;
  vertical-align: center;
  height: 50px;
}
</style>