import { ActivatedRoute, Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { Component, OnInit,Input } from '@angular/core';
import { Food } from '../../../shared/model/Food';
import { FoodService } from '../../../services/food.service';
import { CommonModule } from '@angular/common';
import { CartService } from '../../../services/cart.service';
import { NotFoundComponent } from '../not-found/not-found.component';
import { MenuManipulateService } from '../../../services/menu-manipulate.service';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../../services/api.service';
import { UserService } from '../../../services/user.service'; 
@Component({
  selector: 'app-food-page',
  standalone: true,
  imports: [CommonModule, FormsModule, NotFoundComponent, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './food-page.component.html',
  styleUrls: ['./food-page.component.css']
})
export class FoodPageComponent implements OnInit {
  food!: Food;
  newFood: Food = new Food();
  newPrice!: number;
  @Input() userRole: string | null = null;
  @Input() userid: string | null = null;
  constructor(
    private activatedRoute: ActivatedRoute,
    private foodService: FoodService,
    private cartService: CartService,
    private menuService: MenuManipulateService,
    private router: Router,
    private apiService:ApiService,
    private userService: UserService
  ) {
    this.activatedRoute.params.subscribe((params) => {
      if (params['food-id']) {
        this.food = this.foodService.getFoodById(params['food-id']);
      }
    });
    this.userRole = this.userService.getUserRole();
    
    this.userid = this.userService.getUserId();
  }

  ngOnInit(): void {}

  addToCart() {
    this.cartService.addToCart(this.food);
    const dataToSend = {
      "cart_status": "update",
      "user_id": this.userid,
      "item_id": this.food.id, 
      "quantity": 1
    }
    console.log('Data to send:', dataToSend);
    this.apiService.updateCart(dataToSend).subscribe({
      next: res => {
        console.log(res);
      },
      error: err => {
        console.log(err);
      }
    });
    this.router.navigateByUrl('/cart-page');
  }

  addNewFood() {
    this.menuService.addFood(this.newFood);
    this.newFood = new Food(); // Reset the form
  }

  deleteFood() {
    //this.menuService.deleteFood(this.food.id);
    const dataToSend = {
      "change_status":"DELETE",
      "item_id":this.food.id,
      "availability":this.food.availibility,
    }
    console.log('Data to send:', dataToSend);
    this.apiService.Change_menu(dataToSend).subscribe({
      next: res => {
        console.log(res);
      },
      error: err => {
        console.log(err);
      }
    });
    this.router.navigateByUrl(''); // Redirect to home after deletion
  }

  updateFoodPrice() {
    //const newPrice = prompt('Enter new price:', this.food.price.toString());
    console.log('New price:', this.newPrice);
    
      const dataToSend = {
        "change_status":"ADJUST",
        "item_id":this.food.id,
        "price":Number(this.newPrice),
      }
      console.log('Data to send:', dataToSend);
      this.apiService.Change_menu(dataToSend).subscribe({
        next: res => {
          console.log(res);
        },
        error: err => {
          console.log(err);
        }
      });
      this.router.navigateByUrl(''); // Redirect to home after deletion
      //this.menuService.updateFoodPrice(this.food.id, parseFloat(newPrice));
      //this.food.price = parseFloat(newPrice); // Update the displayed price
    
  }
}
