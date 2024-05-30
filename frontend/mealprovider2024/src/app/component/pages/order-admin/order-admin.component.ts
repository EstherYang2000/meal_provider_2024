import { Component } from '@angular/core';
import { Order_Kitchen } from '../../../shared/model/Order';
import { CommonModule } from '@angular/common';
import { FormGroup,FormBuilder,FormControl,ReactiveFormsModule, Validators} from '@angular/forms';

@Component({
  selector: 'app-order-admin',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './order-admin.component.html',
  styleUrl: './order-admin.component.css'
})
export class OrderAdminComponent {
  orders: Order_Kitchen[] = [];
  ngOnInit() {
    // Example data
    this.orders = [
      {
        customer_id: 'C001',
        order_id: 'O1001',
        order_date: '2024-05-01',
        confirmed_date: '2024-05-01',
        prepared_date: '2024-05-02',
        completed_date: '2024-05-03',
        canceled_date: '',
        items: [
          { item_id: '101', item_name: 'Burger', quantity: 2, unit_price: 5.99 },
          { item_id: '102', item_name: 'Fries', quantity: 1, unit_price: 2.99 }
        ],
        order_status: 'PENDING',
        total_price: 14.97,
        paid: true
      },
      {
        customer_id: 'C002',
        order_id: 'O1002',
        order_date: '2024-05-02',
        confirmed_date: '2024-05-02',
        prepared_date: '2024-05-03',
        completed_date: '',
        canceled_date: '',
        items: [
          { item_id: '103', item_name: 'Pizza', quantity: 1, unit_price: 12.99 },
          { item_id: '104', item_name: 'Soda', quantity: 2, unit_price: 1.99 }
        ],
        order_status: 'PREPARED',
        total_price: 16.97,
        paid: false
      },
      {
        customer_id: 'C003',
        order_id: 'O1003',
        order_date: '2024-05-03',
        confirmed_date: '2024-05-03',
        prepared_date: '',
        completed_date: '',
        canceled_date: '',
        items: [
          { item_id: '105', item_name: 'Pasta', quantity: 1, unit_price: 10.99 },
          { item_id: '106', item_name: 'Salad', quantity: 1, unit_price: 6.99 }
        ],
        order_status: 'CONFIRMED',
        total_price: 17.98,
        paid: true
      },
      {
        customer_id: 'C004',
        order_id: 'O1004',
        order_date: '2024-05-04',
        confirmed_date: '2024-05-04',
        prepared_date: '',
        completed_date: '',
        canceled_date: '2024-05-05',
        items: [
          { item_id: '107', item_name: 'Steak', quantity: 1, unit_price: 19.99 },
          { item_id: '108', item_name: 'Mashed Potatoes', quantity: 1, unit_price: 4.99 }
        ],
        order_status: 'CANCELED',
        total_price: 24.98,
        paid: true
      },
      {
        customer_id: 'C005',
        order_id: 'O1005',
        order_date: '2024-05-05',
        confirmed_date: '2024-05-05',
        prepared_date: '2024-05-06',
        completed_date: '2024-05-07',
        canceled_date: '',
        items: [
          { item_id: '109', item_name: 'Sushi', quantity: 1, unit_price: 14.99 },
          { item_id: '110', item_name: 'Miso Soup', quantity: 1, unit_price: 3.99 }
        ],
        order_status: 'COMPLETED',
        total_price: 18.98,
        paid: false
      }
    ]
  }
  months = [
    { name: 'January', value: 0 },
    { name: 'February', value: 1 },
    { name: 'March', value: 2 },
    { name: 'April', value: 3 },
    { name: 'May', value: 4 },
    { name: 'June', value: 5 },
    { name: 'July', value: 6 },
    { name: 'August', value: 7 },
    { name: 'September', value: 8 },
    { name: 'October', value: 9 },
    { name: 'November', value: 10 },
    { name: 'December', value: 11 }
  ];
  monthForm:FormGroup;
  constructor(private fb: FormBuilder) {
    this.monthForm = this.fb.group({
      month: ['', Validators.required]
    });
  }
  submit_month() {
    const formValue = this.monthForm.value;
    const monthValue = Number(formValue.month);
    const monthValue2 = monthValue +Number(1);
    const year = new Date().getFullYear();
    const firstDay = new Date(year, monthValue, 2);
    const lastDay = new Date(year, monthValue2, 1);
    
    const dataToSend = {
      "start_date": firstDay.toISOString().split('T')[0],
      "end_date": lastDay.toISOString().split('T')[0],
      "restaurant_id":"C46"
      //firstDay: firstDay,
      //lastDay: lastDay
    };
    
    console.log('Data to send:', dataToSend);
    // Here you can add the logic to send dataToSend to your server.
  }
  selectedOrder: any = null;
  selectOrder(order: any) {
    this.selectedOrder = order;
  }
  submit(order_id:string,order_status_before:string,flag:Number) {
    
    if(flag===0){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'PREPARED',
        
      }
      console.log('Data to send:', dataToSend);
    }
    else if(flag===1){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'CONFIRMED',
        
      }
      console.log('Data to send:', dataToSend);
    }
    else if(flag===2){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'CANCELED',
      }
      console.log('Data to send:', dataToSend);
    }
  
    
  }
  

}
