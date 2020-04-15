<template>
    <div id="hello">
        <h1>{{ mr }}</h1>
    </div>
</template>

<script>
export default {
    name:"hello",
    data() {
        return {
            mr:"宇宙无敌大坏蛋 - - ！"
        }
    },
}
</script>



<style>
#hello {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>