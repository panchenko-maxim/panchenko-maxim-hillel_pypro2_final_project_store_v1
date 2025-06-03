<template>
    <button v-if="isAuthenticated" @click="logout">Logout</button>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    data() {
        return {
            isAuthenticated: false
        }
    },
    setup() {
        const router = useRouter();
        return { router };
    },
    methods: {
        checkAuthStatus() {
            this.isAuthenticated = !!localStorage.getItem('access_token');
        },
        async logout() {
            try {
                const refreshToken = localStorage.getItem('refresh_token');
                if (refreshToken) {
                    await axios.post('http://127.0.0.1:8000/api/logout/', { refresh_token: refreshToken });
                }
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                this.isAuthenticated = false;

                this.router.push('/login');
            } catch (error) {
                console.error('Logout failed (likely due to token invalidation or network issue):', error);
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                this.isAuthenticated = false;

                this.router.push('/login');
            }
        }
    },
    mounted() {
        this.checkAuthStatus();
        window.addEventListener('storage', this.checkAuthStatus);
    },
    beforeUnmount() {
        window.removeEventListener('storage', this.checkAuthStatus);
    }
}

</script>

<style>

</style>