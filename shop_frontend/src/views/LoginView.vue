<template>
    <div class="auth-container">
        <h2>Login</h2>
        <form @submit.prevent="login" class="auth-form">
            <input v-model="credentials.username" placeholder="Username" required />
            <input v-model="credentials.password" type="password" placeholder="Password" required />
            <button type="submit">Login</button>
        </form>
        <p>Not registered? <router-link to="/register">Register</router-link></p>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            credentials: {username: '', password: ''}
        };
    },
    methods:
    {
        async login() {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/token/', this.credentials)
                localStorage.setItem('access_token', response.data.access)
                localStorage.setItem('refresh_token', response.data.refresh)
                this.$router.push('/')
            } catch (error) {
                alert('Login failed')
            }
        }
    }
};
</script>

<style scoped></style>