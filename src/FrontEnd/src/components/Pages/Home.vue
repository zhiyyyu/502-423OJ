<template>
  <div id="content">
    {{msg}}
  </div>

</template>

<script>


export default {
  name: "Home",
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
  background-color: whitesmoke;
}

</style>