<template>
    <div class="auth-buttons">
        <button v-if="!isAuthenticated" @click="goToLogin">Login</button>
        <button v-if="!isAuthenticated" @click="goToRegister">Register</button>
    </div>
</template>

<script>
import { useRouter } from 'vue-router';
export default {
    data(){
        return {
            isAuthenticated: false
        }
    },
    setup() {
        const router = useRouter();
        return {router};
    },
    methods: {
        checkAuthStatus() {
            this.isAuthenticated = !!localStorage.getItem('access_token')
        },
        goToLogin() {
            this.router.push('/login');
        },
        goToRegister() {
            this.router.push('/register');
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