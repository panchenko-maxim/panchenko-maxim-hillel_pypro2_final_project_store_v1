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

            const authToken = localStorage.getItem('access_token');
            if (!authToken) {
                alert('You need to be logged!')
                return;
            }
            
            try {
                await axios.post('http://localhost:8000/api/orders/', { 
                    items: items, 
                    comment: this.comment 
                }, {
                    headers: {
                        'Authorization': `Bearer ${authToken}`,
                    }
                })
                alert('Order placed')
                this.cart.clear()
                this.comment = ''
            } catch (error) {
                if (error.response && error.response.status === 401) {
                    alert('Authentication failed. Please log in again.');
                    
                } else {
                    alert('Error placing order. Please try again.');
                    console.error('Error details:', error.response ? error.response.data : error.message);
                }
            }
            
        }
    }
}

</script>

<style>

</style>