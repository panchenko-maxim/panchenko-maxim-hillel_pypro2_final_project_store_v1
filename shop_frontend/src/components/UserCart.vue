<template>
<div class="cart-icon-container">
    <a @click="toggleCartOverlay" class="cart-icon">
        <svg xmlns="http://www.w3.org/2000/svg" 
        width="25" height="25" fill="currentColor" 
        class="bi bi-cart" 
        viewBox="0 0 16 16">
        <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5M3.102 4l1.313 7h8.17l1.313-7zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4m7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4m-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2m7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2"/>
    </svg>
    </a>
    <span v-if="totalCartItems > 0" class="item-count">{{ totalCartItems }}</span>
    {{ console.log(cart.items) }}
</div>

<div v-if="showCartOverlay" class="cart-overlay">
    <div class="cart-overlay-content">
        <button @click="toggleCartOverlay" class="close-button">X</button>
        <h2>Cart</h2>
        <ul v-if="cart.items.length > 0"> 
            <li v-for="item in cart.items" :key="item.product.id">
                <span>{{ item.product.name }}</span>
                <button @click="cart.decrementQuantity(item.product.id)" 
                    :disabled="item.quantity <= 1">-</button>
                <span>{{ item.quantity }}</span>
                <button @click="cart.incrementQuantity(item.product.id)">+</button>
                
                <button @click="cart.remove(item.product.id)">Delete</button>
            </li>
        </ul>
        <!-- <textarea v-model="comment" placeholder="Comment for your order (optional)"></textarea> -->
        <button @click="goToCheckout" :disabled="cart.items.length === 0" class="checkout-button">Make an order</button>
    </div>
</div>
</template>

<script>
import { inject, ref } from 'vue';
import  axios  from 'axios';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const cart = inject('cart');
        const comment = ref('');
        const showCartOverlay = ref(false);
        const router = useRouter();

        const toggleCartOverlay = () => {
                showCartOverlay.value = !showCartOverlay.value;
            };

        const goToCheckout = () => {
            toggleCartOverlay();
            router.push('/checkout');
        };

        return { cart, comment, showCartOverlay, toggleCartOverlay, goToCheckout }
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

    },
    computed: {
        totalCartItems() {
            if (!this.cart || !this.cart.items || this.cart.items.length === 0) {
                return 0;
            }
            return this.cart.items.reduce((sum, item) => sum + item.quantity, 0);
        }
    }
}

</script>

<style>
.cart-icon-container {
    position: relative;
    display: inline-block;
    cursor: pointer;
}

.cart-icon {
    color: #fff;
}

.item-count {
    position: absolute;
    background-color: red;
    color: white;
    border-radius: 50%;
    padding: 2px 6px;
    font-size: 0.7em;
    font-weight: bold;
    min-width: 18px;
    text-align: center;
}

.cart-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 5000;
}

.cart-overlay-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    width: 90%; /* Ширина всплывающего окна */
    max-width: 500px; /* Максимальная ширина */
    position: relative; /* Для позиционирования кнопки закрытия */
    max-height: 80vh; /* Чтобы окно не было слишком высоким на маленьких экранах */
    overflow-y: auto; /* Добавляем скролл, если содержимое не помещается */
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 1.2em;
  cursor: pointer;
  padding: 5px;
}

.cart-overlay-content ul {
  list-style: none;
  padding: 0;
  margin: 15px 0;
}

.cart-overlay-content li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #333;
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.cart-overlay-content li:last-child {
  border-bottom: none;
}

.cart-overlay-content textarea {
  width: 100%;
  margin-top: 15px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  min-height: 60px;
}

.cart-overlay-content button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 15px;
  /* width: 100%; */
}

.cart-overlay-content button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.cart-overlay-content .checkout-button { 
    width: 100%; 
}

/* Стили для кнопок "Delete" (меньшего размера) */
.cart-overlay-content li button { /* Более специфичное правило для кнопок внутри <li> */
    padding: 5px 10px; /* Меньший padding */
    font-size: 0.9em; /* Чуть меньший шрифт */
    background-color: #dc3545; /* Красный цвет для удаления */
    margin-top: 0; /* Уберем верхний отступ, чтобы они были по центру с текстом */
    width: auto; /* Пусть ширина будет по содержимому */
}

.cart-overlay-content textarea {
    width: 90%; /* Например, 90% */
    max-width: 400px; /* Или установите максимальную ширину */
    /* ... остальные стили ... */
}




</style>