<template>
    <div>
        <h1>Register</h1>
        <form @submit.prevent="register">
            <input v-model="credentials.username" placeholder="Username" required>
            <input v-model="credentials.password" type="password" placeholder="Password" required>
            <button type="submit">Register</button>
        </form>
    </div>

</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            credentials: {username: '', password: ''}
        };
    },
    methods: {
        async register() {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/auth/register/', this.credentials)
                localStorage.setItem('access_token', response.data.access_token)
                localStorage.setItem('refresh_token', response.data.refresh_token)
                localStorage.setItem('username', this.credentials.username)
                this.$router.push('/')
            } catch (error) {
                if (error.response && error.response.data) {
                    alert('Register failed' + JSON.stringify(error.response.data));
                } else {
                    alert('Register failed' + error.message);
                }
            }
        }
    }
}

</script>


<style>

</style>