<template>
<div>
    <h2>Cart</h2>
    <ul>
        <li v-for="item in cart.items" :key="item.product.id">
            {{ item.product.name }} - {{ item.quantity }} units
            <button @click="cart.remove(item.product.id)">Delete</button>
        </li>
    </ul>
    <button @click="submitOrder" :disabled="cart.items.length === 0">Make an order</button>
</div>    
</template>

<script>
import { inject } from 'vue';
import { axios } from 'axios';

</script>

<style>

</style>