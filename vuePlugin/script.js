import Vue from 'vue/dist/vue.js'
import VueMathPlugin from './VueMathPlugin.js'
import Vuex from 'Vuex'
Vue.use(VueMathPlugin)   // 调用
Vue.use(Vuex)    // 调用

var store = new Vuex.Store({
    state:{message:'Hello!'},
    mutations:{

    },
    actions:{},
    getters:{},
})
new Vue({
    el:'#app',
    data:{
        item:50
    },
    store:store
})