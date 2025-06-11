<template>
    <h1>Cart</h1>
    <ul>
        <li v-for="item in cart.items" :key="item.product.id">{{ item }}</li>
    </ul>
    <br>
    <ul>
        <li v-for="item in cart.items" :key="item.product.id">{{ item.name }}</li>
    </ul>
</template>

<script>
import { inject } from 'vue';

export default{
    setup() {
        const cart = inject('cart');

        return { cart, }
    }
    
}


</script>

<style>

</style>