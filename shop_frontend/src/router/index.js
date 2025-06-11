import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import AboutUs from '@/views/AboutUs.vue';
import CheckoutPage from '@/views/CheckoutPage.vue'
import CategoryPage from '@/views/CategoryPage.vue';
import BaseLayout from '@/components/Base.vue'
// import { compile } from 'vue';

const routes = [
    {
        path: '/',
        component: BaseLayout,
        children: [
            {
                path: '',
                name: 'HomePage',
                component: HomePage,
                meta: { requiresAuth: false }
            },
            {
                path: 'about-us',
                name: 'AboutUs',
                component: AboutUs,
                meta: { requiresAuth: false }
            },
            {
                path: '/category/:categoryName',
                name: 'CategoryProducts',
                component: CategoryPage,
                props: true,
            },
            {
                path: 'checkout',
                name: 'Checkout',
                component: CheckoutPage,
            },
        ]
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
    },
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