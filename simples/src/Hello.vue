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
            mr:"王国芳我爱你，一生一世 - - ！"
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