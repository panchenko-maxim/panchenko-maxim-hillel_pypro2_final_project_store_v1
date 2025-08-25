<template>
    <h2>List of {{ infoTitle() }}</h2>
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
    </div>
    
</div>
</template>


<script>
import axios from 'axios';
import { inject } from 'vue';

export default {
    props: {
        apiUrl: {
            type: String,
            required: true,
        }
    },
    setup() {
        const cart = inject('cart')
        return { cart }
    },
    data() {
        return {
            title: '',
            products: [],
            loading: false,
            error: null,
        }
    },
    watch: {
        apiUrl: {
            immediate: true,
            handler: 'fetchProducts',
        }
    },
    methods: {
        async fetchProducts() {
            this.loading = true;
            this.error = null;
            this.products = [];
            try {
                const response = await axios.get(this.apiUrl);
                this.products = response.data
            } catch(err) {
                console.error('Error while receiving products', err);
                this.error = 'Failed to load products. Please try again later.'
            } finally {
                this.loading = false;
            }
            
        },
        addToCart(product) {
            this.cart.add(product)
        },

        infoTitle() {
            const listUrl = this.apiUrl.split('/')
            if (listUrl[listUrl.length - 1] == ''){
                return 'products'
            } else {
                return listUrl[listUrl.length - 1].split('=')[1]
            }
            
        
            
        }
    },
    mounted(){
        this.fetchProducts()
    }
}

</script>


<style scoped>
.card-img-top {
    width: 100px;
    height: auto;
}

.product-grid {
    max-height: 80vh;
    overflow-y: auto;
    padding-right: 15px;
}

.card {
    transition: transform 0.2s ease-in-out;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>