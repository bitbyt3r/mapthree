import Vue from 'vue'
import Vuex from 'vuex'
import VueMaterial from 'vue-material'
import VueRouter from 'vue-router'
import VueWamp from 'vue-wamp'
import App from './App.vue'
import Home from './Home.vue'
import Space from './Space.vue'

Vue.use(VueWamp, {
  debug: true,
  lazy_open: false,
  url: 'ws://photomaster.irc.umbc.edu:8888/ws',
  realm: 'realm1',
  onopen: function(session, details) {
    console.log('WAMP connected', session, details);
  },
  onclose: function(reason, details) {
    console.log('WAMP closed: ' + reason, details);
  }
});

Vue.use(VueMaterial);

Vue.use(VueRouter);

const routes = [{
    path: '/',
    component: Home
  },
  {
    path: '/space',
    component: Space
  }
];

const router = new VueRouter({
  routes
});

const store = new Vuex.Store();

window.vue = new Vue({
  router,
  store,
  el: '#app',
  render: h => h(App)
})
