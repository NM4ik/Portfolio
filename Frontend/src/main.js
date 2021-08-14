import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import 'animate.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

library.add(fas, fab);

Vue.component('fa', FontAwesomeIcon);

Vue.config.productionTip = false;
Vue.component('public_layout', () => import('@/layouts/publicLayout/Index'));
Vue.component('main_layout', () => import('@/layouts/MainLayout/Index'));


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
