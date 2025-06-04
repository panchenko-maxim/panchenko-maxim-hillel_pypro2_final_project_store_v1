<template>
    <div>
        <p v-if="isAuthenticated">Username: {{ username }}</p>
        <p v-else>Noname</p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isAuthenticated: false,
            username: ''
        }
    },
    methods: {
        updateUserInfo() {
            this.username = localStorage.getItem('username') || '';
            this.isAuthenticated = !!localStorage.getItem('access_token');
        }
    },
    mounted() {
        this.updateUserInfo();
        window.addEventListener('storage', this.updateUserInfo);
    },
    beforeUnmount() {
        window.removeEventListener('storage', this.updateUserInfo);
    }
}

</script>

<style>

</style>