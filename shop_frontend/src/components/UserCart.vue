<template>
<div>
    <h2>Cart</h2>
    <ul>
        <li v-for="item in cart.items" :key="item.product.id">
            {{ item.product.name }} - {{ item.quantity }} units
            <button @click="cart.remove(item.product.id)">Delete</button>
        </li>
    </ul>
    <textarea v-model="comment" placeholder="Comment for your order (optional)"></textarea>
    <button @click="submitOrder" :disabled="cart.items.length === 0">Make an order</button>
</div>    
</template>

<script>
import { inject, ref } from 'vue';
import  axios  from 'axios';

export default {
    setup() {
        const cart = inject('cart')
        const comment = ref('')
        return { cart, comment }
    },
    methods: {
        async submitOrder(){
            const items = this.cart.items.map(item => ({
                product_id: item.product.id,
                quantity: item.quantity
            }))
            
            try {
                await axios.post('http://localhost:8000/api/orders/', { items, comment: this.comment })
                alert('Order placed')
                this.cart.clear()
                this.comment = ''
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