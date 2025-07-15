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
                    <img v-if="item.product.image" :src="getFullImageUrl(item.product.image)" :alt="item.product.name">
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
                    <p>Price per item: {{ item.product.price }}</p>
                    <p>Subtotal: {{ item.product.price * item.quantity }}</p>
                </div>
                <div v-else>
                    <h5>Product not available</h5>
                </div>
            </li>
        </ul>

        <div class="cart-summary">
            <h3>Total items: {{ cart.totalItems }}</h3>
            <h3>Total cost: {{ cart.totalCost }}</h3>
        </div>

    </div>
    <div class="filling_info">

        <h3>Filling the information for order</h3>
        <form @submit.prevent="placeOrder" class="order-form">

            <div class="form-group">
                <label for="full_name">Full Name:</label>
                <input type="text" id="full_name" v-model="formData.full_name" required>
                <span v-if="errors.full_name" class="error-message">{{ errors.full_name }}</span>
            </div>

            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" v-model="formData.email" required>
                <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
            </div>

            <div class="form-group">
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" v-model="formData.phone" required>
                <span v-if="errors.phone" class="error-message">{{ errors.phone }}</span>
            </div>

            <div class="form-group">
                <label for="address">Delivery Address:</label>
                <textarea id="address" v-model="formData.address" rows="3" required></textarea>
                <span v-if="errors.address" class="error-message">{{ errors.address }}</span>
            </div>

            <button type="submit" :disabled="isPlacingOrder || cart.totalItems === 0" class="place-order-button">
                {{ isPlacingOrder ? 'Placing Order ...' : 'Place Order' }}
            </button>

            <p v-if="orderSuccess" class="success-massage">Your order has been placed successfully!</p>
            <p v-if="orderError" class="error-message">Error placing order: {{ orderError }}</p>

        </form>

    </div>
    
</template>

<script>
import { inject, ref, reactive } from 'vue';
import axios from 'axios';

export default{
    setup() {
        const cart = inject('cart');

        const API_BASE_URL = 'http://127.0.0.1:8000';
        const ORDER_API_ENDPOINT = `${API_BASE_URL}/api/orders/`

        const formData = reactive({
            full_name: '',
            email: '',
            phone: '',
            address: '',
        });

        const errors = reactive({});
        const isPlacingOrder = ref(false);
        const orderSuccess = ref(false);
        const orderError = ref(null); 

        const getFullImageUrl = (relativePath) => {
            if (!relativePath) return '';
            return `${API_BASE_URL}${relativePath.startsWith('/') ? '' : '/'}${relativePath}`;
        }

        const validateForm = () => {
            Object.keys(errors).forEach(key => delete errors[key]);
            let isValid = true

            if (!formData.full_name.trim()){
                errors.full_name = 'Full Name is required.';
                isValid = false;
            }

            if (!formData.email.trim()) {
                errors.email = 'Email is required.';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
                errors.email = 'Invalid email format.';
                isValid = false;
            }

            if (!formData.phone.trim()) {
                errors.phone = 'Phone number is required.';
                isValid = false;
            }

            if (!formData.address.trim()) {
                errors.address = 'Delivery Address is required.';
                isValid = false;
            }

            if (cart.totalItems === 0) {
                orderError.value = 'Your cart is empty. Please add products before placing an order.';
                isValid = false;
            }

            return isValid;

        }

        const placeOrder = async() => {
            orderSuccess.value = false;
            orderError.value = null;

            if (!validateForm()) {
                console.log("Form validation failed:", errors);
                return;
            }

            isPlacingOrder.value = true;

            const orderPayload = {
                customer_name: formData.full_name,
                customer_email: formData.email,
                customer_phone: formData.phone,
                delivery_address: formData.address,
                items: cart.items.map(item => ({
                    product: item.product.id,
                    quantity: item.quantity,
                    price_at_order: item.product.price
                })),
                total_cost: cart.totalCost,
            };

            try {
                const response = await axios.post(ORDER_API_ENDPOINT, orderPayload);
                console.log('Order placed successfully:', response.data);
                orderSuccess.value = true;

                cart.clear()

                formData.full_name = '';
                formData.email = '';
                formData.phone = '';
                formData.address = '';
            } catch (err) {
                console.error('Error placing order:', err);
                if (err.response && err.response.data) {
                    orderError.value = err.response.data.detail || JSON.stringify(err.response.data);
                } else {
                    orderError.value = 'An unexpected error occurred. Please try again.';
                }
            } finally {
                isPlacingOrder.value = false;
            }
        };

        return { cart, getFullImageUrl, formData, errors, isPlacingOrder, orderSuccess, orderError, placeOrder};
    }
    
}


</script>

<style scoped>
.cart {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border-bottom: 1px solid #eee;
  padding: 15px 0;
  margin-bottom: 15px;
}

li:last-child {
  border-bottom: none;
  margin-bottom: 0;
}

li div {
  display: flex;
  flex-direction: column;
  width: 100%;
}

img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  margin-right: 15px;
  border-radius: 4px;
  align-self: center;
  margin-bottom: 10px;
}

h5 {
  margin: 0 0 5px 0;
  color: #555;
  font-size: 1.1em;
}

p {
  margin: 5px 0;
  color: #666;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s ease;
  margin-right: 5px;
}

button:hover:not(:disabled) {
  background-color: #0056b3;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.cart-summary {
  text-align: right;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 2px dashed #ccc;
}

.cart-summary h3 {
  color: #333;
  margin: 5px 0;
}

/* Стили для новой секции формы */
.filling_info {
  margin-top: 40px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.filling_info h3 {
  text-align: center;
  color: #333;
  margin-bottom: 25px;
}

.order-form .form-group {
  margin-bottom: 15px;
  text-align: left;
}

.order-form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

.order-form input[type="text"],
.order-form input[type="email"],
.order-form input[type="tel"],
.order-form textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box; /* Учитывает padding и border в общей ширине */
  font-size: 1em;
  transition: border-color 0.2s ease;
}

.order-form input[type="text"]:focus,
.order-form input[type="email"]:focus,
.order-form input[type="tel"]:focus,
.order-form textarea:focus {
  border-color: #007bff;
  outline: none;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}

.order-form textarea {
  resize: vertical; /* Разрешить вертикальное изменение размера */
}

.place-order-button {
  width: 100%;
  padding: 12px 20px;
  background-color: #28a745;
  color: white;
  font-size: 1.2em;
  border-radius: 5px;
  margin-top: 20px;
}

.place-order-button:hover:not(:disabled) {
  background-color: #218838;
}

.error-message {
  color: #dc3545;
  font-size: 0.9em;
  margin-top: 5px;
  display: block;
}

.success-message {
  color: #28a745;
  font-size: 1.1em;
  text-align: center;
  margin-top: 20px;
  padding: 10px;
  background-color: #d4edda;
  border: 1px solid #28a745;
  border-radius: 5px;
}
</style>