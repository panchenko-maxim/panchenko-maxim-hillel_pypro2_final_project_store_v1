<template>
<div class="d-flex flex-column min-vh-100">
    <header class="bg-dark text-white text-center py-3">
        <h1>Store products</h1>
        <nav class="navbar navbar-expand navbar-light bg-primary">
            <div class="dropdown me-3">
                <button class="btn btn-outline-light dropdown-toggle"
                type="button"
                id="dropdownMenuButton"
                data-bs-toggle="dropdown"
                aria-expanded="false">
                    Menu
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li>
                        <a class="dropdown-item" href="#">Page 1</a>
                    </li>
                    <li>
                        <h6 class="dropdown-header">Categories</h6>
                        <ul class="list-unstyled ms-3">
                            <li><a class="dropdown-item" href="#">Shoes</a></li>
                            <li><a class="dropdown-item" href="#">Clothes</a></li>
                        </ul>
                    </li>
                    <li>
                        <a class="dropdown-item" href="#">About us</a>
                    </li>
                </ul>
            </div>

            <form class="d-flex me-3" role="search">
                <input
                    class="form-control me-2" 
                    type="search"
                    placeholder="Search"
                    aria-label="Search">
                <button class="btn btn-outline-light" type="submit">></button>
            </form>

            <div class="conteiner-fluid">
                <UsernameInfo />
            </div>

            <LogoutButton />
            <AuthButtons />

        </nav>


        <!-- <UsernameInfo /> -->
        <!-- <AuthButtons /> -->
        <!-- <LogoutButton /> -->
    </header>

    <main>
        <ProductList />
        <UserCart />
    </main>

    <footer class="bg-dark text-white text-center py-3 mt-auto">
        <p>Footer</p>
    </footer>
    
    

</div>
</template>

<script>
import ProductList from '@/components/ProductList.vue'
import UserCart from '@/components/UserCart.vue';
import LogoutButton from '@/components/LogoutButton.vue';
import AuthButtons from '@/components/AuthButtons.vue';
import UsernameInfo from '@/components/UsernameInfo.vue';

export default {
    components: { ProductList, UserCart, LogoutButton, AuthButtons, UsernameInfo},
}

</script>

<style scoped>
.dropdown-menu .list-unstyled .dropdown-item {
    display: block;
    padding: 0.25rem 1rem;
}

</style>