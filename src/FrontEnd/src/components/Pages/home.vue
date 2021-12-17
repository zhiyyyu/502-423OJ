<template>
  <el-card id="content">
    {{msg}}
  </el-card>
</template>
<script>

export default {
  name: "home",
  components:{
  },
  data:function () {
    return{
      msg:"Welcome to 502-423OJ"
    }
  }
}
</script>

<style scoped>
#content{
  padding-top: 100px;
  margin-top: 20px;
  text-align: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: xxx-large;
  color: black;
  vertical-align: center;
  height: 400px;
}

</style>