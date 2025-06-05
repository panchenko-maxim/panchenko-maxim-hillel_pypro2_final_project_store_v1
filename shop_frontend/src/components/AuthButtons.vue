<template>
        <button v-if="!isAuthenticated" @click="goToLogin" class="btn btn-outline-light">Login</button>
        <button v-if="!isAuthenticated" @click="goToRegister" class="btn btn-outline-light">Register</button>
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