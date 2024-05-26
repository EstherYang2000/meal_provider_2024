import { Routes } from '@angular/router';
import { HomeComponent } from './component/pages/home/home.component';
import { FoodPageComponent } from './component/pages/food-page/food-page.component';
import { CartPageComponent } from './component/pages/cart-page/cart-page.component';
import { LoginComponent } from './component/pages/login/login.component';

export const routes: Routes = [
  {path: '', component: HomeComponent},

  {path: 'search/:searchTerm', component: HomeComponent},

  {path: 'tag/:tag', component: HomeComponent},

  {path: 'food/:id', component: FoodPageComponent},

  {path: 'cart-page', component: CartPageComponent},
  
  {path: 'header', component: HomeComponent},
  {path: 'dashboard', component: HomeComponent},
  {path: 'profile', component: HomeComponent},
  {path: 'order', component: HomeComponent},
  {path: 'login', component: LoginComponent},
  {path: 'logout', component: HomeComponent}

];
