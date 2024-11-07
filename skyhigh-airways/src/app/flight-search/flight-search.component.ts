import { HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { FlightService } from '../services/flight.service';

@Component({
  selector: 'app-flight-search',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, HttpClientModule],
  templateUrl: './flight-search.component.html',
  styleUrl: './flight-search.component.css'
})
export class FlightSearchComponent implements OnInit {
  searchForm: FormGroup; // Define a form group for search form
  flights: any[] = []; // Variable to store fetched flights

  // Loading state and error message variables
  isLoading: boolean = false;
  errorMessage: string = '';

  constructor(private fb: FormBuilder, private flightService: FlightService) {
    // Define the search form with validation
    this.searchForm = this.fb.group({
      origin: ['', Validators.required],        // Origin city
      destination: ['', Validators.required],   // Destination city
      //travelDate: ['', Validators.required],    // Travel date
      // numPassengers: ['', [Validators.required, Validators.min(1)]] // Number of passengers
    });
    
  }

  ngOnInit(): void {}

  searchFlights(): void {
    console.log('Inside searchFlights():');
    // Check if the form is valid before submitting
    if (this.searchForm.invalid) {
      console.log("Form is invalid");
      return;
    }

    // Start loading
    console.log("Searching flights...");
    this.isLoading = true;
    this.errorMessage = '';

    // Extract form values
    const { origin, destination } = this.searchForm.value;
    console.log({ origin, destination });

    // Call the service to fetch available flights
    this.flightService.searchFlights(origin, destination).subscribe(
    //this.flightService.searchFlights(origin, destination).subscribe(
      (data) => {
        console.log("Flight data received:", data);
        this.flights = data;
        this.isLoading = false;
      },
      (error) => {
        this.errorMessage = 'An error occurred while fetching flights.';
        console.error(error);
        this.isLoading = false;
      }
    );
  }

  selectFlight(flight: any): void {
    // Logic for handling the selection of a flight
    // ToDo: Update later on to display flight information
    console.log('Selected flight:', flight);
    // Redirect or store selected flight for next page
  }
}
