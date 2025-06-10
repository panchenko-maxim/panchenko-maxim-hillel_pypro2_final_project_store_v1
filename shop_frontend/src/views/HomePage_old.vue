<template>
<div class="d-flex flex-column min-vh-100">
    <header class="bg-dark text-white text-center pt-3 d-flex flex-column">
        <h1>Store products</h1>
        <nav class="navbar navbar-expand navbar-light bg-primary pb-1 pt-1">
        <div class="container-fluid">
            <div class="dropdown me-3">
                <button class="btn btn-outline-light dropdown-toggle menu-button"
                type="button"
                id="dropdownMenuButton"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                data-bs-auto-close="outside">
                    Menu
                </button>
                <ul class="dropdown-menu menu-button" aria-labelledby="dropdownMenuButton">
                    <li>
                        <a class="dropdown-item" href="#">Page 1</a>
                    </li>
                    <li class="dropend"> <a class="dropdown-item dropdown-toggle" href="#"
                        id="categoriesDropdown" role="button"
                        data-bs-toggle="dropdown"
                        aria-expanded="false">
                            Categories
                        </a>
                        <ul class="dropdown-menu menu-button" aria-labelledby="categoriesDropdown"> <li><a class="dropdown-item" href="#">Shoes</a></li>
                            <li><a class="dropdown-item" href="#">Clothes</a></li>
                        </ul>
                    </li>
                    <li>
                        <router-link to="/about-us" class="dropdown-item">About us</router-link>
                    </li>
                </ul>
            </div>

            <UserCart />
        
            <div class="d-flex ms-auto">

                <form class="d-flex me-3" role="search">
                <div class="input-group">
                    <input
                    class="form-control" 
                    type="search"
                    placeholder="Search"
                    aria-label="Search">
                    <button class="btn btn-outline-light search-button" type="submit"><i class="fas fa-search"></i></button>                
                </div>
            </form>

            
            <UsernameInfo />
            

            <LogoutButton />
            <AuthButtons />

            </div>
            
            </div>
        </nav>


        <!-- <UsernameInfo /> -->
        <!-- <AuthButtons /> -->
        <!-- <LogoutButton /> -->
    </header>

    <main>
        <ProductList />
        
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
/* .dropdown-menu .list-unstyled .dropdown-item {
    display: block;
    padding: 0.25rem 1rem;
} */
 .menu-button {
    width: 15em;
 }

.search-button {
    background-color: transparent;
    color: #fff;
    border-color: #dee2e6;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.search-button:hover {
    background-color: #6c757d;
    color: #fff;
}

.search-button:active {
    background-color: rgb(153, 180, 113);
}

</style>