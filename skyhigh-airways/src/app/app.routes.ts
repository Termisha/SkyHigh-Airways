import { Routes } from '@angular/router';
import { FlightSearchComponent } from './flight-search/flight-search.component';
import { MyTripsComponent } from './my-trips/my-trips.component';
import { PassengerInfoComponent } from './passenger-info/passenger-info.component';

export const routes: Routes = [
    {path: 'home', component: FlightSearchComponent},
    {path: 'flights', component: FlightSearchComponent},
    {path: 'my-trips', component: MyTripsComponent},
    {path: 'passenger', component: PassengerInfoComponent},
];
