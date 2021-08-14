export default [
  {
    path: '/',
    name: 'home',
    meta: { layout: 'public_layout' },
    component: () => import('@/views/Home.vue'),
  },
  {
    path: '/about',
    name: 'About',
    meta: {layout: 'main_layout'},
    component: () => import('@/views/About.vue'),
  },
  {
    path: '/projects',
    name: 'projects',
    meta: { layout: 'main_layout' },
    component: () => import('@/views/Projects.vue'),
  },
];