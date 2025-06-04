<template>
<div>
    <h1>Store products</h1>
    <UsernameInfo />
    <AuthButtons />
    <LogoutButton />
    <ProductList />
    <UserCart />

</div>
</template>

<script>
import ProductList from '@/components/ProductList.vue'
import UserCart from '@/components/UserCart.vue';
import LogoutButton from '@/components/LogoutButton.vue';
import AuthButtons from '@/components/AuthButtons.vue';
import UsernameInfo from '@/components/UsernameInfo.vue';

export default {
    components: { ProductList, UserCart, LogoutButton, AuthButtons, UsernameInfo},
}

</script>

<style scoped>

</style>