import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from './Layout.vue'
import IndexPage from './pages/index.vue'
import mock from './mock/mock'

// console.log(mock)   打印

// 调用
Vue.use(VueRouter)
// 实例化 VueRouter    let 变量申明符
let router = new VueRouter({
  mode:'history',   // 记录路由   可以让页面 回退
  routes:[
    {
      path:'/',
      component:IndexPage    // 根路径页面
    }
  ]
})

new Vue({
  el: '#app', 
  router,
  components:{
    Layout
  },
  template:'<Layout/>'    // 对应Layout.vue里面所有的标签
})
