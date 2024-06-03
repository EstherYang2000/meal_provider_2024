import { Restaurant, ResIDUserRole } from './../../../shared/model/Restaurant';
import { Component, OnInit, Input } from '@angular/core';
import { FoodService } from '../../../services/food.service';
import { Food, FoodRes } from '../../../shared/model/Food';
import { CommonModule } from '@angular/common';
import {
  ActivatedRoute,
  RouterLink,
  RouterLinkActive,
  RouterOutlet,
} from '@angular/router';
import { SearchComponent } from '../search/search.component';
import { TagComponent } from '../tag/tag.component';
import { NotFoundComponent } from '../not-found/not-found.component';
import { RestaurantTypeComponent } from '../restaurant-type/restaurant-type.component';
import { FoodSearchComponent } from '../food-search/food-search.component';
import {
  FormGroup,
  FormBuilder,
  FormControl,
  ReactiveFormsModule,
} from '@angular/forms';
import { NewFood } from '../../../shared/model/addfood';
import { Campus_name } from '../../../shared/model/Campus_name';
import { ApiService } from '../../../services/api.service';
import { UserService } from '../../../services/user.service';

@Component({
  selector: 'app-restaurant-page',
  standalone: true,
  imports: [
    CommonModule,
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    SearchComponent,
    TagComponent,
    NotFoundComponent,
    RestaurantTypeComponent,
    FoodSearchComponent,
    ReactiveFormsModule,
  ],
  templateUrl: './restaurant-page.component.html',
  styleUrls: ['./restaurant-page.component.css'],
})
export class RestaurantPageComponent implements OnInit {
  campus_name: Campus_name[] = [];
  food!: FoodRes[];
  restaurant_id: string = '';
  newfood!: FormGroup;
  newfoodObj: NewFood = new NewFood();
  api_input: ResIDUserRole = {
    role: '',
    restaurant_id: '',
  };

  @Input() userRole: string | null = null;
  @Input() userid: string | null = null;

  constructor(
    private foodService: FoodService,
    private activateRoute: ActivatedRoute,
    private formBuilder: FormBuilder,
    private apiService: ApiService,
    private userService: UserService
  ) {
    this.activateRoute.params.subscribe((params) => {
      console.log(params, 'params'); // 输出参数
      if (params['id']) {
        var res_id_user_role: ResIDUserRole = {
          role: 'employee',
          restaurant_id: params['id'],
        };
        this.api_input = res_id_user_role;
        this.apiService.getFoods(res_id_user_role).subscribe((res) => {
          this.food = res;
          console.log(res, 'API response');
          console.log(this.food, 'api response');

          if (params['food-searchTerm']) {
            console.log(params['food-searchTerm'], 'input food-searchTerm');
            console.log(this.food, 'inner food data');
            this.food = this.foodService.getAllFoodBySearchTerm(
              this.food,
              params['food-searchTerm']
            );
            console.log(this.food, 'food-searchTerm results');
          }
        });
      }
    });

    this.newfood = this.formBuilder.group({
      category: [''],
      item_name: [''],
      description: [''],
      price: [''],
      image_url: [''],
    });

    this.userRole = this.userService.getUserRole();
    this.userid = this.userService.getUserId();
    console.log('header', this.userRole, this.userid);
  }

  ngOnInit(): void {}

  addFood() {
    this.newfoodObj.category = this.newfood.value.category;
    this.newfoodObj.item_name = this.newfood.value.item_name;
    this.newfoodObj.description = this.newfood.value.description;
    this.newfoodObj.price = this.newfood.value.price;
    this.newfoodObj.imageUrl = this.newfood.value.image_url;
    this.newfoodObj.availibility = true;
    this.newfoodObj.change_status = 'ADD';
    this.newfoodObj.restaurant_id = this.restaurant_id;
    console.log(this.newfoodObj);
    this.apiService.Change_menu(this.newfoodObj).subscribe({
      next: (res) => {
        console.log(res);
      },
      error: (err) => {
        console.log(err);
      },
    });
  }
}
