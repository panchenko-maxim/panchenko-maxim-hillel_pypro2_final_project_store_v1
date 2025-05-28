import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage,
        meta: { requiresAuth: true }
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access_token');
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  } else {
    next()
  }
})

export default router