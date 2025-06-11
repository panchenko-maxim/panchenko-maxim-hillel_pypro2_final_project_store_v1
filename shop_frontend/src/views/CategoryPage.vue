<template>
<ProductList :apiUrl="categoryApiUrl" />

</template>

<script>
import ProductList from '@/components/ProductList.vue';

export default {
    data() {
        return {
            link: 'hello'
        }
    },
    components: { ProductList, },
    props: {
        categoryName: {
            type: String,
            default: null,
        }
    },
    computed: {
        categoryApiUrl() {
            if (this.categoryName) {
                return `http://127.0.0.1:8000/api/products/?category_name=${this.categoryName}`;
                
            } else {
                return 'http://localhost:8000/api/products/';
                
            }
        }
    }
}

</script>

<style>

</style>