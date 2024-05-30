import { Component, OnInit } from '@angular/core';
import { FoodService } from '../../../services/food.service';
import { Food } from '../../../shared/model/Food';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { SearchComponent } from '../search/search.component';
import { TagComponent } from '../tag/tag.component';
import { NotFoundComponent } from '../not-found/not-found.component';
import { Restaurant } from '../../../shared/model/Restaurant';
import { RestaurantService } from '../../../services/restaurant.service';
import { RestaurantTypeComponent } from '../restaurant-type/restaurant-type.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive, SearchComponent, TagComponent, NotFoundComponent, RestaurantTypeComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  food: Food[] = [];
  restaurant: Restaurant[] = [];
  constructor(private restaurantService: RestaurantService, private activateRoute: ActivatedRoute) {
    this.activateRoute.params.subscribe((params) => {
      if (params['searchTerm']) {
        this.restaurant = this.restaurantService.getAllRestaurantBySearchTerm(params['searchTerm']);
      } else if (params['tag-type']) {
        this.restaurant = this.restaurantService.getAllRestaurantByTag(params['tag-type']);
      } else {
        this.restaurant = this.restaurantService.getAll();
      }
    });
  }

  ngOnInit(): void {}
}