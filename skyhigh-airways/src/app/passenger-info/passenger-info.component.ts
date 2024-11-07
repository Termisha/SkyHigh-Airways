import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar'; 
import { SharedModule } from '../shared.module';

@Component({
  selector: 'app-passenger-info',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, HttpClientModule, SharedModule],
  templateUrl: './passenger-info.component.html',
  styleUrl: './passenger-info.component.css'
})
export class PassengerInfoComponent {
  passengerForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient, private snackBar: MatSnackBar) {
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
    if (this.passengerForm.invalid) {
      this.snackBar.open('Please fill out the form correctly.', 'Close', {
        duration: 3000, // 3 seconds duration
        panelClass: ['error-snackbar'] // Style class for error messages
      });
      return;
    }

    if (this.passengerForm.valid) {
      const passengerData = this.passengerForm.value;  // This should contain the right keys
      console.log(passengerData); // Check the data in the console before sending the request

      this.http.post('http://localhost:5000/api/passengers', passengerData)
        .subscribe(
        (response) => {
          console.log("Passenger added successfully", response);
          // Show success message
          this.snackBar.open('Passenger added successfully!', 'Close', {
            duration: 3000, // 3 seconds duration
            panelClass: ['success-snackbar'] // Style class for success messages
          });
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
