<template>
  <el-card>
  <el-table :data="aboutTable">
    <el-table-column prop="time" label="time"></el-table-column>
    <el-table-column prop="msg" label="msg"></el-table-column>
  </el-table>
  </el-card>
</template>

<script>
export default {
  name: "about",
  data(){
    return{
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
  }
}
</script>
<style scoped>

</style>