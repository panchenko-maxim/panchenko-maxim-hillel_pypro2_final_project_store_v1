<template>
    <div class="cart">
        <h1>Cart</h1>
        <ul>
            <li v-for="item in cart.items" :key="item.product.id">{{ item }}</li>
        </ul>
        <br>
        <br>
        <ul>
            <li v-for="item in cart.items" :key="item.product.id">
                <div v-if="item && item.product">
                    <img v-if="item.product.image" :src="item.product.image" :alt="item.product.name">
                    <h5>{{ item.product.name }}</h5>
                </div>
                <div v-else>
                    <h5>Product not available</h5>
                </div>
                
                
            </li>
        </ul>
    </div>
    
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

<style scoped>
.cart {
    margin: 5%;
}

.cart h1 {
    text-align: center;
}
</style>