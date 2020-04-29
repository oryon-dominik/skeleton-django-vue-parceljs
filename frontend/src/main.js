import Vue from 'vue';
import App from './App.vue';

import Vuetify from './plugins/vuetify.js'

new Vue({
  vuetify: Vuetify,
  render: createElement => createElement(App) 
}).$mount('#app');
