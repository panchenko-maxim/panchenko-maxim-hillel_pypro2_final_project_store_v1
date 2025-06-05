<template>
    <!-- <div>
        <p v-if="isAuthenticated">Username: {{ username }}</p>
        <p v-else>Noname</p>
    </div> -->
    <div class="navbar-text me-3">
        <span v-if="isAuthenticated">Username: {{ username }}</span>
    <span v-else>Noname</span>
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