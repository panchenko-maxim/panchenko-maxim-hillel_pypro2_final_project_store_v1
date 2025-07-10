import { reactive } from 'vue';
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const cart = reactive({
    items: [],

    async loadCart() {
        try {
            const response = await axios.get(`${API_BASE_URL}/cart/`);
            this.items = response.data.map(item => ({
                product: item.product,
                quantity: item.quantity
            })); 
        } catch (error) {
            console.log('Error loading cart:', error);
        }
    },

    async saveCartItem(productId, quantity) {
        try {
            if (quantity < 0) {
                await this.remove(productId);
            } else {
                const existing = this.items.find(i => i.product.id === productId);
                if (existing) {
                    await axios.put(`${API_BASE_URL}/cart/`, {product_id: productId, quantity: quantity});
                } else {
                    await axios.post(`${API_BASE_URL}/cart/`, {product_id: productId, quantity: quantity});
                }
            }
        } catch (error) {
            console.error('Error saving cart item:', error)
        }
    },

    async add(product) {
        const existing = this.items.find(i => i.product.id === product.id)
        if (existing) {
            existing.quantity += 1
            await this.saveCartItem(product.id, existing.quantity);
        } else {
            this.items.push({product, quantity: 1})
            await axios.post(`${API_BASE_URL}/cart/`, {product_id: product.id, quantity: 1})
        }
    },

    async remove(productId) {
        this.items = this.items.filter(i => i.product.id !== productId)
        try {
            await axios.delete(`${API_BASE_URL}/cart/${productId}/`);
        } catch (error) {
            console.error('Error removing item from cart:', error);
            await this.loadCart();
        }
    },

    async clear() {
        this.items = []
        try {
            await axios.delete(`${API_BASE_URL}/cart/`);
        } catch (error) {
            console.error('Error clearing cart:', error);
            await this.loadCart();
        }
    },

    async incrementQuantity(productId) {
        const item = this.items.find(i => i.product.id === productId)
        if (item) {
            item.quantity++;
            await this.saveCartItem(productId, item.quantity);
        }
    },

    async decrementQuantity(productId) {
        const itemIndex = this.items.findIndex(i => i.product.id === productId);
        if (itemIndex !== -1) {
            const item = this.items[itemIndex];
            if (item.quantity > 1) {
                item.quantity --;
                await this.saveCartItem(productId, item.quantity);
            } else {
                await this.remove(productId);
            }
        }
    }


    // add(product) {
    //     const existing = cart.items.find(i => i.product.id === product.id)
    //     if (existing) {
    //         existing.quantity += 1
    //     } else {
    //         cart.items.push({ product, quantity:1 })
    //     }
    // },
    // remove(productId) {
    //     cart.items = cart.items.filter(i => i.product.id !== productId)
    // },
    // clear() {
    //     cart.items = []
    // },
    // incrementQuantity(productId) {
    //     const item = cart.items.find(i => i.product.id === productId);
    //     if (item){
    //         item.quantity++
    //     }
    // },
    // decrementQuantity(productId) {
    //     const itemIndex = cart.items.findIndex(i => i.product.id === productId);
    //     if (itemIndex !== -1) {
    //         const item = cart.items[itemIndex];
    //         if (item.quantity > 1) {
    //             item.quantity --;
    //         } else {
    //             this.items.splice(itemIndex, 1)
    //         }
    //     }
    // }
})