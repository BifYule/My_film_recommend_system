// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'

import semantic from '../node_modules/semantic-ui-css/semantic.min.js'
// 引入css文件
import '../node_modules/semantic-ui-css/semantic.min.css'

Vue.use(semantic);
Vue.use(ElementUI)
Vue.use(VueResource)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  data(){
    return{
      movie_name:null,
      user_name:null,
    }
  },
  template: '<App/>'
})
