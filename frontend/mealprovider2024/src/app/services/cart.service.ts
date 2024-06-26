import { Injectable } from '@angular/core';
import { Cart } from '../shared/model/Cart';
import { BehaviorSubject, Observable } from 'rxjs';
import { Food, FoodRes } from '../shared/model/Food';
import { CartItem } from '../shared/model/CartItem';

@Injectable({
  providedIn: 'root',
})
export class CartService {
  private cart: Cart = new Cart();
  private cartSubject: BehaviorSubject<Cart> = new BehaviorSubject(this.cart);
  constructor() {}
  //Add to Cart Method
  addToCart(food: FoodRes[]): void {
    let cartItem = this.cart.items.find(
      (item) => item.food.item_id === food[0].item_id
    );
    if (cartItem) return;
    this.cart.items.push(new CartItem(food[0]));
    this.setCartToLocalStorage();
  }
  //Remove Cart Item
  removeFromCart(foodId: string): void {
    this.cart.items = this.cart.items.filter(
      (item) => item.food.item_id != foodId
    );
    this.setCartToLocalStorage();
  }
  //Change Quantity
  changeQuantity(foodId: string, quantity: number) {
    let cartItem = this.cart.items.find((item) => item.food.item_id === foodId);
    if (!cartItem) return;

    cartItem.quantity = quantity;
    cartItem.price = quantity * cartItem.food.price;
    this.setCartToLocalStorage();
  }
  //Clear Cart
  clearCart() {
    this.cart = new Cart();
    this.setCartToLocalStorage();
  }
  //Get Cart Observable mean check Observable data
  getCartObservable(): Observable<Cart> {
    return this.cartSubject.asObservable();
  }
  //Now Set LocalStorage Data
  private setCartToLocalStorage(): void {
    this.cart.totalPrice = this.cart.items.reduce(
      (prevSum, currentItem) => prevSum + currentItem.price,
      0
    );
    this.cart.totalCount = this.cart.items.reduce(
      (prevSum, currentItem) => prevSum + currentItem.quantity,
      0
    );

    const cartJson = JSON.stringify(this.cart); //Convert value into json string
    localStorage.setItem('Cart', cartJson);
    this.cartSubject.next(this.cart);
  }
  //When ever Set Local Storage Data then Get Data
  private getCartFromLocalStorage(): Cart {
    const cartJson = localStorage.getItem('Cart');
    return cartJson ? JSON.parse(cartJson) : new Cart(); //Convert json into object
  }
}
