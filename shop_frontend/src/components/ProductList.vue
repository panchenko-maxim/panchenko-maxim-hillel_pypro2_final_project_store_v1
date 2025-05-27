<template>
<div>
    <h2>List of products</h2>
    <ul>
        <li v-for="product in products" :key="product.id">
            <h3>{{ product.name }}</h3>
            <p>{{ product.description }}</p>
            <p>Price: {{ product.price }} coin.</p>
            <button @click="addToCart(product)">Add to cart</button>
        </li>
    </ul>
</div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            products: [],
        }
    },
    methods: {
        async fetchProducts() {
            const response = await axios.get('http://localhost:8000/api/products/')
            this.products = response.data
        },
        addToCart(product) {
            alert(`Product "${product.name}" added to cart`)
        },
    },
    mounted(){
        this.fetchProducts()
    }
}

</script>


<style scoped>

</style>