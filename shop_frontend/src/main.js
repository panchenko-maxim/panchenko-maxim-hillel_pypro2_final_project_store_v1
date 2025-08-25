import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import { cart } from './store/cart.js'

axios.defaults.withCredentials = true;

axios.interceptors.request.use(
    config => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config
    },
    error => Promise.reject(error)
);


axios.interceptors.response.use(
    response => response,
    async error => {
       const originalRequest = error.config;
       if (error.response.status == 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            const refreshToken = localStorage.getItem('refresh_token');
            try {
                const response = await axios.post('http://localhost:8000/api/token/refresh/', {refresh: refreshToken});
                localStorage.setItem('access_token', response.data.access);
                originalRequest.headers.Authorization = `Bearer ${response.data.access}`;
                return axios(originalRequest);
            } catch (err){
                router.push('/login');
                return Promise.reject(error);
            }
       
        }
        return Promise.reject(error);
    }
);

cart.loadCart().then(() => {
    createApp(App).use(router).mount('#app');
})

createApp(App).use(router).mount('#app')
