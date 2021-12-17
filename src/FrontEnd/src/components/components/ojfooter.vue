<template>
  <div id="app">
    {{msg}}
  </div>
</template>

<script>
export default {
  name: "Footer",
  data(){
    return{
      msg:"@502-423OJ"
    }
  }
}
</script>

<style scoped>
#app{
  padding-top: 15px;
  text-align: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: small;
  color: black;
  vertical-align: center;
  background-color: whitesmoke;
  height: 50px;
}
</style>