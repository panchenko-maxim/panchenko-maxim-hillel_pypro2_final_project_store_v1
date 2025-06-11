import { reactive } from 'vue';

export const cart = reactive({
    items: [],
    add(product) {
        const existing = cart.items.find(i => i.product.id === product.id)
        if (existing) {
            existing.quantity += 1
        } else {
            cart.items.push({ product, quantity:1 })
        }
    },
    remove(productId) {
        cart.items = cart.items.filter(i => i.product.id !== productId)
    },
    clear() {
        cart.items = []
    },
    incrementQuantity(productId) {
        const item = cart.items.find(i => i.product.id === productId);
        if (item){
            item.quantity++
        }
    },
    decrementQuantity(productId) {
        const itemIndex = cart.items.findIndex(i => i.product.id === productId);
        if (itemIndex !== -1) {
            const item = cart.items[itemIndex];
            if (item.quantity > 1) {
                item.quantity --;
            } else {
                this.items.splice(itemIndex, 1)
            }
        }
    }
})