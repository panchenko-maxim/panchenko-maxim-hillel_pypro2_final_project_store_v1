<template>
<ProductList apiUrl="http://localhost:8000/api/products/"/>
</template>

<script>
import ProductList from '@/components/ProductList.vue'
export default {
    components: { ProductList },
}

</script>

<style scoped>


</style>