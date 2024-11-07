import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-passenger-info',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, HttpClientModule],
  templateUrl: './passenger-info.component.html',
  styleUrl: './passenger-info.component.css'
})
export class PassengerInfoComponent {
  passengerForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient) {
    this.passengerForm = this.fb.group({
      firstName: ['', [Validators.required, Validators.pattern('[a-zA-Z ]*')]],
      lastName: ['', [Validators.required, Validators.pattern('[a-zA-Z ]*')]],
      dateOfBirth: ['', Validators.required],
      gender: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      phoneNumber: ['', [Validators.required, Validators.pattern('^[0-9]{10,15}$')]]
    });
  }

  get f() { return this.passengerForm.controls; }

  onSubmit() {
    console.log("Inside on Submit function")
    if (this.passengerForm.valid) {
      const passengerData = this.passengerForm.value;  // This should contain the right keys
      console.log(passengerData); // Check the data in the console before sending the request

      this.http.post('http://localhost:5000/api/passengers', passengerData)
        .subscribe(
        (response) => {
          console.log("Passenger added successfully", response);
          // Clear the form after successful submission
          this.passengerForm.reset();
        },
        (error) => {
          console.log("Error:", error);
        }
      );
    } else {
      this.passengerForm.markAllAsTouched();
    }
  }
}
