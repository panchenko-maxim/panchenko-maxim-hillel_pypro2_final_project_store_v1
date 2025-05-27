<template>
<div>
    <h1>Store products</h1>
    <ProductList />
    <UserCart />

</div>
</template>

<script>
import ProductList from '@/components/ProductList.vue'
import UserCart from '@/components/UserCart.vue';

export default {
    components: { ProductList, UserCart }
}

</script>

<style scoped>

</style>