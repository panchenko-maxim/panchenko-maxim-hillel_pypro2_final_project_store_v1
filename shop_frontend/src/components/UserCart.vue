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
import  axios  from 'axios';

export default {
    setup() {
        const cart = inject('cart')
        return { cart }
    },
    methods: {
        async submitOrder(){
            const items = this.cart.items.map(item => ({
                product: item.product.id,
                quantity: item.quantity
            }))
            
            try {
                await axios.post('http://localhost:8000/api/orders/', { items })
                alert('Order placed')
                this.cart.clear()
            } catch (error) {
                alert('Error order placed')
                console.error(error)
            }
            
        }
    }
}

</script>

<style>

</style>