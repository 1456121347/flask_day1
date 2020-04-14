import Vue from "vue/dist/vue.js"
import VueMathPlugin from "./VueMathPlugin.js"
import Vuex from "vuex"  //插件
    
Vue.use(VueMathPlugin)
// 调用vuex
Vue.use(Vuex)
var store = new Vuex.Store({
    state:{message:"你好啊"},
    mutations:{},
    actions:{},
    gerrers:{},
})
new Vue({
    el:"#app",
    data:{
        item:20
    },
    store:store
})