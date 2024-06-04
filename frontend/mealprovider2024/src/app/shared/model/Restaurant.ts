import { Restaurant_Type } from './Restaurant_Type';
export class Restaurant {
  restaurant_id!: string; //restaurant_id
  restaurant_name!: string; //restaurant_name
  type!: string; //restaurant_type
  restaurant_type!: string; //restaurant_type
  image_url!: string; //image_url
  campus!: string; //campus
  campus_building!: string; //fab
  canteen_number!: string; //canteen_number
}
// Generated by https://quicktype.io
export interface RestaurantInfo {
  restaurant_id: string;
  restaurant_type: string;
  restaurant_name: string;
  image_url: string;
  campus_building: string;
  canteen_number: string;
} // Generated by https://quicktype.io

// Generated by https://quicktype.io

export interface AllRestaurant {
  stand_id: string;
  restaurant_id: string;
  name: string;
  type: string;
  address: string;
  phone: string;
  campus_building: string;
  canteen_number: string;
  floor: string;
  meal_types: string[];
  operating_hours: string;
  campus: string;
} // Generated by https://quicktype.io

export interface ResIDUserRole {
  role: string | null;
  restaurant_id: string;
} // Generated by https://quicktype.io

export interface Restaurantinfomation {
  restaurant_id: string;
  type: string;
  name: string;
  image_url: string;
  campus_building: string;
  canteen_number: string;
  campus: string;
}
