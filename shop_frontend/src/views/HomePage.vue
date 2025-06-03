<template>
<div>
    <h1>Store products</h1>
    <!-- <button v-if="!isAuthenticated" @click="logout">Logout</button> -->
    <LogoutButton />
    <ProductList />
    <UserCart />

</div>
</template>

<script>
import ProductList from '@/components/ProductList.vue'
import UserCart from '@/components/UserCart.vue';
import LogoutButton from '@/components/LogoutButton.vue';
// import axios from 'axios';

export default {
    // data () {
    //     return {
    //         isAuthenticated: false,
    //     }
    // },
    components: { ProductList, UserCart, LogoutButton},
    // methods: {
    //     async logout() {
    //         try {
    //             const refreshToken = localStorage.getItem('refresh_token');
    //             if (refreshToken) {
    //                 await axios.post('http://127.0.0.1:8000/api/logout/', {
    //                     refresh_token: refreshToken
    //                 });
    //             }
    //             localStorage.removeItem('access_token');
    //             localStorage.removeItem('refresh_token');
    //             this.isAuthenticated = false;
    //             this.$router.push('/login');
    //         } catch (error) {
    //             console.error("Logout failed:", error);
    //             localStorage.removeItem('access_token');
    //             localStorage.removeItem('refresh_token');
    //             this.isAuthenticated = false;
    //             this.$router.push('/login');
    //         }
    //     }
    // }
}

</script>

<style scoped>

</style>