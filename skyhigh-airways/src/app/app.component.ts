import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FlightSearchComponent } from './flight-search/flight-search.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ToastrModule } from 'ngx-toastr';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet, 
    FlightSearchComponent, 
    NavbarComponent,
    ToastrModule
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Skyhigh Airways';
}
