<template>
    <div class="cart">
        <h1>Your order</h1>
        <ul>
            <li v-for="item in cart.items" :key="item.product.id">{{ item }}</li>
        </ul>
        <br>
        <br>
        <ul>
            <li v-for="item in cart.items" :key="item.product.id">
                <div v-if="item && item.product">
                    <img v-if="item.product.image" :src="item.product.image" :alt="item.product.name">
                    <h5>Product name: "{{ item.product.name }}"</h5>
                    <p>Count: 
                        <button @click="cart.decrementQuantity(item.product.id)" 
                            :disabled="item.quantity <= 1">
                            -
                        </button>
                        <span>{{ item.quantity }}</span>
                        <button @click="cart.incrementQuantity(item.product.id)">+</button>
                    </p>
                    <button @click="cart.remove(item.product.id)">Delete</button>
                </div>
                <div v-else>
                    <h5>Product not available</h5>
                </div>
            </li>
        </ul>
    </div>
    <div class="filling_info">
        <h3>Filling the information for order</h3>
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

img {
    width: 10%;
}

li {
    list-style-type: none;
    margin-bottom: 3%;
    
}

.filling_info {
    margin-left: 5%;
}
</style>