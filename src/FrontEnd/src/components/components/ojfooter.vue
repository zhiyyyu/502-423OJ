<template>
  <div id="footer">
    {{msg}}
  </div>
</template>

<script>
export default {
  name: "oj-footer",
  data(){
    return{
      msg:"@502-423OJ"
    }
  },
  created() {
    console.log("footer准备完毕");
  }
}
</script>

<style scoped>
#footer{
  text-align: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: small;
  color: black;
  height: 50px;
}
</style>