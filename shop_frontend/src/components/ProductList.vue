<template>
    <h2>List of products</h2>
<div class="container-fluid mt-4">
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 product-grid">
        <div class="col" v-for="product in products" :key="product.id">
            <div class="card h-100">
                <img v-if="product.image" :src="product.image" class="card-img-top" :alt="product.name">
                <div class="card-body">
                    <h3 class="card-title">{{ product.name }}</h3>
                    <p class="card-text">{{ product.description }}</p>
                    <p class="card-text"><strong>Price:</strong> {{ product.price }} coin.</p>
                    <button class="btn btn-primary" @click="addToCart(product)">Add to cart</button>
                </div>
            </div>
        </div>
        <!-- <ul>
            <li v-for="product in products" :key="product.id">
                <h3>{{ product.name }}</h3>
                <p>{{ product.description }}</p>
                <p>Price: {{ product.price }} coin.</p>
                <button @click="addToCart(product)">Add to cart</button>
            </li>
         </ul> -->
    </div>
    
</div>
</template>


<script>
import axios from 'axios';
import { inject } from 'vue';

export default {
    setup() {
        const cart = inject('cart')
        return { cart }
    },
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
            this.cart.add(product)
        },
    },
    mounted(){
        this.fetchProducts()
    }
}

</script>


<style scoped>
.product-grid {
    max-height: 80vh; /* Максимальная высота блока, чтобы появилась прокрутка */
    overflow-y: auto; /* Включаем вертикальную прокрутку */
    padding-right: 15px; /* Добавляем небольшой отступ справа, чтобы не было наложения на скроллбар */
}

/* Дополнительные стили для лучшего отображения */
.card {
    transition: transform 0.2s ease-in-out;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>